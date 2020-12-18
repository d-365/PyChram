from UI_Yss_Web.Base.Show_Location import BasePage
import pytest
from time import sleep
from selenium import webdriver
import os
from selenium.webdriver.support.select import Select
import random


##定位元素
class Test_register(BasePage):

    # ##register_button 注册按钮
    # @property
    # def register_button(cls):
    #     return cls.By_Text(element='考生注册')
    #
    # ##继续注册按钮J_goon_register
    # @property
    # def J_goon_register(self):
    #     return self.By_ID("J_goon_register")
    #
    # ##同意协议按钮
    # @property
    # def agree_protocol(self):
    #     return self.By_ID('agree_protocol',OverText='没找到同意协议按钮')

    ##点击打开上传窗口
    @property
    def jUploadCard(self):
        return self.By_ID('jUploadCard')

    ##登录密码
    @property
    def yongHuKL(self):
        return self.By_ID('yongHuKL')

    ##确认密码agginYongHuKL
    @property
    def agginYongHuKL(self):
        return self.By_ID('agginYongHuKL')

    ##安全问题下拉框wenTi
    @property
    def wenTi(self):
        return self.By_ID('wenTi')

    ##安全问题答案
    @property
    def daAn(self):
        return self.By_Name("daAn")

    ##输入验证码authCode
    @property
    def authCode(self):
        return self.By_Name('authCode')

    ##jSubmit注册按钮
    @property
    def jSubmit(self):
        return self.By_ID('jSubmit')


##执行测试用例
class TestCase_register:
    ##初始化driver
    driver = webdriver.Chrome()
    page = Test_register(driver)
    random_int = random.randint(0, 6)
    list_answer = ['17637898368', '杜军', '杨勤', '羽毛球和运动', '大海', '周杰伦', '平凡的世界']

    def testcase1(self):
        ## 打开艺术生网站
        self.page.get('http://user.artstudent.cn/')
        ##点击考生注册按钮
        self.page.By_Text('考生注册').click()
        ##点击继续注册
        self.page.By_ID('J_goon_register').click()
        ##同意注册协议
        self.page.By_Xpath('//*[@id="jReadProtocolLabel"]').click()
        ##打开身份证上传弹窗
        self.page.jUploadCard.click()
        os.system(r"D:\pythonProject\UI_Yss_Web\File\upload_file.exe")
        ##输入用户登录密码
        self.page.yongHuKL.send_keys('Test1234')
        ##输入确认用户密码
        self.page.agginYongHuKL.send_keys('Test1234')
        ##选择安全问题Select
        Select(self.page.wenTi).select_by_index(self.random_int)
        ##输入安全问题答案
        self.page.daAn.send_keys(self.list_answer[self.random_int])
        ##输入验证码
        self.page.authCode.send_keys('YxYss')


if __name__ == "__main__":
    run = TestCase_register()
    run.testcase1()
