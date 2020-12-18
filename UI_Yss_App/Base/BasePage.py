# -*- coding: utf-8 -*- 
# @Time : 2020/12/11 10:37 
# @Author : dujun
# @describe : AppiumBase页面
# @File : BasePage.py
from appium import webdriver
from selenium.webdriver.support.wait import WebDriverWait


class Base:
    ##基础配置
    def __init__(self):
        desired_caps = {
            'platformName': 'Android',
            'platformVersion': '9',
            'deviceName': 'BGR6R19B26016266',
            'appPackage': 'cn.artstudent.app',
            'appActivity': 'cn.artstudent.app.act.app.LaunchActivity',
            'noReset': 'True',
            'automationName': 'UiAutomator1'
        }
        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_capabilities=desired_caps)

    #ID定位
    def By_ID(self, element=None, OverText=None):
        return WebDriverWait(self.driver, 6, 0.5).until(lambda X: self.driver.find_element_by_id(element), OverText)

    #Xpath定位
    def By_Xpath(self,element=None,OverText=None):
        return WebDriverWait(self.driver,6,0.5).until(lambda X: self.driver.find_element_by_xpath(element),OverText)
