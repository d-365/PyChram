# -*- coding: utf-8 -*- 
# @Time : 2021/1/22 22:19 
# @Author : dujun
# @describe : describe
# @File : testCreateStu测试固件
import os

from Interface_Yss.project.plat_raw import platRaw
from Interface_Yss.project.user import userProject
from Interface_Yss.project.audit import audit_project
import pytest
from Interface_Yss.data import Account
from Interface_Yss.project.stu import stu_project


# 设置命令行参数
def pytest_addoption(parser):
    parser.addoption(
        "--env", action="store", default="", help="my option: '' or online"
    )


# 添加命令行参数
@pytest.fixture(scope='session')
def cmdOption(request):
    return request.config.getoption("--env")


# 实例stu对象,登录平台管理员账号
@pytest.fixture(scope='session')
def platSetUp(cmdOption):
    platRequest = platRaw(environment=cmdOption)
    # 管理员登录
    datas = Account.manage_Account
    response = platRequest.plat_login(data=datas)
    platTicket = response['ticket']
    return platRequest, platTicket,


# 初始化aidit对象
@pytest.fixture(scope='session')
def auditRequest(cmdOption):
    audit = audit_project(environment=cmdOption)
    return audit


# 初始化user对象
@pytest.fixture(scope='session')
def userRequest(cmdOption):
    userRequest = userProject(environment=cmdOption)
    return userRequest


# 初始化stu对象
@pytest.fixture(scope='session')
def stuRequest(cmdOption):
    stuRequest = stu_project(environment=cmdOption)
    print('cmdoption', cmdOption)
    return stuRequest


# 考生数据
@pytest.fixture(scope='module')
def stuData():
    stuName = []
    for i in range(0, 20):
        strInt = str(i)
        name = 'bei' + strInt
        stuName.append(name)
    print("待处理考生数据：", stuName)
    return stuName


# 日程数据
@pytest.fixture(scope='module')
def riChengData():
    riChengData = {"riChengID": "11110092"}
    return riChengData

# @pytest.fixture(scope="session", autouse=True)
# def host(request):
#     """获取命令行参数"""
#     # 获取命令行参数给到环境变量
#     os.environ["host"] = request.config.getoption("--env")
#     print("当前用例运行测试环境:%s" % os.environ["host"])
