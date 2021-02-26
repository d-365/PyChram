# -*- coding: utf-8 -*- 
# @Time : 2021/2/8 14:51 
# @Author : dujun
# @describe : describe
# @File : test_case1.py 

from UI_Yss_App.Base.driver_config import Singleton


class TestCase1:

    def testcase1(self, logger):
        print(Singleton.desired_caps['noReset'])


if __name__ == "__main__":
    run = TestCase1()
