# -*- coding:utf-8 -*-
# author : BieFeNg
# date_time 2020/01/15 11:59
# file_name : spec.py

from pluggy import HookspecMarker
from ..config import APP_NAME

spec = HookspecMarker(APP_NAME)


class CustomSpec:
    @spec
    def app_or_blueprint_load_route(app):
        """app or blueprint used to load route"""
