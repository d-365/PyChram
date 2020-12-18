# -*- coding: utf-8 -*- 
# @Time : 2020/12/10 14:50 
# @Author : dujun
# @describe : 模拟考生报名
# @File : Test_StuApply.py

import requests
import pytest


class Teststu_Apply:
    header = {
        "platformType": "2",
        "udid": "1519fbbacd907027e734fbf8b17b2a7a",
        "tkn": "yx001",
        "yks": "1",
    }

    def Before(self, name):
        self.list_UserName = []
        for i in range(1, 10):
            strInt = str(i)
            # strIntAuto = strInt.zfill(2)
            nameInt = str(strInt)
            names = name + nameInt
            self.list_UserName.append(names)
        return self.list_UserName

    ##登录
    def Login(self, i):
        LoginUrl = 'http://user.51bm.net.cn/login'
        stu_Password = 'Csk001'
        datas = {
            "loginName": self.list_UserName[i],
            "password": stu_Password
        }
        response = requests.post(url=LoginUrl, headers=self.header, data=datas)
        self.ticket = response.json()['ticket']
        print(response.json())
        return self.ticket

    ##选择专业
    def Choose(self):
        Choose_Url = 'http://stu.51bm.net.cn/api/m/auth/apply/save_prof.htm'
        data = {"m": "", "p": {"riChengID": "11108254"}}
        datas = {
            "ticket": self.ticket,
            "data": str(data)
        }
        requests.post(url=Choose_Url, headers=self.header, data=datas)

    ##报考信息
    def BaokaoMessage(self):
        BaokaoMessage_Url = 'http://stu.51bm.net.cn/api/m/auth/apply/query_prof.htm'
        data = {"m": "", "p": {"xueXiaoID": 6666, "baoKaoBZList": [1, 2, 3]}}
        datas = {
            "data": str(data),
            "ticket": self.ticket
        }
        response = requests.post(url=BaokaoMessage_Url, headers=self.header, data=datas)
        self.BaokaoId = response.json()["datas"]["list"][0]["baoKaoID"]
        return self.BaokaoId

    ##创建订单
    def Order(self):
        Order_Url = 'http://stu.51bm.net.cn/api/m/auth/apply/add_prof_order.htm'
        data = {"m": "", "p": {"xueXiaoID": 6666, "baoKaoIDs": [self.BaokaoId], "sIds": ""}}
        datas = {
            "ticket": self.ticket,
            "data": str(data)
        }
        response = requests.post(url=Order_Url, headers=self.header, data=datas)

    ##在线确认
    def Confirm(self):
        Confirm_Url = 'http://print.51bm.net.cn/api/m/auth/apply/commit_online_confirm.htm'
        data = {"m": "", "p": {"baoKaoIDs": [self.BaokaoId], "xueXiaoID": "6666"}}
        datas = {
            'ticket': self.ticket,
            'data': str(data)
        }
        requests.post(url=Confirm_Url, headers=self.header, data=datas)


if __name__ == "__main__":
    run = Teststu_Apply()
    run.Before("haibei")
    for i in range(0, 9):
        run.Login(i)
        run.Choose()
        run.BaokaoMessage()
        run.Order()
