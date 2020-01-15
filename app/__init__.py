# -*- coding:utf-8 -*-
# author : BieFeNg
# date_time 2020/01/14 22:04
# file_name : __init__.py.py

from flask import Flask

from app.user import user

bps = [
    user
]


def create_app():
    app = Flask(__name__)

    for bp in bps:
        app.register_blueprint(bp)
    # 配置数据库链接
    # app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE['SQLALCHEMY_DATABASE_URI']
    # app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = DATABASE['SQLALCHEMY_TRACK_MODIFICATIONS']
    # 配置文件上传上限Size：16M
    app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024
    # db.init_app(app)

    # Migrate(app, db)
    return app
