# flask-project-demo

### 环境准备
```
python -m venv venv
```

创建文件gitignore
创建文件夹flaskr, tests

```shell
# windows
set FLASK_APP=flaskr
set FLASK_ENV=development
```

```shell
# linux
export FLASK_APP=flaskr
export FLASK_ENV=development
```

flask init-db
flask run

### 打包和安装

安装打包依赖
pip install wheel

生成安装文件（在dist下）
python setup.py bdist_wheel

安装
pip3 install flaskr-1.0.0-py3-none-any.whl

### 部署运行
export FLASK_APP=flaskr
首先得通过flask进行数据库初始化
db_path: /usr/local/python3.7/var/flaskr-instance/flaskr.sqlite

centos 加python3 -m
python3 -m flask init-db

pip3 install waitress
mac:     waitress-serve --call 'flaskr:create_app'
windows: waitress-serve --call flaskr:create_app
centos:  python3 -m waitress --call 'flaskr:create_app'

### 目录结构

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
