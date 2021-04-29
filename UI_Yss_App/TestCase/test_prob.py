# -*- coding: utf-8 -*-
# @Time : 2021/4/6 9:30
# @Author : dujun
# @describe : 录取概率
# @File : test_prob.py
import os
import time

import allure
import pytest
from uiautomator2.xpath import TimeoutException

from UI_Yss_App.Common.photoTailor import imgTailor
from UI_Yss_App.Common.photoContrast import *


class TestProb_tools:

    def setup_class(self):
        pass

    def teardown_class(self):
        pass

    @pytest.mark.run
    @allure.story('概率工具：操作说明')
    def test_probTools_case1(self, mainView, probView):
        try:
            time.sleep(1)
            mainView.AppInit_PassBtn()
            time.sleep(2)
            advertising = mainView.isElement('Id', 'cn.artstudent.app:id/img')
            if advertising:
                mainView.probAlterCancel()
        except Exception:
            pass

        mainView.probButton()
        mainView.swipe_up()
        # probView.volunteer_tools(1)
        # time.sleep(4)
        # os.popen('adb shell screencap -p /sdcard/screen.png')
        # os.popen(r'adb pull /sdcard/screen.png D:\pythonProject\UI_Yss_App\photo')
        # os.popen('adb shell rm /sdcard/screen.png')
        # path = r'D:\pythonProject\UI_Yss_App\photo\screen.png'
        # time.sleep(2)
        # imgTailor(path,'zixunInfo')
        # # 均值哈希比较
        # path1 = r'D:\pythonProject\UI_Yss_App\photo\zixunInfo.png'
        # path2 = r'D:\pythonProject\UI_Yss_App\photo\zixunInfoRaw.png'
        # img_one = cv2.imread(path1)
        # img_two= cv2.imread(path2)
        # hash_one = aHash(img_one)
        # hash_two = aHash(img_two)
        # os.remove(r'D:\pythonProject\UI_Yss_App\photo\screen.png')
        # value = cmpHash(hash_one, hash_two)
        # try:
        #     if value <= 2 :
        #         print('Hash值对比：',value)
        #     else:
        #         raise BaseException('图片hash值相差较大',value)
        # except:
        #     pass
        # mainView.btn_back(1)

    @allure.story('概率工具：热门院校')
    def test_probTools_case2(self, probView, mainView):
        probView.volunteer_tools(2)
        time.sleep(5)
        rawMessage = '热门院校'
        title = probView.probTools_title()
        try:
            title = probView.probTools_title()
            assert rawMessage == title
        except:
            pass
        mainView.btn_back(1)
        assert title == rawMessage

    @allure.story('概率工具：历年分数')
    def test_probTools_case3(self, probView, mainView):
        rawMessage = '历年分数'
        probView.volunteer_tools(3)
        time.sleep(5)
        try:
            title = probView.probTools_title()
            assert rawMessage == title
        except:
            pass
        mainView.btn_back(1)

    @allure.story('概率工具：综合分计算')
    def test_probTools_case4(self, probView, mainView):
        rawMessage = '综合分计算器'
        probView.volunteer_tools(4)
        time.sleep(5)
        title = probView.probTools_title()
        assert rawMessage == title
