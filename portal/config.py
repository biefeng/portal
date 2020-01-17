# -*- coding:utf-8 -*-
# author : BieFeNg
# date_time 2020/01/15 11:42
# file_name : config.py
from flask import current_app
import os

APP_NAME = "portal"


def get_database(app, type=None):
    MYSQL = {
        'SQLALCHEMY_DATABASE_URI': 'mysql+pymysql://root:Biefeng123!@192.168.186.137/recosys',
        'SQLALCHEMY_POOL_SIZE': 10,
        'SQLALCHEMY_POOL_RECYCLE': 3600,
        'SQLALCHEMY_TRACK_MODIFICATIONS': False,
        'SQLALCHEMY_ENGINE_OPTIONS': {
            'mysql_engine': 'InnoDB'
        }
    }

    SQLITE = {
        'SQLALCHEMY_TRACK_MODIFICATIONS': False
    }

    with app.app_context():
        SQLITE["SQLALCHEMY_DATABASE_URI"] = "sqlite:///" + os.path.join(os.path.dirname(current_app.instance_path),
                                                                        "test.db")
    if type is None or type not in ["mysql", "sqlite"]:
        return SQLITE
    elif type == "mysql":
        return MYSQL
