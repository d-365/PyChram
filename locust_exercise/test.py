# -*- coding: utf-8 -*- 
# @Time : 2021/3/6 16:06 
# @Author : dujun
# @describe : describe
# @File : test.py 

import requests
import json
import hashlib


def query(self):
    url = 'http://user.51bm.net.cn/auth/admin/suppassword/supPasswordListData.htm'

    queryStu_data = {
        "pageSize": 15,
        "curPage": 1,
        "ticket": self.ticket
    }
    response = requests.post(url=url, headers=self.header, data=queryStu_data, cookies=self.cookie)


class r:
    header = {
        "platformType": "2",
        "udid": "1519fbbacd907027e734fbf8b17b2a7a",
        "tkn": "yx001",
        "yks": "1"
    }

    def login(self):
        url = 'http://user.51bm.net.cn/login'
        data = {
            "loginName": "haitun",
            "password": 'Test1234',
        }
        session = requests.session()
        response = session.post(url=url, headers=self.header, data=data)
        print(response.json())
        cookie = response.cookies
        a = cookie.get_dict()
        print(a)


if __name__ == "__main__":
    run = r()
    run.login()
    # run.query()
