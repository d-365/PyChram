# -*- coding: utf-8 -*- 
# @Time : 2021/3/4 19:55
# @Author : dujun
# @describe : describe

import os
from locust import HttpUser, TaskSet, task


class test_score(TaskSet):
    # def on_start(self):
    #     print('开始执行用例啦')

    header = {
        "platformType": "2",
        "udid": "1519fbbacd907027e734fbf8b17b2a7a",
        "tkn": "yx001",
        "yks": "1"
    }

    @task(1)
    def login(self):
        url = '/login'
        data = {
            "loginName": "yuanxiao",
            "password": 'Test1234',
        }

        response = self.client.post(url=url, headers=self.header, data=data)
        self.ticket = response.json()['ticket']
        try:
            assert response.status_code == 200
        except Exception:
            print(response.text)

    @task
    def queryStu(self):
        url = '/auth/admin/user/userList.htm'
        queryStu_data = {
            "ticket": self.ticket,
            "useFlag": 1
        }
        response = self.client(url=url, headers=self.header, data=queryStu_data)
        print(response.json())


class User(HttpUser):
    host = 'http://user.51bm.net.cn'
    tasks = [test_score]


if __name__ == "__main__":
    os.system('locust -f locust_fileA.py --headless -u 10 -r 10 -t 3s')
