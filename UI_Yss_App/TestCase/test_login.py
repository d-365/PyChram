# -*- coding: utf-8 -*- 
# @Time : 2020/12/15 19:41 
# @Author : dujun
# @describe : describe
# @File : test_login.py
import pytest
from UI_Yss_App.Page.My_Button import My


class Test_Login:
    ##初始化MY,我的页面元素对象
    page = My()
    page.My_button.click()
    page.head_photo.click()

    def test_case1(self):
        pass


if __name__ == "__main__":
    run = Test_Login()
    run.test_case1()