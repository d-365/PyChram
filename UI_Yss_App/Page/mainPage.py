# -*- coding: utf-8 -*- 
# @Time : 2021/2/9 11:59 
# @Author : dujun
# @describe : App首页
# @File : mainPage.py

from UI_Yss_App.Base.Base import Base


class mainPage(Base):

    # 报考按钮_点击报考
    def register(self):
        register = self.By_ID('cn.artstudent.app:id/bkbtn')
        register.click()

    # 返回按钮_返回操作
    def btn_back(self, count):
        btnBack = self.By_ID('cn.artstudent.app:id/btn_back')
        for i in range(0, count):
            btnBack.click()

    # 首页
    def homeButton(self):
        home_button = self.By_ID('cn.artstudent.app:id/homebtn')
        home_button.click()

    # 院校
    def colleges_Button(self):
        collegesBtn = self.By_ID('cn.artstudent.app:id/collegesbtn')
        collegesBtn.click()

    # 圈子
    def groups_Button(self):
        groupsBtn = self.By_ID('cn.artstudent.app:id/groupsBtn')
        groupsBtn.click()

    # 专业评测
    def production_appraiseButton(self):
        production_appraise = self.By_Xpath('//android.widget.TextView[@text="专业评画"]')
        production_appraise.click()

    # 录取概率
    def probButton(self):
        prob = self.By_Xpath('//*[@text="录取概率"]')
        prob.click()
