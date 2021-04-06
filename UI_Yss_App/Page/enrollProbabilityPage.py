# -*- coding: utf-8 -*-
# @Time : 2021/4/6 9:26
# @Author : dujun
# @describe : 录取概率页面
# @File : enrollProbabilityPage.py
from UI_Yss_App.Base.Base import Base


class probPage(Base):

    # 成绩管理
    def modifyInfoButton(self):
        modifyInfo = self.By_Xpath('//*[@resource-id="cn.artstudent.app:id/modifyInfo"]')
        modifyInfo.click()

    # 第一批
    def batch_one(self):
        batchOne = self.By_Xpath('//*[@content-desc="第一批"]')
        batchOne.click()

    # 第二批第一段
    def batch_two1(self):
        batch_two = self.By_Xpath('//*[@text="第二批第一段"]')
        batch_two.click()

    # 第二批第二段
    def batch_two2(self):
        batch_two = self.By_Xpath('//*[@text="第二批第二段"]')
        batch_two.click()

    # 冲刺院校
    def sprintProfessional(self):
        sprint = self.By_Xpath('//*[@resource-id="cn.artstudent.app:id/sprintLayout"]')
        sprint.click()

    # 稳妥专业
    def safeProfessional(self):
        safe = self.By_Xpath('//*[@resource-id="cn.artstudent.app:id/safeLayout"]')
        safe.click()

    # 保底专业
    def mustProfessional(self):
        must = self.By_Xpath('//*[@resource-id="cn.artstudent.app:id/paulendLayout"]')
        must.click()

    # 我的志愿表
    def myVoluntary(self):
        Voluntary = self.By_Xpath('//*[@resource-id="cn.artstudent.app:id/myWishListLayoutItem1"]')
        Voluntary.click()

    # 我的志愿表
    def IntelligentRecommend(self):
        Intelligent = self.By_Xpath('//*[@resource-id="cn.artstudent.app:id/myWishListLayoutItem1"]')
        Intelligent.click()

    # 省份政策
    def provincePolicy(self):
        province = self.By_Xpath('//*[@resource-id="cn.artstudent.app:id/myWishListLayoutItem3"]')
        province.click()

    # 志愿填报工具
    def volunteer_tools(self, number):
        """
        :param number: 1:操作说明 2：热门院校 3：历年分数 4：综合分计算 5：性格测试 6：常见问题
        """
        operation = self.By_Xpath(
            '//*[@resource-id="cn.artstudent.app:id/toolsRecyclerView"]/android.widget.LinearLayout[%d]' % number)
        operation.click()
