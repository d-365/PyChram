# -*- coding: utf-8 -*-
# @Time : 2021/1/22 22:19
# @Author : dujun
# @describe : 实例化page页面
# @File :conftest.py
import pytest
from UI_Yss_App.Page.My_Button import myPage
from UI_Yss_App.Page.enrollProbabilityPage import probPage
from UI_Yss_App.Page.examHomePage import examMainPage, examSubject_info
from UI_Yss_App.Page.mainPage import mainPage
from UI_Yss_App.Base.driver_config import desired_caps
from UI_Yss_App.Page.StuProduction_appraisePage import stuProduction_appraise_webView, stuProduction_appraise_native
from faker import Faker
from UI_Yss_App.Page.AndroidCommonPage import androidCommon

@pytest.fixture(scope='session')
def faker():
    f = Faker(locale='zh_CN')
    return f


@pytest.fixture(scope='session')
def myView(driver):
    MyPage = myPage(driver)
    if not desired_caps['noReset']:
        MyPage.resetApp()
    return MyPage


# App首页
@pytest.fixture(scope='session')
def mainView(driver):
    mainView = mainPage(driver)
    return mainView


# 网络考试页面-录制页面
@pytest.fixture(scope='session')
def examMain(driver):
    register = examMainPage(driver)
    return register


# 网络考试页面-科目详情
@pytest.fixture(scope='session')
def subjectInfo(driver):
    subjectInfo = examSubject_info(driver)
    return subjectInfo


# 专业评画webView
@pytest.fixture(scope='session')
def stuAppraiseWebView(driver):
    appraise = stuProduction_appraise_webView(driver)
    return appraise


# 专业评画native
@pytest.fixture(scope='session')
def stuAppraiseNative(driver):
    appraise = stuProduction_appraise_native(driver)
    return appraise


# androidCommonPage
@pytest.fixture(scope='session')
def androidCommonView(driver):
    android = androidCommon(driver)
    return android


# probPage
@pytest.fixture(scope='session')
def probView(driver):
    prob = probPage(driver)
    return prob
