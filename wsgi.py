# -*- coding:utf-8 -*-
# author : BieFeNg
# date_time 2020/01/17 23:06
# file_name : wsgi.py

import sys

from portal import create_app

if sys.version_info[0] == 2:
    reload(sys)
else:
    import importlib

    importlib.reload(sys)

if sys.getdefaultencoding() != 'utf-8':
    sys.setdefaultencoding("utf-8")

portal = create_app()
