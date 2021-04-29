# -*- coding: utf-8 -*- 
# @Time : 2021/1/19 10:49 
# @Author : dujun
# @describe : describe
# @File : user.py 
from Interface_Yss.Common.Base_Request import Base_requests
from Interface_Yss.data.caps import Caps


class userProject:

    def __init__(self, environment):
        self.re = Base_requests()
        self.caps = Caps(env=environment)

    # 登录接口App登录
    def stuLogin(self, data=''):
        url = self.caps['user'] + "/login"
        response = self.re.post(url=url, data=data)
        return response

    # 提交考生个人信息
    def save_stuinfo(self, data=''):
        url = self.caps['user'] + '/api/m/auth/user/save_stuinfo.htm'
        response = self.re.post(url=url, data=data)
        return response

    # 上传报考资料
    def uploadStuPhoto(self, data=''):
        url = self.caps['23000'] + "/api/m/auth/service/v191119/upload_auth_res.ws"
        headers = {
            "platformType": "2",
            "udid": "1519fbbacd907027e734fbf8b17b2a7a",
            "tkn": "yx001",
            "yks": "1"
        }
        response = self.re.post(url=url, headers=headers, data=data)
        return response

    # 提交报考资料
    def submitStuInfo(self, data=''):
        url = self.caps['23000'] + "/api/m/auth/service/v191119/commit_auth_res.ws"
        response = self.re.post(url=url, data=data)
        return response