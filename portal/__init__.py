# -*- coding:utf-8 -*-
# author : BieFeNg
# date_time 2020/01/14 22:04
# file_name : __init__.py.py

from flask import Flask
from pluggy import PluginManager

from ._compat import *
from .config import APP_NAME
from .plugins.spec import CustomSpec
from .user import views
import logging


# from app.user import user

# bps = [
#     user
# ]


def configure_app(app, config):
    app.pluggy = PluginManager(APP_NAME)


def load_plugins(app):
    app.pluggy.add_hookspecs(CustomSpec)
    sys_modules = iteritems(sys.modules)
    app_modules = set()
    for name, module in sys_modules:
        if name.startswith("app.user.views"):
            app_modules.add(module)

    for module in app_modules:
        app.pluggy.register(module)


def configure_blueprints(app):
    app.pluggy.hook.app_or_blueprint_load_route(app=app)


def create_app():
    app = Flask(__name__)
    configure_app(app, None)
    load_plugins(app)
    configure_blueprints(app)
    # for bp in bps:
    #     app.register_blueprint(bp)
    # 配置数据库链接
    # app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE['SQLALCHEMY_DATABASE_URI']
    # app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = DATABASE['SQLALCHEMY_TRACK_MODIFICATIONS']
    # 配置文件上传上限Size：16M
    app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024
    # db.init_app(app)

    # Migrate(app, db)
    return app
