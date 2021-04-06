# -*- coding: utf-8 -*- 
# @Time : 2021/2/26 14:46 
# @Author : dujun
# @describe : test_exam对应接口脚本 ：视频录制类视频打回
# @File : exam_VideoBack.py

import pytest

from UI_Yss_App.interface.project.college import college_project
from UI_Yss_App.interface.project.examVideo import examVideo_project
from UI_Yss_App.interface.project.school import school_project


class videoBack:
    """
    考试：日常测试：kaoShiID：2110
    专业：所有模式
    riChengID:30781
    视频录制类科目1： esId: 13703
    监考笔试类科目2： esId: 13704
    """

    def __init__(self):
        env = 'online'
        self.college = college_project(environment=env)
        self.school = school_project(environment=env)
        self.examVideo = examVideo_project(environment=env)

        login_data = {
            "loginName": "海豚_90201",
            "password": "Test1234"
        }
        login_re = self.college.login(data=login_data)
        self.ticket = login_re['ticket']

    # 打回考生视频_视频录制类
    def videoBack1(self, esId):
        query_data = {
            'commitFlag': 1,
            'showSubject': 1,
            'showSchedule': 1,
            'kaoShiID': "2110",
            'kaoDianID': "3100",
            'riChengId': 30781,
            'riChengID': 30781,
            'esId': esId,
            'stuIDCard': 'haitun3',
            'ticket': self.ticket
        }
        response = self.examVideo.loadExaminerAssignDetailData(data=query_data)
        svId = response['datas']['page']['dataList'][0]['svId']

        pwd_data = {
            "authCode": "Test1234",
            "ticket": self.ticket
        }
        res = self.school.pwdAuth(data=pwd_data)
        token = res['datas']['token']

        reset_data = {
            'svId': svId,
            'token': token,
            'ticket': self.ticket
        }
        res = self.school.resetVideo(data=reset_data)
        print('视频录制类对应视频打回成功', res)

    # 监考笔试类视频打回
    def videoBack2(self):
        pass


if __name__ == "__main__":
    run = videoBack()
    run.videoBack1(13703)
