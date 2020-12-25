# -*- coding: utf-8 -*- 
# @Time : 2020/12/17 19:40 
# @Author : dujun
# @describe : describe
# @File : Base_Request.py 

import requests

class Base_requests:

    def Post(self,url=None,headers=None,data=None):
        response = requests.post(url,headers,data)
        return response.json()

