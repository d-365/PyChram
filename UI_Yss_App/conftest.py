# -*- coding: utf-8 -*-
# @Time : 2021/1/22 22:19
# @Author : dujun
# @describe : pytest用例执行测试初始化工作
# @File :conftest.py
import os
import subprocess

import pytest
from UI_Yss_App.Base.driver_config import DriverClient
from UI_Yss_App.Config.logger import log


@pytest.fixture(scope='session')
def driver():
    drivers = DriverClient().get_driver()
    return drivers

# # 初始化logger
# @pytest.fixture(scope='session')
# def logger():
#     loggers = log()
#     return loggers
