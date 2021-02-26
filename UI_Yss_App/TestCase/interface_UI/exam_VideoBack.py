# -*- coding: utf-8 -*- 
# @Time : 2021/2/26 14:46 
# @Author : dujun
# @describe : test_exam对应接口脚本 ：视频录制类视频打回
# @File : exam_VideoBack.py
import pytest

from Interface_Yss.project.college import college_project
from Interface_Yss.project.school import school_project
from Interface_Yss.project.examVideo import examVideo_project


class videoBack:
    """
    视频录制类——视频打回
    """

    ##打回考生视频
    def videoBack(self):
        env = 'online'
        college = college_project(environment=env)
        school = school_project(environment=env)
        examVideo = examVideo_project(environment=env)
        login_data = {
            "loginName": "海豚_90201",
            "password": "Test1234"
        }
        login_re = college.login(data=login_data)
        self.ticket = login_re['ticket']

        query_data = {
            'showSubject': 1,
            'showSchedule': 1,
            'kaoShiID': "2110",
            'kaoDianID': "3100",
            'riChengId': "30780",
            'riChengID': '30780',
            'stuIDCard': 'haitun3',
            'ticket': self.ticket
        }
        response = examVideo.loadExaminerAssignDetailData(data=query_data)
        self.svId = response['datas']['page']['dataList'][0]['svId']

        pwd_data = {
            "authCode": "Test1234",
            "ticket": self.ticket
        }
        res = school.pwdAuth(data=pwd_data)
        self.token = res['datas']['token']

        reset_data = {
            'svId': self.svId,
            'token': self.token,
            'ticket': self.ticket
        }
        res = school.resetVideo(data=reset_data)
        print(res)
