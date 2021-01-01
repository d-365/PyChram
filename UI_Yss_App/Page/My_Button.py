# -*- coding: utf-8 -*- 
# @Time : 2020/12/18 11:06
# @Author : dujun
# @describe : 我的页面
# @File : My_Button.py
from UI_Yss_App.Base.BasePage import Base

class My(Base):

    ##我的按钮
    @property
    def My_button(self):
        return self.By_ID(element='cn.artstudent.app:id/mebtn')

    ## 关闭头像框提示：App生命周期只出现一次
    @property
    def close_MyNotice(self):
        return self.By_ID('cn.artstudent.app:id/text')

    ##头像(没有用户登录)
    @property
    def head_photo(self):
        return self.By_Xpath(element='//*[@text="点击头像登录"]')

    ##登录账号
    @property
    def username(self):
        return self.By_ID(element='cn.artstudent.app:id/name')

    ##登录密码password
    @property
    def password(self):
        return self.By_ID(element='cn.artstudent.app:id/pwd')

    ##登录按钮
    @property
    def loginButton(self):
        return self.By_ID(element='cn.artstudent.app:id/loginBtn')
