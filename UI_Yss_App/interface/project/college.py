# -*- coding: utf-8 -*- 
# @Time : 2021/2/26 14:28 
# @Author : dujun
# @describe : describe
# @File : college.py
from UI_Yss_App.interface.Common.Base_Request import Base_requests
from UI_Yss_App.interface.data import Account
from UI_Yss_App.interface.data.caps import Caps


class college_project:

    def __init__(self, environment):
        self.re = Base_requests()
        self.caps = Caps(env=environment)

    # 平台登录
    def login(self, data=''):
        url = self.caps['college'] + '/login'
        if data == '':
            response = self.re.post(url=url, data=Account.yuanXiao)
        else:
            response = self.re.post(url=url, data=data)
        return response
