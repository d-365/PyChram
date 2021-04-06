# -*- coding: utf-8 -*- 
# @Time : 2021/2/26 11:32 
# @Author : dujun
# @describe : describe
# @File : school.py
from UI_Yss_App.interface.Common.Base_Request import Base_requests
from UI_Yss_App.interface.data.caps import Caps


class school_project:
    def __init__(self, environment):
        self.re = Base_requests()
        self.caps = Caps(env=environment)

    ##视频打回,输入当前账号密码
    def pwdAuth(self, data):
        """
        :param data:
            authCode:账户密码;
            optRemark：备注
        """
        url = self.caps['school'] + '/auth/school/examstatistic/pwdAuth.htm'
        response = self.re.post(url=url, data=data)
        return response

    ##视频打回
    def resetVideo(self, data):
        """
        :param data:
            svId:考生科目视频唯一标记
            token：院校账户token
            optRemark:备注
        :return:
        """
        url = self.caps['school'] + '/auth/school/examstatistic/resetVideo.htm'
        response = self.re.post(url=url, data=data)
        return response
