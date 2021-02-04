# -*- coding: utf-8 -*- 
# @Time : 2021/1/23 14:49 
# @Author : dujun
# @describe : 考生进行报考
# @File : test_apply.py 
from pprint import pprint
import pytest
import allure


@allure.feature('考生报考')
class TestApply:
    ##日程数据
    riChengData = {"riChengID": "11110092"}

    @allure.story('考生端操作')
    def test_stuApply(self, stuData, stuRequest, userRequest, riChengData):
        ##考生登录
        for i in range(0, 1):
            ##考生登录
            datas = {
                "loginName": stuData[i],
                "password": "Test1234"
            }
            stuResponse = userRequest.stuLogin(data=datas)
            stuTicket = stuResponse['ticket']

            ##选择指定日程进行报考
            datas = {"m": "", "p": {"riChengID": self.riChengData['riChengID']}}
            payload = {
                "data": str(datas),
                "ticket": stuTicket
            }
            response = stuRequest.save_prof(data=payload)

            ##查询考试列表(baoKaoId)
            datas = {"m": "", "p": {}}
            payload = {
                "data": str(datas),
                "ticket": stuTicket
            }
            response = stuRequest.query_exam_prof(data=payload)
            baoKaoId = response['datas']['list'][0]['baoKaoID']

            ##创建报考订单
            datas = {"m": "", "p": {"xueXiaoID": 6666, "baoKaoIDs": [baoKaoId], "sIds": ""}}
            payload = {
                "data": str(datas),
                "ticket": stuTicket
            }
            response = stuRequest.add_prof_order(data=payload)

            ##根据日程在线确认
            datas = {"m": "", "p": {"baoKaoIDs": [baoKaoId], "xueXiaoID": "6666"}}
            payload = {
                "data": str(datas),
                "ticket": stuTicket
            }
            response = stuRequest.commit_online_confirm(data=payload)
            print(stuData[i], response['message'])
