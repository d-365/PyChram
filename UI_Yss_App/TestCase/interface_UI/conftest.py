# # -*- coding: utf-8 -*-
# # @Time : 2021/2/26 15:04
# # @Author : dujun
# # @describe : describe
# # @File : conftest.py
#
# import pytest
# from Interface_Yss.project.college import college_project
# from Interface_Yss.project.school import school_project
# from Interface_Yss.project.examVideo import examVideo_project
#
# #用例执行环境
# env_execute = "online"
# @pytest.fixture(scope='session')
# def college():
#     college = college_project(environment=env_execute)
#     return college
#
# @pytest.fixture(scope='session')
# def school():
#     school = school_project(environment=env_execute)
#     return school
#
# @pytest.fixture(scope='session')
# def examVideo():
#     examVideo = examVideo_project(environment=env_execute)
#     return examVideo
