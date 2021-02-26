# coding=utf-8
# @Time : 2021/2/9 10:22 
# @Author : dujun
# @describe : 视频录制——>上传
# @File : test_exam.py 

import datetime
import time
import allure
import pytest
import os
from UI_Yss_App.TestCase.interface_UI.exam_VideoBack import videoBack


@allure.feature('网络考试页面用例')
class TestRegister:

    def setup_class(self):
        self.startTime = datetime.datetime.now()
        os.popen('adb shell rm -rf /sdcard/yks')
        ##打回对应视频
        videoBack().videoBack()
        print('-------------------------网络考试用例开始执行', self.startTime, '----------------------------')

    def teardown_class(self):
        endTime = datetime.datetime.now()
        print('----------------------------网络考试用例执行完毕,用例耗时', endTime - self.startTime, '----------------------------')

    @allure.story('进入科目详情页')
    def test_intoSubjectInfo(self, mainView, examMain):
        mainView.register()
        examMain.WorkExam()
        ##点击进入对应专业科目列表,默认进入第一个
        examMain.tempOfficialExam_button()
        ##进入对应科目详情页(下标为1)
        examMain.subject(1)
        time.sleep(2)

    @allure.story('进入录制_开始录制')
    # @pytest.mark.skipif(1 == 1, reason='不进行录制')
    @pytest.mark.repeat(2, scope='function')
    def test_StuRegister(self, mainView, logger, examMain):
        try:
            with allure.step('点击录制按钮，进入录制画面'):
                examMain.swipe_up()
                examMain.recordButton()
                examMain.recordAlter_affirm()
                ##开始录制
                time.sleep(6)
                examMain.record_start()
                ##播放语音指令时间（5）
                time.sleep(5)
                question_text = examMain.recoding_textQuestion()
                raw_questionText = '这是视频录制类配置的试题详情'
                assert question_text == raw_questionText
                ##录制时长
                time.sleep(15)
                ##结束录制
                examMain.record_end()
                examMain.endRecord_affirm()
                time.sleep(1)
        except Exception:
            examMain.screenCap('test_StuRegister')
            logger.info('网络考试录制用例failed')

    @allure.story('科目详情页_拍照上传')
    @allure.step('未拍照，未选视频进行提交')
    # @pytest.mark.skipif(1 == 1, reason='不执行')
    def test_pictureUpload_case1(self, subjectInfo, logger):
        rawToast = '请选择您要提交的视频'
        subjectInfo.submit()
        toast = subjectInfo.catch_toast(rawMessage=rawToast)
        assert toast.text == rawToast
        logger.info('上传case1执行成功,未拍照，未选视频进行提交')

    @allure.story('科目详情页_拍照上传')
    @allure.step('仅拍照片进行提交')
    # @pytest.mark.skipif(1 == 1, reason='不执行')
    def test_pictureUpload_case2(self, subjectInfo, logger):
        try:
            subjectInfo.swipe_up()
            subjectInfo.swipe_up()
            subjectInfo.delete_allPicture(1)
        except:
            pass
        ##H5调用，进行拍照
        subjectInfo.take_picture_H5()
        subjectInfo.take_picture_native('huawei')
        subjectInfo.save_picture('huawei')
        ##进行提交操作
        subjectInfo.submit()
        rawToast = '请选择您要提交的视频'
        toast = subjectInfo.catch_toast(rawMessage=rawToast)
        assert rawToast == toast.text
        ##删除已保存照片
        subjectInfo.delete_allPicture(1)
        time.sleep(1)
        logger.info('上传case2执行成功，仅拍照片进行提交')

    @allure.story('科目详情页_拍照上传')
    @allure.step('仅选中视频进行提交')
    # @pytest.mark.skipif(1 == 1, reason='不执行')
    def test_pictureUpload_case3(self, subjectInfo, logger):
        rawToast = '请上传考试图片'
        try:
            ##删除已保存照片
            subjectInfo.swipe_up()
            subjectInfo.swipe_up()
            subjectInfo.delete_allPicture(1)
        except:
            pass
        # 选中第一个视频进行提交
        subjectInfo.checked_video(2)
        subjectInfo.submit()
        toast = subjectInfo.catch_toast(rawMessage=rawToast)
        assert toast.text == rawToast
        logger.info('上传case3执行成功，仅选中视频进行提交')

    @allure.story('视频提交测试用例')
    @allure.step('选中任意视频，拍照进行上传')
    # @pytest.mark.skipif(1 == 1, reason='跳过')
    def test_pictureUpload_case4(self, subjectInfo, logger):
        try:
            ##删除已保存照片
            subjectInfo.swipe_up()
            subjectInfo.swipe_up()
            subjectInfo.delete_allPicture(1)
            ##视频列表
            # videoList = subjectInfo.By_Xpath('//*[@resource-id="app"]/android.view.View[1]/android.view.View[1]/android.view.View[2]/android.view.View[2]')
        except:
            pass
        # 拍照
        subjectInfo.take_picture_H5()
        subjectInfo.take_picture_native(phoneType='huawei')
        subjectInfo.save_picture(phoneType='huawei')

        ##选中视频
        subjectInfo.checked_video(2)
        ##提交
        subjectInfo.submit()
        subjectInfo.submitVideo_alter_confirm()
        logger.info('视频提交成功')
        time.sleep(5)
