# -*- coding: utf-8 -*-
# @Time : 2021/1/22 22:19
# @Author : dujun
# @describe : 实例化page页面
# @File :conftest.py

import pytest
from UI_Yss_App.Page.My_Button import myPage
from UI_Yss_App.Page.examHomePage import examMainPage, examSubject_info
from UI_Yss_App.Page.mainPage import mainPage


@pytest.fixture(scope='session')
def test_my(driver):
    MyPage = myPage(driver)
    ##若重置App,需要调用此方法进行前置动作
    MyPage.startApp()
    return MyPage


##实例化mainPage-App首页
@pytest.fixture(scope='session')
def mainView(driver):
    mainView = mainPage(driver)
    return mainView


##实例化网络考试页面-录制页面
@pytest.fixture(scope='session')
def examMain(driver):
    register = examMainPage(driver)
    return register


##实例化网络考试页面-科目详情
@pytest.fixture(scope='session')
def subjectInfo(driver):
    subjectInfo = examSubject_info(driver)
    return subjectInfo
