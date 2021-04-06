# -*- coding: utf-8 -*- 
# @Time : 2021/3/4 15:52 
# @Author : dujun
# @describe : 专业评测
# @File : eval.py
from UI_Yss_App.interface.Common.Base_Request import Base_requests
from UI_Yss_App.interface.data.caps import Caps


class eval_project:

    def __init__(self, environment):
        self.re = Base_requests()
        self.caps = Caps(env=environment)

    ##提交评测作品
    def save_stu_evaluation(self, data):
        url = self.caps['eval'] + '/api/m/auth/paint/v200929/save_stu_evaluation.htm'
        response = self.re.post(url=url, data=data)
        return response

    ##查询我的折扣
    def query_my_discounts(self, data):
        url = self.caps['eval'] + '/api/m/auth/paint/v200929/query_my_discounts.htm'
        response = self.re.post(url=url, data=data)
        return response

    ##提交评画订单
    def commit_evaluation_order(self, data):
        url = self.caps['eval'] + '/api/m/auth/paint/v200929/commit_evaluation_order.htm'
        response = self.re.post(url=url, data=data)
        return response
