# -*- coding: utf-8 -*-
# @Time : 2021/3/29 10:00
# @Author : dujun
# @describe : 专业评画
# @File : production_appraisePage.py

from UI_Yss_App.Base.Base import Base


class stuProduction_appraise_webView(Base):
    """
    考生端上传评画作品：WebView页面
    """

    # 改画按钮,顶部banner
    def drawPicture_location(self):
        """
        改画老师页面顶部banner图
        :return:
        """
        super().tap_relative(400, 400)

    # 帮我改画按钮 895,1912
    def drawPicBtn_webView(self):
        appraise_button = self.By_Xpath('//*[@id="app"]/div/div/div[2]')
        appraise_button.click()

    # 选择改画老师
    def choseTeacher_webView(self, index):
        """
        改画老师页面:选择改画老师
        index ：1 ++
        :return:
        """
        choseTeacher = self.By_Xpath('//*[contains(@id,"inner-")]/div[2]/div[%d]/div[2]/div[2]/div[2]/button' % index)
        choseTeacher.click()

    # 求改画文本输入框_输入
    def InputTextarea_webView(self, text):
        textarea = self.By_Xpath('//*[@id="app"]/div/div/div/div/div[2]/div[1]/textarea')
        textarea.click()
        textarea.send_keys(text)

    # 求改画文本输入框
    def textarea_webView(self):
        textarea = self.By_Xpath('//*[@id="app"]/div/div/div/div/div[2]/div[1]/textarea')
        return textarea

    # 求改画：上传作品按钮
    def photoCore_webView(self):
        photoCore = self.By_Xpath('//*[@id="app"]/div/div/div/div/div[2]/div[2]/div/img')
        photoCore.click()

    # 求改画：选择专业按钮
    def choseSubjectBtn_webView(self):
        """
        默认选中第二个元素
        :return:
        """
        choseSub = self.By_Xpath('//*[@id="app"]/div/div/div/div/div[2]/div[4]/div[1]/div[2]/div')
        choseSub.click()

    # 选择专业
    def choseSubjectList_webView(self, index):
        """
        :param index: 下标 1 ++
        :return:
        """
        choseSubjectList = self.By_Xpath(
            '//*[@id="app"]/div/div/div/div/div[2]/div[7]/div[2]/div[2]/div[1]/div/div[%d]' % index)
        choseSubjectList.click()

    # 求改画：选择专业 取消
    def choseSub_cancelWebView(self):
        choseSub_cancel = self.By_Xpath('//*[@id="app"]/div/div/div/div/div[2]/div[7]/div[1]/span[1]')
        choseSub_cancel.click()

    # 求改画：选择专业 确认
    def choseSub_confirmWebView(self):
        choseSub_confirm = self.By_Xpath('//*[@id="app"]/div/div/div/div/div[2]/div[7]/div[1]/span[2]')
        choseSub_confirm.click()

    # 选择年级按钮
    def chose_gradeBtn_WebView(self):
        """
        默认选中第一个元素
        :return:
        """
        chose_gradeBtn = self.By_Xpath('//*[@id="app"]/div/div/div/div/div[2]/div[4]/div[2]/div[2]/div')
        chose_gradeBtn.click()

    # 选择年级元素
    def chose_gradeList_WebView(self, index):
        """
        :param index: 1 ++
        :return:
        """
        chose_gradeList = self.By_Xpath(
            '//*[@id="app"]/div/div/div/div/div[2]/div[6]/div[2]/div[2]/div[1]/div/div[%d]' % index)
        chose_gradeList.click()

    # 选择年级：取消
    def chose_gradeClose_WebView(self):
        chose_gradeClose = self.By_Xpath('//*[@id="app"]/div/div/div/div/div[2]/div[6]/div[1]/span[1]')
        chose_gradeClose.click()

    # 选择年级：确认
    def chose_gradeConfirm_WebView(self):
        chose_gradeConfirm = self.By_Xpath('//*[@id="app"]/div/div/div/div/div[2]/div[6]/div[1]/span[2]')
        chose_gradeConfirm.click()

    # 求改画页面,点击批改老师
    def switch_teacher_webView(self):
        switchTeacher = self.By_Xpath('//*[@id="app"]/div/div/div/div/div[2]/div[4]/div[3]/div[2]/div')
        switchTeacher.click()

    # 求改画页面,点击批改老师弹窗_取消
    def switchTeacher_cancel(self):
        switchTeacherCel = self.By_Xpath('//*[@text="取消"]')
        switchTeacherCel.click()

    # 求改画页面,点击批改老师弹窗_确认
    def switchTeacher_confirm(self):
        switchTeacherCfm = self.By_Xpath('//*[@text="确定"]')
        switchTeacherCfm.click()

    # 提交按钮
    def submit_webView(self):
        submitButton = self.By_Xpath('//*[@id="app"]/div/div/div/div/div[2]/div[5]/button')
        submitButton.click()


class stuProduction_appraise_native(Base):
    """
    考生端上传评画作品：NATIVE页面
    """

    # 求改画：选择上传方式拍照
    def take_Picture(self):
        """
        改画作品上传方式：拍照
        :return:
        """
        takePicture = self.By_Xpath('//*[@text="拍照"]')
        takePicture.click()

    # 求改画：选择上传方式拍照
    def photo_album(self):
        """
        改画作品上传方式：相册
        :return:
        """
        photoAlbum = self.By_Xpath('//*[@text="相册"]')
        photoAlbum.click()

    # 选择上传方式:取消
    def choseUploadPhoto_cancel(self):
        UploadPhoto_cancel = self.By_Xpath('//*[@resource-id="cn.artstudent.app:id/ok"]')
        UploadPhoto_cancel.click()

    # 旋转按钮
    def rotateButton(self, count):
        """
        :param count: 旋转次数 1
        :return:
        """
        rotateBtn = self.By_ID('cn.artstudent.app:id/rotateBtn')
        for i in range(0, count):
            rotateBtn.click()

    # 删除已上传图片
    def deleteUpload_picture(self):
        """
        :return:
        """
        super().tap_relative(265, 700)

    # 支付详情_立即支付
    def payBtn(self):
        super().tap_relative(650, 2135)

    # 支付界面,确认支付
    def payConfirm(self):
        payConfirmBtn = self.By_Xpath('//*[@resource-id="cn.artstudent.app:id/submitBtn"]')
        payConfirmBtn.click()

    # 支付弹窗,取消
    def alter_cancel(self):
        alterCancel = self.By_Xpath('//*[@resource-id="android:id/button2"]')
        alterCancel.click()
