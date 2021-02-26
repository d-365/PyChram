# -*- coding: utf-8 -*-
# @Time : 2021/2/4 11:46
# @Author : dujun
# @describe : 对logging日志进行封装
# @File : logger.py
import logging
import logging.handlers
import os
import subprocess
import time


# class Singleton(object):
#     def __new__(cls,*args,**kwargs):
#         if not hasattr(cls,'_inst'):
#             cls._inst=super(Singleton,cls).__new__(cls,*args,**kwargs)
#         return cls._inst

class log(object):
    def __init__(self, level='info'):
        ##实例化logger对象
        self.logger = logging.getLogger()
        ##日志等级
        levels = {
            'noset': logging.NOTSET,
            'debug': logging.DEBUG,
            'info': logging.INFO,
            'warning': logging.WARNING,
            'error': logging.ERROR,
            'critical': logging.CRITICAL
        }
        ##判断创建日志文件保存目录
        logs_dir = 'log/console'
        if os.path.exists(logs_dir) and os.path.isdir(logs_dir):
            pass
        else:
            os.mkdir(logs_dir)
        ##修改log日志文件保存位置
        timestamp = time.strftime("console%Y-%m-%d", time.localtime())
        logFileName = '%s.txt' % timestamp
        ##文件保存位置
        logFilePath = os.path.join(logs_dir, logFileName)

        ##文件句柄rotatingFileHandler
        rotatingFileHandler = logging.handlers.RotatingFileHandler(logFilePath, maxBytes=1024 * 200, backupCount=3)
        ##rotatingFileHandler.setLevel(logging.DEBUG)

        ##控制台句柄StreamHandler
        consoleHandle = logging.StreamHandler()
        ##consoleHandle.setLevel(logging.DEBUG)

        ##设置日志格式
        formatter = logging.Formatter("%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s")
        ##formatter = logging.Formatter('%(asctime)s-%(name)s-%(filename)s-[line:%(lineno)d]-%(levelname)s-[日志信息]: %(message)s',datefmt='%a, %d %b %Y %H:%M:%S')
        rotatingFileHandler.setFormatter(formatter)
        consoleHandle.setFormatter(formatter)

        ##添加内容到句柄中
        self.logger.addHandler(rotatingFileHandler)
        self.logger.addHandler(consoleHandle)
        self.logger.setLevel(levels[level])

    def debug(self, message):
        self.logger.debug(message)

    def info(self, message):
        self.logger.info(message)

    def warning(self, message):
        self.logger.warning(message)

    def error(self, message):
        self.logger.error(message)

    def critical(self, message):
        self.logger.critical(message)

    ##捕获程序运行异常
    def error(self, message):
        self.logger.error(message, exc_info=True)

    ##捕获APP运行日志
    def adbLogCat(self):
        ##app运行日志存放目录
        AppLogs_dir = 'log/App'
        if os.path.exists(AppLogs_dir) and os.path.isdir(AppLogs_dir):
            pass
        else:
            os.mkdir(AppLogs_dir)
        ##获取当前时间
        timestamp = time.strftime("%Y-%m-%d", time.localtime())
        ##设置文件名
        fileName = '%s.txt' % timestamp
        ##加载文件路径
        appLogPath = os.path.join(AppLogs_dir, fileName)
        ##执行adb logcat 命令
        command = "adb logcat -v time > %s" % appLogPath
        ##执行command
        subprocess.Popen("adb logcat -c")
        subprocess.Popen(command, stdout=subprocess.PIPE, shell=True)

    ##关闭adb服务
    def kill_adbServer(self):
        subprocess.Popen('adb kill-server')


if __name__ == "__main__":
    logger = log(level='debug')
    logger.info('查看是否生成了log文件')
    # logger.adbLogCat()
    # logger.kill_adbServer()
