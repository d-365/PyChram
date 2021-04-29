# -*- coding: utf-8 -*- 
# @Time : 2021/3/4 19:55
# @Author : dujun
# @describe : describe

import os
from locust import TaskSet, task, HttpUser


class MyTaskSet(TaskSet):

    def login(self):
        header = {
            "platformType": "2",
            "udid": "1519fbbacd907027e734fbf8b17b2a7a",
            "tkn": "yx001",
            "yks": "1"
        }
        url = 'http://user.51bm.net.cn/login'
        data = {
            "loginName": "yuanxiao",
            "password": 'Test1234',
        }

        re = self.client.post(url=url, headers=header, data=data)
        response = re.json()
        ticket = response['ticket']
        return header, ticket

    @task
    def case1(self):
        result = self.login()
        url = '/auth/school/examschedule/examScheduleData.htm'
        data = {
            'kaoShiID': 13186,
            'zhuanYeID': 1223691,
            'ticket': result[1]
        }
        self.client.headers.update(result[0])
        response = self.client.post(url=url, data=data)
        print(response.json())


class MyLocust(HttpUser):
    tasks = [MyTaskSet]
    host = 'http://school.51bm.net.cn'
    min_wait = 5000
    max_wait = 15000


if __name__ == "__main__":
    # os.system('locust -f locust_fileA.py --headless -u 1 -r 1 -t 3s')
    os.system('locust -f locust_fileA.py')
