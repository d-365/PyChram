# -*- coding: utf-8 -*- 
# @Time : 2020/12/15 19:41
# @Author : dujun
# @describe : App登录页面
# @File : test_login.py

from UI_Yss_App.Common.pressKeyCode import pressKeyCode
import datetime
import time
import pytest
from UI_Yss_App.Config.logger import log


def setup_module():
    global startTime
    global logger
    # 实例化logger对象
    logger = log()
    logger.adbLogCat()
    startTime = datetime.datetime.now()
    print('登录用例执行开始时间', startTime)


def teardown_module():
    endTime = datetime.datetime.now()
    print('用例耗时', endTime - startTime)
    logger.kill_adbServer()


class Test_Login:
    pressKey = pressKeyCode()

    ##用户名输入不正确(toast)
    def test_case1(self, page):
        errorMessage = '用户名输入不正确'
        try:
            ##用户名输入框
            page.username.click()
            page.press_keyCode('h')
            ##密码输入框
            page.password.click()
            page.press_keyCode('h')
            ##提交登录
            page.loginButton.click()
            ##捕捉toast提示
            message = '//*[@text=\'{}\']'.format(errorMessage)
            toast = page.By_Xpath(message)
            assert toast.text == errorMessage
            logger.info("test_case1,用户名输入不正确,执行成功")
        except AssertionError:
            logger.error('case1执行失败')

    ##密码输入长度不正确（toast）
    def test_case2(self, page):
        errorMessage = '密码输入长度不正确'
        try:
            ##用户名输入框
            page.username.click()
            page.press_keyCode('a', 'i', 't', 'u', 'n', '2')
            ##密码输入框
            page.password.click()
            page.press_keyCode('a', 'i')
            ##提交登录
            page.loginButton.click()
            ##捕捉toast提示
            message = '//*[@text=\'{}\']'.format(errorMessage)
            toast = page.By_Xpath(message)
            assert toast.text == errorMessage
            logger.info("test_case2,密码输入长度不正确,执行完毕")
        except AssertionError:
            logger.error('case2执行失败')

    ##登录名或密码不正确（弹窗）
    def test_case3(self, page):
        try:
            errorMessage = '登录名或密码不正确'
            ##密码输入框
            page.password.click()
            page.press_keyCode('t', 'u', 'n')
            ##提交登录
            page.loginButton.click()
            ##处理alter
            alter_message = page.By_ID('cn.artstudent.app:id/message')
            alter_button = page.By_ID('cn.artstudent.app:id/positiveButton')
            alter_button.click()
            logger.info('test_case3,执行成功')
        except Exception:
            logger.error('case3执行失败')

    ##正确的用户名密码,完成登录
    def test_case4(self, page):
        try:
            ##密码输入框
            page.driver.implicitly_wait(3)
            page.password.click()
            page.password.clear()
            page.driver.press_keycode(self.pressKey['t'], '64')
            page.press_keyCode('e', 's', 't', '1', '2', '3', '4')
            ##提交登录
            page.loginButton.click()
            ##alter处理
            alter_button = page.By_ID('cn.artstudent.app:id/closeDialog')
            alter_button.click()
            logger.info('test_case4,登录成功')
        except Exception:
            logger.error('case4执行失败')

    ##用例执行后,关闭driver
    @pytest.mark.skipif(1 == 1, reason="用例执行完,关闭driver")
    def test_down(self, page):
        time.sleep(3)
        page.driver.quit()


if __name__ == "__main__":
    run = Test_Login()
    run.test_case1()
