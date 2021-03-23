# -*- coding: utf-8 -*- 
# @Time : 2021/3/19 16:26 
# @Author : dujun
# @describe : describe
# @File : prob.py
from Interface_Yss.Common.Base_Request import Base_requests
from Interface_Yss.data.caps import Caps


class prob_project:
    def __init__(self, environment):
        self.re = Base_requests()
        self.caps = Caps(env=environment)

    ##省份分数线查询
    def loadProvinceScoreLineData(self, data=''):
        url = self.caps['prob'] + '/auth/prob/provinceScoreLine/loadProvinceScoreLineData.htm'
        response = self.re.post(url=url, data=data)
        return response

    ##统考计算公式
    def loadJointScoreExpressionData(self, data=''):
        url = self.caps['prob'] + '/auth/prob/jointScoreExpression/loadJointScoreExpressionData.htm'
        response = self.re.post(url=url, data=data)
        return response

    ##获取App统考成绩列表
    def getUser(self, data=''):
        url = self.caps['prob'] + '/api/m/auth/wish/user/v200630/getUser.ws'
        response = self.re.post(url=url, data=data)
        return response

    # 获取校考成绩列表
    def addSchoolExamList(self, data=''):
        url = self.caps['prob'] + '/api/m/auth/schoolExamList/v200630/addSchoolExamList.ws'
        response = self.re.post(url=url, data=data)
        return response

    # 获取校考计算公式
    def loadSchoolScoreExpressionData(self, data=''):
        url = self.caps['prob'] + '/auth/prob/schoolScoreExpression/loadSchoolScoreExpressionData.htm'
        response = self.re.post(url=url, data=data)
        return response
