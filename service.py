# !/usr/bin/env python
# _*_ coding:utf-8 _*_
# -= dynamic_plugin_service/service.py coding by scott in 2023/4/13 15:32 with IDE:PyCharm on Mac =-
import importlib
import os
import traceback

from flask import Flask, request, jsonify

from utils import get_logger, CustomError

app = Flask(__name__)

logger = get_logger('service')
# 插件文件夹名称
plugins_folder = 'plugins'


def call_plugin(plugin_name, plugin_method, method_data):
    plugin_path = f'{plugins_folder}.{plugin_name}'  # 构造插件的完整路径
    plugin_module = importlib.import_module(plugin_path)  # 动态加载插件
    func = getattr(plugin_module, plugin_method)  # 动态引用函数/方法
    return func(method_data)


def raw_data_handler():
    files = os.listdir(plugins_folder)
    content_type = request.content_type
    # 1.获取原始数据解析插件
    for file in files:
        if not file.startswith('raw_'):
            continue
        plugin_name = file.split('.py')[0]
        plugin_path = f'{plugins_folder}.{plugin_name}'
        plugin_module = importlib.import_module(plugin_path)
        importlib.reload(plugin_module)
        match_type = plugin_module.match_type
        # 2.根据原始数据类型匹配插件
        if not match_type == content_type:
            continue
        # 3.通过插件解析规则判断数据是否满足要求，对满足要求的数据进行处理
        func = getattr(plugin_module, 'check_data')
        if not func():
            continue
        run_plugin = getattr(plugin_module, 'run_plugin')
        return run_plugin()
    return {}


@app.route("/plugin/service", methods=["POST", 'GET'])
def plugins():
    rsp = {
        'status': 'success',
        'code': 0
    }
    try:
        rq_method = request.method
        data = request.get_json()
        if rq_method == 'GET':
            args = request.args
        else:
            plugin_name = data.get('plugin')
            plugin_method = data.get('method')
            method_data = data.get('data')
            if not (plugin_name and plugin_method):
                rsp.update({
                    'status': 'failure',
                    'code': -1
                })
                raise CustomError
            ret = call_plugin(plugin_name, plugin_method, method_data)
            rsp.update({
                'data': ret
            })
    except CustomError:
        logger.info(traceback.format_exc())
    except Exception as e:
        logger.error(e)
        logger.info(traceback.format_exc())
        rsp.update({
            'status': 'failure',
            'code': -1
        })
    finally:
        return jsonify(rsp)


@app.route("/raw/service", methods=["POST", 'GET'])
def raw():
    rsp = dict()
    rq_method = request.method
    if rq_method == 'GET':
        pass
    else:
        logger.info(request.content_type)
        logger.info(request.data)
        rsp = raw_data_handler()
        # rsp = {'content_type': request.content_type}
    return jsonify(rsp)


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5050, debug=True)
