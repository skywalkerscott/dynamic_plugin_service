# !/usr/bin/env python
# _*_ coding:utf-8 _*_
# -= dynamic_plugin_service/utils.py coding by scott in 2023/4/13 15:33 with IDE:PyCharm on Mac =-
import logging
import os
from logging.handlers import TimedRotatingFileHandler


def get_logger(log_file_name, level='INFO'):
    """
    获取logger
    Args:
        log_file_name:日志名称
        level:日志等级，默认INFO
    Returns:
    """
    # 日志名称需要以.log结尾
    if not str(log_file_name).endswith(".log"):
        log_file_name = log_file_name + ".log"
    logger = logging.getLogger(log_file_name)
    current_path = os.path.split(os.path.abspath(__file__))[0]
    log_root = current_path + "/logs/"
    if not os.path.exists(log_root):
        os.mkdir(log_root)
    log_handler = TimedRotatingFileHandler(os.path.normpath(log_root + log_file_name), 'MIDNIGHT',
                                           backupCount=7)
    log_handler.suffix = "%Y-%m-%d"
    # formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(funcName)s - %(lineno)d - %(message)s')
    formatter = logging.Formatter(
        '[%(asctime)s] %(levelname)s [%(filename)s %(funcName)s - line:%(lineno)s] %(message)s')

    log_handler.setFormatter(formatter)
    if log_handler not in logger.handlers:
        logger.addHandler(log_handler)
    logger.setLevel(level.upper())
    return logger


class CustomError(Exception):
    def __init__(self, message=None):
        self.message = message or 'undefined error'

    def __str__(self):
        return repr(self.message)
