# -*- coding: utf-8 -*- 
# @Time : 2021/1/22 22:19 
# @Author : dujun
# @describe : describe
# @File : testCreateStu测试固件
from Interface_Yss.project.plat_raw import platRaw
from Interface_Yss.project.user import userProject
from Interface_Yss.project.audit import audit_project
import pytest
from Interface_Yss.data import Account
from Interface_Yss.project.stu import stu_project


##实例stu对象,登录平台管理员账号
@pytest.fixture(scope='module')
def platSetUp():
    platRequest = platRaw()
    ##管理员登录
    datas = Account.manage_Account
    response = platRequest.plat_login(data=datas)
    platTicket = response['ticket']
    return platRequest, platTicket,


##初始化aidit对象
@pytest.fixture(scope='module')
def auditRequest():
    audit = audit_project()
    return audit


##初始化user对象
@pytest.fixture(scope='module')
def userRequest():
    userRequest = userProject()
    return userRequest


##初始化stu对象
@pytest.fixture(scope='module')
def stuRequest():
    stuRequest = stu_project()
    return stuRequest


##考生数据
@pytest.fixture(scope='module')
def stuData():
    stuName = []
    for i in range(0, 1):
        strInt = str(i)
        name = 'xiaoxian' + strInt
        stuName.append(name)
    print("待处理考生数据：", stuName)
    return stuName


##日程数据
@pytest.fixture(scope='module')
def riChengData():
    riChengData = {"riChengID": "11110092"}
    return riChengData
