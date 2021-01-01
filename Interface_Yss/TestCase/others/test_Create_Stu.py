# -*- coding: utf-8 -*- 
# @Time : 2020/12/17 19:31 
# @Author : dujun
# @describe : describe
# @File : test_Create_Stu.py

from Interface_Yss.data import Account
from Interface_Yss.data import VideoSchema_Url
from Interface_Yss.Common.Base_Request import Base_requests
import pytest
import requests


class Test_CreateStu:
    # 管理员登录
    def test_ManageLogin(self):
        response = requests.post(url=VideoSchema_Url.login_url, headers=VideoSchema_Url.header,
                                 data=Account.manage_Account)
        self.ticket = response.json()['ticket']

    ##管理员创建考生
    def test_Create_Stu(self):
        response = requests.post(url=VideoSchema_Url.Create_StuUrl, headers=VideoSchema_Url.header, data='')


if __name__ == "__main__":
    pass
