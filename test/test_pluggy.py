# -*- coding:utf-8 -*-
# author : BieFeNg
# date_time 2020/01/15 11:25
# file_name : test_pluggy.py

import pluggy

hookspec = pluggy.HookspecMarker("myproject")
hookimpl = pluggy.HookimplMarker("myproject")


class MySpec(object):
    """A hook specification namespace.
    """

    @hookspec
    def myhook(self, arg1, arg2):
        """My special little hook that you can customize.
        """


class Plugin_1(object):
    """A hook implementation namespace.
    """

    @hookimpl
    def myhook(self, arg1, arg2):
        print("inside Plugin_1.myhook()")
        return arg1 + arg2


class Plugin_2(object):
    """A 2nd hook implementation namespace.
    """

    @hookimpl
    def myhook(self, arg1, arg2):
        print("inside Plugin_2.myhook()")
        return arg1 - arg2


# create a manager and add the spec
pm = pluggy.PluginManager("myproject")
pm.add_hookspecs(MySpec)

# register plugins
pm.register(Plugin_1())
pm.register(Plugin_2())

# call our ``myhook`` hook
results = pm.hook.myhook(arg1=1, arg2=2)
# print(results)

"""--------------------------------------"""


def test_base64():
    import base64

    # decode = base64.b64decode("YmllZmVuZzpiaWVmZW5nMTIz")
    decode = base64.b64decode("5B8N1KMUFJPypRBQnF93Y1DedL8BfL2t")
    print(decode)

test_base64()
