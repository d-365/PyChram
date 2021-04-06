# -*- coding: utf-8 -*- 
# @Time : 2021/3/4 15:52
# @Author : dujun
# @describe : 支付接口
# @File : eval.py
from UI_Yss_App.interface.Common.Base_Request import Base_requests
from UI_Yss_App.interface.data.caps import Caps


class pay_project:

    def __init__(self, environment):
        self.re = Base_requests()
        self.caps = Caps(env=environment)

    ##提交支付
    def pay(self, orderId):
        url = self.caps['pay'] + '/pay/alipay/testnotify.htm?orderId= %d' % orderId
        response = self.re.get(url=url)
        return response
