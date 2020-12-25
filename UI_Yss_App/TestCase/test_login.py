# -*- coding: utf-8 -*- 
# @Time : 2020/12/15 19:41 
# @Author : dujun
# @describe : describe
# @File : test_login.py
import pytest
from UI_Yss_App.Base.driver_Setting import desired_caps
from UI_Yss_App.Page.My_Button import My
import unittest


class Test_Login(unittest.TestCase):
    ##初始化MY,我的页面元素对象
    page = My(desired_caps)
    page.My_button.click()
    page.head_photo.click()
    ##获取上下文
    cons = page.driver.contexts
    print(cons)

    ##page.driver._switch_to.context('WEBVIEW_stetho_cn.artstudent.app')

    ##用户名输入不正确
    def test_case1(self):
        errorMessage = '用户名输入不正确'
        try:
            ##用户名输入框
            self.page.username.click()
            self.page.driver.press_keycode(12)
            print(self.page.username.get_attribute())
            ##密码输入框
            self.page.password.click()
            self.page.driver.press_keycode(12)
            ##提交登录
            self.page.loginButton.click()
            ##捕捉toast提示
            self.message = '//*[@text=\'{}\']'.format(errorMessage)
            toast = self.page.By_Xpath(self.message)
            print(toast)
        except Exception:
            print(Exception)

    def test_case2(self):
        pass


if __name__ == "__main__":
    run = Test_Login()
    run.test_case1()
