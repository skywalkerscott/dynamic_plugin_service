# !/usr/bin/env python
# _*_ coding:utf-8 _*_
# -= dynamic_plugin_service/raw_demo.py coding by scott in 2023/4/14 18:54 with IDE:PyCharm on Mac =-
from flask import request

match_type = 'application/json'  # 插件接收请求类型
validated_keys = {'a', 'b', 'c'}


# 插件校验数据函数
def check_data(*args):
    data = request.get_json()
    keys = data.keys()
    if validated_keys.difference(set(keys)):
        return False
    return True


# 插件入口执行函数
def run_plugin(*args):
    # 实现插件逻辑
    return {
        'status': 'success',
        'code': 0
    }
