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

    # Android,press_keyCode 模拟按键输入
    def press_keyCode(self, *par):
        press_key = pressKeyCode()
        for i in range(0, len(par)):
            ele = par[i]
            self.driver.press_keycode(press_key[ele])

    # 向左滑动
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

    # 向上滑动
    def swipe_up(self, start_y=0.9, end_y=0.1):
        x = self.driver.get_window_size()['width']
        y = self.driver.get_window_size()['height']
        x1 = int(x * 0.1)
        y1 = int(y * start_y)
        x2 = int(x * 0.1)
        y2 = int(y * end_y)
        time.sleep(2)
        self.driver.swipe(x1, y1, x2, y2, duration=1000)

    # App截图
    def screenCap(self, screenCapName):
        os.popen(r'adb shell screencap -p /sdcard/%s.png' % screenCapName)
        os.popen(r'adb pull /sdcard/%s.png D:\pythonProject\UI_Yss_App\screenCap' % screenCapName)

    # 捕获toast提示
    def catch_toast(self, rawMessage, OverText=None):
        # messages = '//*[@text=\'{}\']'.format(rawMessage)
        messages = "//*[contains(@text,{}) ]".format(rawMessage)
        toastWebDriver = WebDriverWait(self.driver, 5, 0.5).until(
            lambda X: self.driver.find_element_by_xpath(messages), OverText)
        return toastWebDriver.text

    # 捕获toast提示
    def catchToast_full(self, rawMessage, OverText=None):
        messages = "//*[@text = {}]".format(rawMessage)
        toastWebDriver = WebDriverWait(self.driver, 5, 0.5).until(
            lambda X: self.driver.find_element_by_xpath(messages), OverText)
        return toastWebDriver.text

    # 获取屏幕尺寸
    def get_screenSize(self):
        w = self.driver.get_window_size()['width']
        h = self.driver.get_window_size()['height']
        return w, h

    # 坐标定位(相对定位)
    def tap_relative(self, point_x, point_y):
        w = self.driver.get_window_size()['width']
        h = self.driver.get_window_size()['height']
        # 比例系数
        ratio_x = point_x / w
        ratio_y = point_y / h
        self.driver.tap([(ratio_x * w, ratio_y * h)])

    # 切换上下文至H5
    def switch_h5(self, contexts):
        self.driver.switch_to.context(contexts)

    # 切换上下文至native
    def switch_native(self, contexts):
        self.driver.switch_to.context(contexts)

    # assertIN 包含
    def assertIn(self, short, long):
        """
        :param short:
        :param long:
        """
        if short in long:
            pass
        else:
            raise Exception(print(long, '中不包含', short))

    # Android 退格键
    def androidKey_Del(self, num):
        press_key = pressKeyCode()
        for i in range(0, num):
            self.driver.press_keycode(press_key['KEYCODE_DEL'])
