# -*- coding: utf-8 -*- 
# @Time : 2021/1/22 22:19 
# @Author : dujun
# @describe : describe
# @File : pyTest测试固件

import pytest
from UI_Yss_App.Base.Base import Base
from appium import webdriver
from UI_Yss_App.Base.driver_Setting import desired_caps
from UI_Yss_App.Page.My_Button import My


##链接Appium服务,初始化driver,进入我的页面
@pytest.fixture(scope='session')
def page():
    ##初始化MY(driver)我的元素页面
    d = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
    page = My(driver=d)
    ##初始化App，点击我知道了, 'noReset'为 True 时忽略
    try:
        Know = page.By_ID('cn.artstudent.app:id/btn')
        Know.click()
        ##点击我的按钮
        page.My_button.click()
        ## 关闭头像框提示：App生命周期只出现一次
        page.close_MyNotice.click()
        ##点击头像
        page.head_photo.click()
        return page
    except Exception:
        pass

##获取上下文
# cons = page.driver.contexts
# print(cons)
##page.driver._switch_to.context('WEBVIEW_stetho_cn.artstudent.app')
