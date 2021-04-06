# -*- coding: utf-8 -*- 
# @Time : 2021/1/21 16:51 
# @Author : dujun
# @describe : describe
# @File : audit.py
from UI_Yss_App.interface.Common.Base_Request import Base_requests
from UI_Yss_App.interface.data.caps import Caps


class audit_project:
    re = Base_requests()
    cap = Caps()

    ##客服主管查询考生psid
    def query_psId(self, data=''):
        url = self.cap['audit'] + '/auth/admin/audit/auditListData.htm'
        response = self.re.post(url=url, data=data)
        return response

    ##对考试资料进行审核
    def check_stuInfo(self, data=''):
        url = self.cap['audit'] + '/auth/admin/audit/auditAction.htm'
        response = self.re.post(url=url, data=data)
        return response
