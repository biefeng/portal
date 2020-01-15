# -*- coding:utf-8 -*-
# author : BieFeNg
# date_time 2020/01/14 22:26
# file_name : user.py

from flask import Blueprint

user = Blueprint("user", __name__, url_prefix="/user")


@user.route("save", methods=["GET"])
def save():
    return "Hello World"
