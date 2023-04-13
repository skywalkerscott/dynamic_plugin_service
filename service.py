# !/usr/bin/env python
# _*_ coding:utf-8 _*_
# -= dynamic_plugin_service/service.py coding by scott in 2023/4/13 15:32 with IDE:PyCharm on Mac =-
import importlib
import traceback

from flask import Flask, request, jsonify

from utils import get_logger, CustomError

app = Flask(__name__)

logger = get_logger('service')


def call_plugin(plugin_name, plugin_method, method_data):
    # 插件文件夹名称
    plugins_folder = 'plugins'
    plugin_path = f'{plugins_folder}.{plugin_name}'  # 构造插件的完整路径
    plugin_module = importlib.import_module(plugin_path)  # 动态加载插件
    func = getattr(plugin_module, plugin_method)  # 动态引用函数/方法
    return func(method_data)


@app.route("/plugin/service", methods=["POST", 'get'])
def plugins():
    rsp = {
        'status': 'success',
        'code': 0
    }
    try:
        rq_method = request.method
        data = request.get_json()
        args = request.args
        # rsp.update({
        #     'data': data,
        #     'args': args
        # })
        if rq_method == 'GET':
            pass
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


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5050, debug=True)
