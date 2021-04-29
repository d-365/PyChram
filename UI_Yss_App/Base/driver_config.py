# -*- coding: utf-8 -*-
# @Time : 2020/12/21 19:25
# @Author : dujun
# @describe : ⼿机驱动对象初始化
# @File : driver_config.py
import subprocess

from appium import webdriver
import os
import re

# 获取设备型号
devicesCode = os.popen('adb devices').readlines()
deviceID = re.findall(r'^\w*\b', devicesCode[1])

# 获取设备版本
androidPlatformVersion = os.popen('adb shell getprop ro.build.version.release').readlines()
androidVersion = re.findall(r'^\w*\b', androidPlatformVersion[0])

desired_caps = {
    # 手机系统信息
    'platformName': 'Android',
    'platformVersion': androidVersion[0],
    'deviceName': deviceID[0],
    # 待测APP信息
    'appPackage': 'cn.artstudent.app',
    'appActivity': 'cn.artstudent.app.act.app.LaunchActivity',
    # 启动前是否重置App,False,True
    'noReset': True,
    # 自动化引擎
    'automationName': 'UiAutomator2',
    # appium指令最长等待时间
    'newCommandTimeout': 120,
    # 自动同意系统权限
    'autoGrantPermissions': True,
    # 'chromeOptions': {'androidProcess': 'cn.artstudent.app:tools'}
    # ##App安装包位置
    # # 'app': r"C:\Users\Administrator\Downloads\Yss.apk",
    # 'newCommandTimeout ': 0
}


class Singleton(object):
    driver = None

    def __new__(cls, *args, **kw):
        if not hasattr(cls, '_instance'):
            orig = super(Singleton, cls)

            cls._instance = orig.__new__(cls, *args, **kw)
            cls._instance.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
        return cls._instance


class DriverClient(Singleton):

    def get_driver(self):
        return self.driver


def appium_start(host='127.0.0.1', port=4723):
    bootstrap_port = str(port + 1)
    cmd = 'start  appium -a ' + host + ' -p ' + str(port) + ' -bp ' + str(bootstrap_port)
    print(cmd)
    subprocess.Popen(cmd, shell=True, stderr=subprocess.STDOUT)


def appium_end(host=4723):
    try:
        cmd = 'netstat -ano | findstr %d' % host
        result = os.popen(cmd).readlines()
        resultList = result[0]
        portList = re.findall(r'\d+', resultList)
        port = portList[-1]
        killCmd = "taskkill -f -pid  %s" % port
        subprocess.Popen(killCmd, shell=True)
    except IndexError:
        print('appium PID 未查询到,请检查传入的端口号')


if __name__ == '__main__':
    appium_end()
