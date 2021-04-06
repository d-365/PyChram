# -*- coding: utf-8 -*- 
# @Time : 2020/12/18 11:06
# @Author : dujun
# @describe : 我的页面
# @File : My_Button.py
from UI_Yss_App.Base.Base import Base


class myPage(Base):

    # def __init__(self, driver):
    #     self.driver = driver

    ##我的按钮
    @property
    def My_button(self):
        return self.By_ID(element='cn.artstudent.app:id/mebtn')

    ## 关闭头像框提示：App生命周期只出现一次
    @property
    def close_MyNotice(self):
        return self.By_ID('cn.artstudent.app:id/text')

    # 头像(没有用户登录)
    @property
    def head_photo(self):
        return self.By_Xpath(element='//*[@text="点击头像登录"]')

    # 登录账号
    @property
    def username(self):
        return self.By_ID(element='cn.artstudent.app:id/name')

    # 登录输入框
    @property
    def usernameText(self):
        return self.By_Xpath(
            element='//*[@resource-id="cn.artstudent.app:id/name"]//android.widget.FrameLayout//android.widget.EditText')

    # 登录密码password
    @property
    def password(self):
        return self.By_ID(element='cn.artstudent.app:id/pwd')

    # 密码输入框
    @property
    def passwordText(self):
        return self.By_Xpath(
            element='//*[@resource-id="cn.artstudent.app:id/pwd"]//android.widget.FrameLayout//android.widget.EditText')

    # 注册协议按钮
    @property
    def CheckBox(self):
        return self.By_ID(element='cn.artstudent.app:id/checkBox')

    # 登录按钮
    @property
    def loginButton(self):
        return self.By_ID(element='cn.artstudent.app:id/loginBtn')

    # 若重置App,需要调用此方法进行前置动作
    def resetApp(self):
        # 初始化App，点击我知道了, 'noReset'为 True 时忽略
        try:
            Know = self.By_ID('cn.artstudent.app:id/btn')
            Know.click()
            # 点击我的按钮
            self.My_button.click()
            # 关闭头像框提示：App生命周期只出现一次
            self.close_MyNotice.click()
            # 点击头像
            self.head_photo.click()
        except Exception:
            pass
