# -*- coding: utf-8 -*- 
# @Time : 2021/2/9 11:59 
# @Author : dujun
# @describe : App首页
# @File : mainPage.py

from UI_Yss_App.Base.Base import Base


class mainPage(Base):

    # 报考按钮
    def register(self):
        register = self.By_ID('cn.artstudent.app:id/bkbtn')
        register.click()
