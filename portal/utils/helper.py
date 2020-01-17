# -*- coding:utf-8 -*-
# author : BieFeNg
# date_time 2020/01/15 13:39
# file_name : helper.py


def registry_view(root, routes, view_func, *args, **kwargs):
    for route in routes:
        root.add_url_rule(route, view_func=view_func, *args, **kwargs)
