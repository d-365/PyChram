# -*- coding: utf-8 -*- 
# @Time : 2020/12/11 10:37 
# @Author : dujun
# @describe : AppiumBase页面
# @File : Base.py
from selenium.webdriver.support.wait import WebDriverWait
from UI_Yss_App.Common.pressKeyCode import pressKeyCode

class Base:
    ##基础配置
    def __init__(self, driver):
        self.driver = driver

    # ID定位
    def By_ID(self, element=None, OverText=None):
        return WebDriverWait(self.driver, 6, 0.5).until(lambda X: self.driver.find_element_by_id(element), OverText)

    # Xpath定位
    def By_Xpath(self, element=None, OverText=None):
        return WebDriverWait(self.driver, 6, 0.5).until(lambda X: self.driver.find_element_by_xpath(element), OverText)

    ##className定位
    def by_class_name(self, element=None, OVerText=None):
        return WebDriverWait(self.driver, 6, 0.5).until(lambda X: self.driver.find_element_by_class_name(element),
                                                        OVerText)

    ##获取元素属性
    def get_attribute(self, method=None, ele=None):
        location = self.driver.find_element(method, ele, )
        location.click()
        return location.get_attribute()

    ##clear()清除文本框数值
    def Clear(self):
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
