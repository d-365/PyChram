# -*- coding: utf-8 -*- 
# @Time : 2020/12/15 19:41 
# @Author : dujun
# @describe : 登录页面
# @File : test_login.py

from appium import webdriver
from selenium.webdriver.common.by import By
from UI_Yss_App.Base.driver_Setting import desired_caps
from UI_Yss_App.Page.My_Button import My


class Test_Login:

    def __init__(self):
        ##初始化MY(driver)我的元素页面
        d = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
        self.page = My(driver=d)
        ##初始化App，点击我知道了, 'noReset'为 True 时忽略
        Know = self.page.By_ID('cn.artstudent.app:id/btn')
        Know.click()
        ##self.page.find_element_and_click(Know)
        ##点击我的按钮
        self.page.My_button.click()
        ## 关闭头像框提示：App生命周期只出现一次
        self.page.close_MyNotice.click()
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
            message = '//*[@text=\'{}\']'.format(errorMessage)
            print(message)
            toast = self.page.By_Xpath(message)
            print(toast)
            assert toast == errorMessage
        except AssertionError:
            print('toast提示未定位到', AssertionError)

    def test_case2(self):
        pass

    @staticmethod
    def teardown(self):
        print('执行完毕')


if __name__ == "__main__":
    run = Test_Login()
    run.test_case1()
