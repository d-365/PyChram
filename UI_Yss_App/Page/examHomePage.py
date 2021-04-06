# -*- coding: utf-8 -*- 
# @Time : 2021/2/5 16:29 
# @Author : dujun
# @describe :科目详情——>录制页面
# @File : examHomePage.py

from UI_Yss_App.Base.Base import Base


# 录制页面
class examMainPage(Base):

    # 网络考试按钮
    def WorkExam(self):
        netWorkExam_button = self.By_Xpath('//*[@text="远程提交考试作品"]')
        netWorkExam_button.click()

    ##点击进入正式考试（默认进入第一个）
    def tempOfficialExam_button(self):
        tempOfficialExam_button = self.By_Xpath('//*[@text="正式考试"]')
        tempOfficialExam_button.click()

    ##科目列表中,开始考试按钮（number下标为1）
    def subject(self, number):
        subjectButton = self.By_Xpath(
            '//*[@resource-id="app"]/android.view.View[1]/android.view.View[5]/android.view.View[%d]/android.view.View[6]' % number)
        subjectButton.click()

    ##科目详情页_录制视频按钮
    def recordButton(self):
        record_button = self.By_Xpath("//android.widget.Button[contains(@text,'录制')]")
        record_button.click()

    ##确认录制弹窗_确认按钮
    def recordAlter_affirm(self):
        record_affirm = self.By_Xpath("//android.widget.Button[contains(@text,'确定') ]")
        record_affirm.click()

    ##录制确认弹窗_取消按钮
    def recordAlter_cancel(self):
        record_cancel = self.By_Xpath("//android.widget.Button[contains(@text,'取消') ]")
        record_cancel.click()

    ##录制界面_开始录制按钮
    def record_start(self):
        recordStart = self.By_ID('cn.artstudent.app:id/startRecordBtn')
        recordStart.click()

    ##录制过程中，隐藏考题按钮
    def recording_hiddenQuestions(self):
        recordingHiddenQuestion = self.By_Xpath('//*[@resource-id="cn.artstudent.app:id/showOrHideBtn"]')
        recordingHiddenQuestion.click()

    ##录制过程中,获取文字考题
    def recoding_textQuestion(self):
        testQuestion = self.By_ID('cn.artstudent.app:id/examTextView').get_attribute('text')
        return testQuestion

    ##录制过程中，获取录制界面图片考题number下标为1
    def recoding_photoQuestion(self, number):
        photoQuestion = self.By_ID('cn.artstudent.app:id/examQuestion%dImg' % number)
        return photoQuestion

    ##录制界面_交卷按钮
    def record_end(self):
        recordEnd = self.By_Xpath('//*[@resource-id="cn.artstudent.app:id/doneBtn"]')
        recordEnd.click()

    # 录制过程中，结束录制弹窗_确定
    def endRecord_affirm(self):
        endRecordAffirm = self.By_ID('cn.artstudent.app:id/rightBtn')
        endRecordAffirm.click()

    # 录制过程中，结束录制弹窗_取消
    def endRecord_cancel(self):
        endRecordCancel = self.By_ID('cn.artstudent.app:id/leftBtn')
        endRecordCancel.click()

    # 隐藏候考/准备阶段说明按钮
    def showHideWaitDescBtn(self):
        showWaitDescBtn = self.By_ID('cn.artstudent.app:id/showOrHideWaitDescBtn')
        showWaitDescBtn.click()

    # 候考/准备_阶段说明
    def examTextView(self):
        examText = self.By_ID('cn.artstudent.app:id/examTextView')
        return examText.get_attribute('text')

    # 候考/准备_倒计时
    def alarmTime(self):
        alarm_time = self.By_ID('cn.artstudent.app:id/alarmTime')
        return alarm_time.get_attribute('text')

    # 准备阶段_准备好了按钮
    def ready_Button(self):
        readyButton = self.By_Xpath('//*[@text="准备好了"]')
        readyButton.click()

    # 准备好了弹窗_文本
    def ready_alter(self):
        ready_alter = self.By_ID('cn.artstudent.app:id/content')
        return ready_alter.get_attribute('text')

    # 准备好了弹窗_再等等leftBtn
    def readyAlter_wait(self):
        leftBtn = self.By_ID('cn.artstudent.app:id/leftBtn')
        leftBtn.click()

    # 准备好了弹窗_准备好了rightBtn
    def readyAlter_confirm(self):
        rightBtn = self.By_ID('cn.artstudent.app:id/rightBtn')
        rightBtn.click()


# 科目详情页
class examSubject_info(Base):

    # 科目详情页_手机音量未开启_确定按钮
    def volume_confirmButton(self):
        volumeButton = self.By_Xpath('//*[@text="确定"]')
        volumeButton.click()

    # 科目详情页_手机音量未开启弹窗
    def volume_confirmAlter(self):
        volumeAlter = self.By_Xpath('//*[@text="考试要求手机声音打开，不能处于静音状态，请检查确认!"]')
        return volumeAlter.get_attribute('text')

    # 科目详情页_拍照按钮H5,下标2开始
    def take_picture_H5(self):
        takePicture = self.By_Xpath('//*[@text="点击拍照"]')
        takePicture.click()

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

    # 科目详情页-删除单张已拍照片( 下标从1开始递增1)
    def delete_picture(self, number):
        deletePicture = self.By_Xpath(
            '//*[@resource-id="app"]/android.view.View[1]/android.view.View[1]/android.view.View[3]/android.view.View[2]/android.widget.Image[%d]' % number)
        deletePicture.click()

    ##已经保存的照片，下标从1开始递增1
    def savedPicture(self, number):
        Picture = self.By_Xpath(
            '//*[@resource-id="app"]/android.view.View[1]/android.view.View[1]/android.view.View[2]/android.view.View[%d]' % number)
        return Picture

    ##科目详情页-删除全部已拍照片
    def delete_allPicture(self, number):
        for i in range(1, number + 1):
            deletePicture = self.By_Xpath(
                '//*[@resource-id="app"]/android.view.View[1]/android.view.View[1]/android.view.View[3]/android.view.View[2]/android.widget.Image[%d]' % i)
            deletePicture.click()

    ##科目详情-选中已录视频(下标从 2开始,每次递增2：偶数)、（播放视频下标为3,每次递增2：奇数）
    def checked_video(self, number):
        checkedVideo = self.By_Xpath(
            '//*[@resource-id="app"]/android.view.View[1]/android.view.View[1]/android.view.View[2]/android.view.View[%d]' % number)
        checkedVideo.click()

    # 提交视频按钮
    def submit(self):
        submitVideo = self.By_Xpath("//android.widget.Button[contains(@text,'提交')]")
        submitVideo.click()

    # 提交视频弹窗_确定
    def submitVideo_alter_confirm(self):
        subAlterConfirm = self.By_Xpath('//*[@text="确定"]')
        subAlterConfirm.click()

    # 提交视频弹窗_取消
    def submitVideo_alter_cancel(self):
        subAlterCancel = self.By_Xpath('//*[@text="取消"]')
        subAlterCancel.click()

    # 视频提交弹窗cn.artstudent.app:id/textContent
    def textContentAlter(self):
        """
        提交过程中：视频提交中，请不要离开APP
        提交成功：视频已提交成功
        :return:
        """
        textContent = self.By_ID('cn.artstudent.app:id/textContent')
        return textContent.get_attribute('text')

    # 视频提交成功弹窗_标志cn.artstudent.app:id/progressText
    def progressText(self):
        """
        已完成
        :return:
        """
        progressText = self.By_ID('cn.artstudent.app:id/progressText')
        return progressText.get_attribute('text')

    # 视频提交中弹窗cn.artstudent.app:id/netSpeed
    def netSpeedText(self):
        """
        上传过程中速度
        :return:
        """
        netSpeedText = self.By_ID('cn.artstudent.app:id/netSpeed')
        return netSpeedText.get_attribute('text')

    # 视频提交弹窗_好的按钮cn.artstudent.app:id/btn
    def videoSubmitAlter_Button(self):
        """
        好的
        :return:
        """
        videoAlterButton = self.By_ID('cn.artstudent.app:id/btn')
        videoAlterButton.click()
