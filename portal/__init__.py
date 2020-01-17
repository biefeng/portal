# -*- coding:utf-8 -*-
# author : BieFeNg
# date_time 2020/01/14 22:04
# file_name : __init__.py.py

import logging

from flask import Flask, render_template_string, redirect
from flask_blogging import SQLAStorage, BloggingEngine
from flask_login import UserMixin, LoginManager, login_user, logout_user
from flask_migrate import Migrate

from ._compat import *
from .config import APP_NAME, get_database
from .shard import db

logger = logging.getLogger(__name__)


def configure_app(app, config):
    # app.pluggy = PluginManager(APP_NAME)
    pass


# def load_plugins(app):
#     app.pluggy.add_hookspecs(CustomSpec)
#     app_modules = set(
#         module
#         for name, module in iteritems(sys.modules)
#         if name.startswith(APP_NAME)
#     )
#     for module in app_modules:
#         app.pluggy.register(module)


def configure_blueprints(app):
    # app.pluggy.hook.app_or_blueprint_load_route(app=app)
    from .user.views import user_bp
    bps = [
        user_bp
    ]

    for bp in bps:
        app.register_blueprint(bp)


def configure_db(app):
    # 配置数据库链接
    app.config['SQLALCHEMY_DATABASE_URI'] = get_database(app)['SQLALCHEMY_DATABASE_URI']
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = get_database(app)['SQLALCHEMY_TRACK_MODIFICATIONS']
    db.init_app(app)


def configure_blogging(app):
    app.config["SECRET_KEY"] = "secret"  # for WTF-forms and login
    app.config["BLOGGING_URL_PREFIX"] = "/blog"
    app.config["BLOGGING_DISQUS_SITENAME"] = "test"
    app.config["BLOGGING_SITEURL"] = "http://localhost:8989"
    app.config["BLOGGING_SITENAME"] = "BieFeNg"
    app.config["BLOGGING_KEYWORDS"] = ["blog", "meta", "keywords"]
    app.config["FILEUPLOAD_IMG_FOLDER"] = "fileupload"
    app.config["FILEUPLOAD_PREFIX"] = "/fileupload"
    app.config["FILEUPLOAD_ALLOWED_EXTENSIONS"] = ["png", "jpg", "jpeg", "gif"]

    with app.app_context():
        sql_storage = SQLAStorage(db=db)
    blog_engine = BloggingEngine(app=None, storage=sql_storage)
    login_manager = LoginManager(app)

    # blog_engine.init_app(app, sql_storage)

    class User(UserMixin):
        def __init__(self, user_id):
            self.id = user_id

        def get_name(self):
            return "Paul Dirac"  # typically the user's name

    @login_manager.user_loader
    @blog_engine.user_loader
    def load_user(user_id):
        return User(user_id)

    index_template = """
    <!DOCTYPE html>
    <html>
        <head> </head>
        <body>
            {% if current_user.is_authenticated %}
                <a href="/logout/"> Logout </a>
            {% else %}
                <a href="/login/"> Login </a>
            {% endif %}
            &nbsp&nbsp<a href="/blog/"> Blog </a>
            &nbsp&nbsp<a href="/blog/sitemap.xml">Sitemap</a>
            &nbsp&nbsp<a href="/blog/feeds/all.atom.xml">ATOM</a>
            &nbsp&nbsp<a href="/fileupload/">FileUpload</a>
        </body>
    </html>
    """

    @app.route("/")
    def index():
        return render_template_string(index_template)

    @app.route("/login/")
    def login():
        user = User("testuser")
        login_user(user)
        return redirect("/blog")

    @app.route("/logout/")
    def logout():
        logout_user()
        return redirect("/")


def create_app():
    app = Flask(__name__)
    configure_app(app, None)
    # load_plugins(app)
    configure_db(app)
    configure_blueprints(app)
    configure_blogging(app)
    # for bp in bps:
    #     portal.register_blueprint(bp)
    # 配置文件上传上限Size：16M
    app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024

    Migrate(app, db)
    return app
