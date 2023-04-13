# !/usr/bin/env python
# _*_ coding:utf-8 _*_
# -= dynamic_plugin_service/demo.py coding by scott in 2023/4/13 18:05 with IDE:PyCharm on Mac =-


class Demo:
    @staticmethod
    def test(data=None):
        write(data or '')


def write(*args):
    with open('demo.txt', mode='a', encoding='utf8') as f:
        for i in args:
            f.write(str(i))


def run_plugin(*args):
    Demo().test(*args)
