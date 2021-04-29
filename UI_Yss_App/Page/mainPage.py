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

    # App启动页跳过按钮
    def AppInit_PassBtn(self):
        passBtn = self.By_ID('cn.artstudent.app:id/time')
        passBtn.click()

    # App首页广告推送(img)
    def imgPush(self):
        mainImg_push = self.By_ID('cn.artstudent.app:id/img')
        return mainImg_push

    # 录取概率广告关闭按钮
    def probAlterCancel(self):
        self.tap_relative(883, 792)
