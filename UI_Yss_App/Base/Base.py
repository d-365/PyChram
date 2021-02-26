# -*- coding: utf-8 -*- 
# @Time : 2020/12/11 10:37 
# @Author : dujun
# @describe : AppiumBase页面
# @File : Base.py
import os
import time

from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from UI_Yss_App.Common.pressKeyCode import pressKeyCode


class Base(object):
    # 基础配置
    def __init__(self, driver: WebDriver):
        self.driver = driver

    # ID定位
    def By_ID(self, element=None, OverText=None):
        return WebDriverWait(self.driver, 10, 0.5).until(lambda X: self.driver.find_element_by_id(element), OverText)

    # Xpath定位
    def By_Xpath(self, element=None, OverText=None):
        return WebDriverWait(self.driver, 6, 0.5).until(lambda X: self.driver.find_element_by_xpath(element), OverText)

    ##className定位
    def by_class_name(self, element=None, OVerText=None):
        return WebDriverWait(self.driver, 6, 0.5).until(lambda X: self.driver.find_element_by_class_name(element),
                                                        OVerText)

    ##clear()清除文本框数值
    def clear(self):
        pass

    ## 定位并点击元素
    def find_element_and_click(self, type, value):
        if type == 'ID':
            self.driver.find_element_by_id(value).click()
        elif type == 'Xpath':
            self.driver.find_element_by_xpath(value).click()

    ##Android,press_keyCode 模拟按键输入
    def press_keyCode(self, *par):
        press_key = pressKeyCode()
        for i in range(0, len(par)):
            ele = par[i]
            self.driver.press_keycode(press_key[ele])

    ##向左滑动
    def swipe_left(self, start_x=0.9, end_x=0.1):

        x = self.driver.get_window_size()['width']
        y = self.driver.get_window_size()['height']

        x1 = int(x * start_x)
        x2 = int(x * end_x)
        y1 = int(y * 0.5)
        y2 = int(y * 0.5)
        self.driver.swipe(x1, y1, x2, y2, duration=2000)

    ##向右滑动
    def swipe_right(self, start_x=0.1, end_x=0.9):
        x = self.driver.get_window_size()['width']
        y = self.driver.get_window_size()['height']

        x1 = int(x * start_x)
        x2 = int(x * end_x)
        y1 = int(y * 0.5)
        y2 = int(y * 0.5)
        self.driver.swipe(x1, y1, x2, y2, duration=1000)

    ##向下滑动
    def swipe_down(self, start_y=0.1, end_y=0.9):
        x = self.driver.get_window_size()['width']
        y = self.driver.get_window_size()['height']
        x1 = int(x * 0.1)
        y1 = int(y * start_y)
        x2 = int(x * 0.1)
        y2 = int(y * end_y)
        time.sleep(2)
        self.driver.swipe(x1, y1, x2, y2, duration=1000)

    ##向上滑动
    def swipe_up(self, start_y=0.9, end_y=0.1):
        x = self.driver.get_window_size()['width']
        y = self.driver.get_window_size()['height']
        x1 = int(x * 0.1)
        y1 = int(y * start_y)
        x2 = int(x * 0.1)
        y2 = int(y * end_y)
        time.sleep(2)
        self.driver.swipe(x1, y1, x2, y2, duration=1000)

    ##App截图
    def screenCap(self, screenCapName):
        os.popen(r'adb shell screencap -p /sdcard/%s.png' % screenCapName)
        os.popen(r'adb pull /sdcard/%s.png D:\pythonProject\UI_Yss_App\screenCap' % screenCapName)

    ##捕获toast提示
    def catch_toast(self, rawMessage, OverText=None):
        messages = '//*[@text=\'{}\']'.format(rawMessage)
        toastWebDriver = WebDriverWait(self.driver, 10, 0.5).until(
            lambda X: self.driver.find_element_by_xpath(messages), OverText)
        return toastWebDriver
