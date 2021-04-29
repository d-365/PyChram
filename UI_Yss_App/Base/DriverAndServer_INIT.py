# -*- coding: utf-8 -*-
# @Time : 2021/4/19 15:07
# @Author : dujun
# @describe : 多进程启动appiumServer,driver
# @File : DriverAndServer_INIT.py

from appium import webdriver
import yaml
from time import ctime
import multiprocessing

path = r'D:\pythonProject\UI_Yss_App\Base\desired_caps.yaml'
with open(path, 'r')as file:
    data = yaml.load(file, Loader=yaml.FullLoader)

devices_list = ['2b17bb80', 'CLB0218728003757']


def appium_desire(udid, port):
    desired_caps = {}
    desired_caps['platformName'] = data['platformName']
    desired_caps['platformVersion'] = str(data['platformVersion'])
    desired_caps['deviceName'] = data['deviceName']
    desired_caps['udid'] = udid
    desired_caps['appPackage'] = data['appPackage']
    desired_caps['appActivity'] = data['appActivity']
    desired_caps['noReset'] = data['noReset']
    desired_caps['automationName'] = data['automationName']
    print('appium port: %s start run %s at %s' % (port, udid, ctime()))
    driver = webdriver.Remote('http://' + str(data['ip']) + ':' + str(port) + '/wd/hub', desired_caps)
    driver.implicitly_wait(5)
    return driver


desired_process = []
for i in range(0, len(devices_list)):
    port = 4723 + 2 * i
    desired = multiprocessing.Process(target=appium_desire, args=(devices_list[i], port))
    desired_process.append(desired)

if __name__ == "__main__":
    for desired in desired_process:
        desired.start()
    for desired in desired_process:
        desired.join()
