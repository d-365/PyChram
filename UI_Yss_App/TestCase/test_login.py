# -*- coding: utf-8 -*- 
# @Time : 2020/12/15 19:41 
# @Author : dujun
# @describe : 登录页面
# @File : test_login.py

from appium import webdriver
import pytest
from UI_Yss_App.Base.driver_Setting import desired_caps
from UI_Yss_App.Page.My_Button import My


class Test_Login:

    def setup_class(self):
        ##初始化MY(driver),我的元素页面
        d = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
        self.page = My(driver=d)
        ##点击我的按钮
        self.page.My_button.click()
        ##点击头像
        self.page.head_photo.click()

    # ##获取上下文
    # cons = page.driver.contexts
    # print(cons)
    ##page.driver._switch_to.context('WEBVIEW_stetho_cn.artstudent.app')

    ##用户名输入不正确
    def test_case1(self):
        errorMessage = '用户名输入不正确'
        try:
            ##用户名输入框
            self.page.username.click()
            self.page.driver.press_keycode(12)
            ##密码输入框
            self.page.password.click()
            self.page.driver.press_keycode(12)
            ##提交登录
            self.page.loginButton.click()
            ##捕捉toast提示
            self.message = '//*[@text=\'{}\']'.format(errorMessage)
            toast = self.page.By_Xpath(self.message)
            print(toast)
        except AssertionError:
            print('AssertionError')

    def test_case2(self):
        pass

    @staticmethod
    def teardown_class(self):
        print('执行完毕')


if __name__ == "__main__":
    run = Test_Login()
    run.test_case1()
