# flask-project-demo

### 环境准备
```
python3 -m venv venv
# mac
. venv/bin/activate
# windows
venv\Scripts\activate

pip install Flask
```

创建文件gitignore
创建文件夹flaskr, tests

```shell
# windows, development表示修改代码不用重启，还开启了调试模式（页面显示错误）
set FLASK_APP=flaskr
set FLASK_ENV=development

# linux
export FLASK_APP=flaskr
export FLASK_ENV=development

flask init-db
# 默认监听127.0.0.1
flask run
# 监听所有网络
flask run --host=0.0.0.0

```

### 测试

pytest -s
测试的是已经install的app

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
centos:  python3 -m waitress --port=5000 --call flaskr:create_app





**问题：**
pip install uwsgi 之后，运行uwsgi 报错：[uwsgi: command not found]

**解决方案：**建立软链接 
ln -s /usr/local/python3.7/bin/uwsgi /usr/bin/uwsgi


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
