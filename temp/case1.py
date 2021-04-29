# -*- coding: utf-8 -*-
# @Time : 2021/4/13 17:01
# @Author : dujun
# @describe : describe
# @File : case1.py
import pytest
from Interface_Yss.project.user import userProject


@pytest.mark.parametrize("loginName,password", [('xiaojun0', 'Test1234'), ('xiaojun1', 'Test1234')])
def test_login(loginName, password):
    user = userProject(environment='')
    data = {
        'loginName': loginName,
        'password': password
    }
    re = user.stuLogin(data=data)
    print(re)
