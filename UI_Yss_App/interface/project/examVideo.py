# -*- coding: utf-8 -*- 
# @Time : 2021/2/26 11:32 
# @Author : dujun
# @describe : describe
# @File : examVideo.py
from UI_Yss_App.interface.Common.Base_Request import Base_requests
from UI_Yss_App.interface.data.caps import Caps


class examVideo_project:
    def __init__(self, environment):
        self.re = Base_requests()
        self.caps = Caps(env=environment)

    ##考试结果查询,视频列表
    def loadExaminerAssignDetailData(self, data):
        """
        showSubject
        showSchedule
        kaoShiID
        kaoDianID
        riChengId
        riChengID
        """
        url = self.caps['examVideo'] + '/auth/school/assignDetail/loadExaminerAssignDetailData.htm'
        response = self.re.post(url=url, data=data)
        return response
