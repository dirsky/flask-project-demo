import sqlite3

import click
from flask import current_app, g
from flask.cli import with_appcontext

'''
g 是一个特殊对象，独立于每一个请求。
在处理请求过程中，它可以用于储存 可能多个函数都会用到的数据。
把连接储存于其中，可以多次使用，而不用在同一个 请求中每次调用 get_db 时都创建一个新的连接。
'''


def get_db():
    if 'db' not in g:
        g.db = sqlite3.connect(
            current_app.config['DATABASE'],
            detect_types=sqlite3.PARSE_DECLTYPES
        )
        g.db.row_factory = sqlite3.Row

    print("db_path:",current_app.config['DATABASE'])

    return g.db


def close_db(e=None):
    db = g.pop('db', None)

    if db is not None:
        db.close()


def init_db():
    db = get_db()

    with current_app.open_resource('schema.sql') as f:
        db.executescript(f.read().decode('utf8'))


@click.command('init-db')
@with_appcontext
def init_db_command():
    """Clear the existing data and create new tables."""
    init_db()
    click.echo('Initialized the database.')


def init_app(app):

    # 告诉 Flask 在返回响应后进行清理的时候调用此函数。
    app.teardown_appcontext(close_db)

    # 在工厂中导入并调用这个函数。
    # 在工厂函数中把新的代码放到 函数的尾部，返回应用代码的前面。
    app.cli.add_command(init_db_command)
