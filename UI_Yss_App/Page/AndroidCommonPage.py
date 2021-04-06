# -*- coding: utf-8 -*-
# @Time : 2021/4/1 10:28
# @Author : dujun
# @describe : android通用页面
# @File : AndroidCommonPage.py
import time

from UI_Yss_App.Base.Base import Base


class androidCommon(Base):

    # 原生拍照页面_点击拍照native
    def take_picture_native(self, phoneType):
        tackPicture = self.By_Xpath(
            '//*[@resource-id="com.%s.camera:id/normal_control_bar"]/android.widget.LinearLayout[2]' % phoneType)
        tackPicture.click()

    # 原生拍照页面_返回
    def take_picture_back(self, phoneType):
        backPicture = self.By_ID('com.%s.camera:id/feature_system_back_entrance' % phoneType)
        backPicture.click()

    # 原生拍照界面_保存
    def save_picture(self, phoneType):
        savePicture = self.By_ID('com.%s.camera:id/done_button' % phoneType)
        savePicture.click()

    # 原生拍照界面_取消保存
    def cancel_picture(self, phoneType):
        cancelPicture = self.By_ID('com.%s.camera:id/btn_review_cancel' % phoneType)
        cancelPicture.click()

    # 右上角按钮
    def rightButton(self):
        """
        native 右上角按钮：完成
        :return:
        """
        rightBtn = self.By_Xpath('//*[@resource-id="cn.artstudent.app:id/rightView"]')
        rightBtn.click()

    # android相册选择照片
    def checkPicture(self, number):
        """
        选择单张图片
        :param number: 1 ++
        """
        checkPic = self.By_Xpath(
            '//*[@resource-id="cn.artstudent.app:id/picture_recycler"]/android.widget.RelativeLayout[%d]/android.widget.LinearLayout[1]/android.widget.TextView[1]' % number)
        checkPic.click()

    # Android 相册选择图片：完成
    def checkPic_save(self):
        """
        选择单张图片,进行完成
        """
        checkPicSave = self.By_ID('cn.artstudent.app:id/picture_tv_ok')
        checkPicSave.click()

    # 返回按钮_返回操作
    def btn_back(self, count):
        """
        :param count: 1++
        :return:
        """
        btnBack = self.By_ID('cn.artstudent.app:id/btn_back')
        for i in range(0, count):
            btnBack.click()
            time.sleep(1)
