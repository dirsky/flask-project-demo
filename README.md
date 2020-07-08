# flask-project-demo

```
python -m venv venv
```

创建gitignore
创建flaskr, tests

```shell
flask init-db
```

```shell
export FLASK_APP=flaskr
export FLASK_ENV=development
```

set FLASK_APP=flaskr
set FLASK_ENV=development
flask run

安装打包依赖
pip install wheel

生成安装文件（在dist下）
python setup.py bdist_wheel

安装
pip install flaskr-1.0.0-py3-none-any.whl

运行
export FLASK_APP=flaskr
首先得通过flask进行数据库初始化
flask init-db
pip install waitress
waitress-serve --call 'flaskr:create_app'


├── flaskr/
│   ├── __init__.py
│   ├── db.py
│   ├── schema.sql
│   ├── auth.py
│   ├── blog.py
│   ├── templates/
│   │   ├── base.html
│   │   ├── auth/
│   │   │   ├── login.html
│   │   │   └── register.html
│   │   └── blog/
│   │       ├── create.html
│   │       ├── index.html
│   │       └── update.html
│   └── static/
│       └── style.css
├── tests/
│   ├── conftest.py
│   ├── data.sql
│   ├── test_factory.py
│   ├── test_db.py
│   ├── test_auth.py
│   └── test_blog.py
├── venv/
├── setup.py
└── MANIFEST.in
