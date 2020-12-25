# -*- coding: utf-8 -*- 
# @Time : 2020/12/17 19:40 
# @Author : dujun
# @describe : request 请求方法封装
# @File : Base_Request.py

import requests

class Base_requests:

    def post(self, url=None, headers=None, data=None):
        response = requests.post(url=url, headers=headers, data=data)
        return response.json(), response.text, response.status_code
