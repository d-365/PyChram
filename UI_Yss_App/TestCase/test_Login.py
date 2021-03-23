# -*- coding: utf-8 -*- 
# @Time : 2020/12/15 19:41
# @Author : dujun
# @describe : App登录页面
# @File : test_login.py

import pytest
from UI_Yss_App.Common.pressKeyCode import pressKeyCode
import datetime
from UI_Yss_App.Base.driver_config import desired_caps


@pytest.mark.skipif(desired_caps['noReset'] == True, reason='noReset为True,无需执行登录用例')
class Test_Login:

    def setup_class(self):
        # 实例化pressKey库
        self.pressKey = pressKeyCode()
        self.startTime = datetime.datetime.now()
        print('----------------------------登录用例执行开始', self.startTime, '----------------------------')

    def teardown_class(self):
        endTime = datetime.datetime.now()
        print('----------------------------登录用例执行完毕用例耗时', endTime - self.startTime, '----------------------------')

    # 用户名输入不正确(toast)
    def test_case1(self, test_my):
        errorMessage = '用户名输入不正确'
        try:
            ##用户名输入框
            test_my.username.click()
            test_my.press_keyCode('h')
            ##密码输入框
            test_my.password.click()
            test_my.press_keyCode('h')
            ##提交登录
            test_my.loginButton.click()
            ##捕捉toast提示
            message = '//*[@text=\'{}\']'.format(errorMessage)
            toast = test_my.By_Xpath(message)
            assert toast.text == errorMessage
            self.logger.info("test_case1执行成功")
        except AssertionError:
            self.logger.error('case1执行失败')

    ##密码输入长度不正确（toast）
    def test_case2(self, test_my):
        errorMessage = '密码输入长度不正确'
        try:
            ##用户名输入框
            test_my.username.click()
            test_my.press_keyCode('a', 'i', 't', 'u', 'n', '2')
            ##密码输入框
            test_my.password.click()
            test_my.press_keyCode('a', 'i')
            ##提交登录
            test_my.loginButton.click()
            ##捕捉toast提示
            message = '//*[@text=\'{}\']'.format(errorMessage)
            toast = test_my.By_Xpath(message)
            assert toast.text == errorMessage
            self.logger.info("test_case2执行完毕")
        except AssertionError:
            self.logger.error('case2执行失败')

    ##登录名或密码不正确（弹窗）
    def test_case3(self, test_my):
        try:
            errorMessage = '登录名或密码不正确'
            ##密码输入框
            test_my.password.click()
            test_my.press_keyCode('t', 'u', 'n')
            ##提交登录
            test_my.loginButton.click()
            ##处理alter
            alter_message = test_my.By_ID('cn.artstudent.app:id/message')
            alter_button = test_my.By_ID('cn.artstudent.app:id/positiveButton')
            alter_button.click()
            self.logger.info('test_case3,执行成功')
        except Exception:
            self.logger.error('case3执行失败')

    ##正确的用户名密码,完成登录
    def test_case4(self, test_my):
        try:
            test_my.driver.implicitly_wait(3)
            # # 用户名输入框
            test_my.username.click()
            test_my.username.clear()
            test_my.press_keyCode('h', 'a', 'i', 't', 'u', 'n', '2')
            ##密码输入框
            test_my.password.click()
            test_my.password.clear()
            test_my.driver.press_keycode(self.pressKey['t'], '64')
            test_my.press_keyCode('e', 's', 't', '1', '2', '3', '4')
            ##提交登录
            test_my.loginButton.click()
            ##alter处理
            alter_button = test_my.By_ID('cn.artstudent.app:id/closeDialog')
            alter_button.click()
            self.logger.info('test_case4,执行成功')
        except Exception:
            self.logger.error('case4执行失败')
