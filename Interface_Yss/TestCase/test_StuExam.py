# -*- coding: utf-8 -*- 
# @Time : 2020/12/23 17:23 
# @Author : dujun
# @describe : 视频录制类考试
# @File : test_StuExam.py
from Interface_Yss.Common.Base_Request import Base_requests
from Interface_Yss.data import Interface_data
import pytest


class Test_stuExam:

    def setup(self):
        self.re = Base_requests()

    ##考生登录
    def test_stuLogin(self):
        response = self.re.post(Interface_data.stu_loginUrl, headers=Interface_data.header,
                                data=Interface_data.stu_Base_data)
        self.ticket = response[0]['ticket']
        assert response[0]['datas']['user']['extInfo']['shenFenZH'] == Interface_data.stu_Base_data['loginName']

    ##querySubjectInfo
    def test_querySubjectInfo(self):
        pass

    @staticmethod
    def teardown_class():
        print('运行结束')
