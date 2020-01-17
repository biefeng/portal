# -*- coding:utf-8 -*-
# author : BieFeNg
# date_time 2020/01/15 11:12
# file_name : views.py
from flask.views import MethodView
from flask import render_template, Blueprint, current_app
from ..config import APP_NAME
from pluggy import HookimplMarker
from ..utils.helper import registry_view
import logging

logger = logging.getLogger(__name__)


class Login(MethodView):
    def get(self, user_id):
        data = list()
        logger.debug("logging the login operation")
        for i in range(5):
            element = dict()
            element["name"] = "Idea 部署Wep-app: " + str(i)
            element["abbreviation"] = "如何部署web app"
            data.append(element)
        return render_template("blog/blog_list.html", data=data)

    def post(self):
        data = {"name": "BieFeNg"}
        return render_template("base.html", data=data)


user_bp = Blueprint("user", __name__, url_prefix="/user")
registry_view(user_bp, routes=["/login/<int:user_id>"], view_func=Login.as_view("login"))
