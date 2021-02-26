# -*- coding: utf-8 -*- 
# @Time : 2021/2/26 14:28 
# @Author : dujun
# @describe : describe
# @File : college.py

from Interface_Yss.data import Account
from Interface_Yss.Common.Base_Request import Base_requests
from Interface_Yss.data.caps import Caps


class college_project:

    def __init__(self, environment):
        self.re = Base_requests()
        self.caps = Caps(env=environment)

    ##平台登录
    def login(self, data=''):
        url = self.caps['college'] + '/login'
        if data == '':
            response = self.re.post(url=url, data=Account.yuanXiao)
        else:
            response = self.re.post(url=url, data=data)
        return response
