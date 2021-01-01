# -*- coding: utf-8 -*- 
# @Time : 2020/12/17 19:40 
# @Author : dujun
# @describe : request 请求方法封装
# @File : Base_Request.py

from Interface_Yss.data import CommonData
import requests


class Base_requests:

    ##封装基本request中post方法
    def post(self, url=None, headers="", data=None):
        if headers == "":
            response = requests.post(url=url, headers=CommonData.header, data=data)
            responseCode = {
                "responseCode": response.status_code
            }
            return response.json(), responseCode
        else:
            response = requests.post(url=url, headers=headers, data=data)
            responseCode = {
                "responseCode": response.status_code
            }
            return response.json(), responseCode

    ##封装基本get方法
    def get(self, url=None, headers=None, data=None):
        response = requests.get(url=url, headers=headers, data=data)
        return response.json()
