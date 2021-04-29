# -*- coding: utf-8 -*- 
# @Time : 2020/12/15 19:41
# @Author : dujun
# @describe : App登录页面
# @File : test_login.py

import pytest
from UI_Yss_App.Common.pressKeyCode import pressKeyCode
import datetime
from UI_Yss_App.Base.driver_config import desired_caps
from UI_Yss_App.Config.logger import log

@pytest.mark.skipif(desired_caps['noReset'] == True, reason='noReset为True,无需执行登录用例')
class Test_Login:

    def setup_class(self):
        # 实例化pressKey库
        self.pressKey = pressKeyCode()
        self.startTime = datetime.datetime.now()
        self.logger = log()
        print('----------------------------登录用例执行开始', self.startTime, '----------------------------')

    def teardown_class(self):
        endTime = datetime.datetime.now()
        print('----------------------------登录用例执行完毕用例耗时', endTime - self.startTime, '----------------------------')

    # 输入用户名和密码,未勾选注册协议
    @pytest.mark.repeat(1, scope='function')
    def test_case1(self, myView):
        errorMessage = '请阅读及确认用户协议和隐私政策'
        try:
            myView.usernameText.click()
            myView.press_keyCode('h', 'a', 'i', 't', 'u', 'n')
            myView.passwordText.click()
            myView.press_keyCode('T', 'e', 's', 't', '1', '2', '3', '4')
            ##提交登录
            myView.loginButton.click()
            message = '//*[@text=\'{}\']'.format(errorMessage)
            toast = myView.By_Xpath(message)
            myView.usernameText.clear()
            myView.passwordText.clear()
            assert toast.text == 1
        except:
            self.logger.info('login_case1,注册协议用例执行失败')

    # 用户名输入不正确(toast)
    def test_case2(self, myView):
        errorMessage = '用户名输入不正确'
        try:
            ##用户名输入框
            myView.usernameText.click()
            myView.press_keyCode('h')
            ##密码输入框
            myView.passwordText.click()
            myView.press_keyCode('h')
            try:
                # 勾选用户注册协议
                myView.CheckBox.click()
            except:
                pass
            ##提交登录
            myView.loginButton.click()
            ##捕捉toast提示
            message = '//*[@text=\'{}\']'.format(errorMessage)
            toast = myView.By_Xpath(message)
            assert toast.text == errorMessage
            self.logger.info("test_case2执行成功")
        except AssertionError:
            self.logger.error('case2执行失败')

    # 密码输入长度不正确(toast)
    def test_case3(self, myView):
        errorMessage = '密码输入长度不正确'
        try:
            ##用户名输入框
            myView.usernameText.click()
            myView.press_keyCode('a', 'i', 't', 'u', 'n', '3')
            ##密码输入框
            myView.passwordText.click()
            myView.press_keyCode('a', 'i')
            ##提交登录
            myView.loginButton.click()
            ##捕捉toast提示
            message = '//*[@text=\'{}\']'.format(errorMessage)
            toast = myView.By_Xpath(message)
            assert toast.text == errorMessage
            self.logger.info("test_case3执行完毕")
        except AssertionError:
            self.logger.error('case3执行失败')

    # 登录名或密码不正确(弹窗)
    def test_case4(self, myView):
        try:
            errorMessage = '登录名或密码不正确'
            ##密码输入框
            myView.passwordText.click()
            myView.press_keyCode('t', 'u', 'n')
            ##提交登录
            myView.loginButton.click()
            ##处理alter
            alter_message = myView.By_ID('cn.artstudent.app:id/message')
            alter_button = myView.By_ID('cn.artstudent.app:id/positiveButton')
            alter_button.click()
            # assert alter_message.text ==errorMessage
            myView.usernameText.clear()
            self.logger.info('test_case4,执行成功')
        except Exception:
            self.logger.error('case4执行失败')

    ##正确的用户名密码,完成登录
    # @pytest.mark.skip()
    def test_case5(self, myView):
        try:
            myView.driver.implicitly_wait(3)
            # # 用户名输入框
            myView.usernameText.click()
            myView.usernameText.clear()
            myView.press_keyCode('h', 'a', 'i', 't', 'u', 'n', '3')
            ##密码输入框
            myView.passwordText.click()
            myView.passwordText.clear()
            myView.driver.press_keycode(self.pressKey['t'], '64')
            myView.press_keyCode('e', 's', 't', '1', '2', '3', '4')
            ##提交登录
            myView.loginButton.click()
            ##alter处理
            alter_button = myView.By_ID('cn.artstudent.app:id/closeDialog')
            alter_button.click()
            self.logger.info('test_case5,执行成功,用户登录成功')
        except Exception:
            self.logger.error('case5执行失败')
