# -*- coding: utf-8 -*-
# @Time : 2021/3/29 9:59
# @Author : dujun
# @describe : 专业评画测试用例
# @File : test_production_appraise.py
import time
import allure
import pytest


@allure.feature('专业评画：考生上传待评作品')
class TeststuUpload_production:

    def setup_class(self):
        pass

    def teardown_class(self):
        pass

    @pytest.mark.runTest
    def test_pre(self, stuAppraiseWebView, mainView):
        """
        评画考生端前置动作：选择评画老师进入求改画页面
        :param stuAppraiseWebView:
        :param mainView:
        """
        try:
            time.sleep(4)
            mainView.probAlterCancel()
        except:
            pass
        mainView.production_appraiseButton()
        # 专业评测页面
        AppraiseContexts = mainView.driver.contexts
        mainView.switch_h5(AppraiseContexts[1])
        stuAppraiseWebView.drawPicBtn_webView()
        stuAppraiseWebView.choseTeacher_webView(1)

    @allure.story('直接进入提交')
    def test_case1(self, stuAppraiseWebView):
        """
        直接进入提交
        """
        rawToast = '请输入作品描述'
        stuAppraiseWebView.submit_webView()
        toast = stuAppraiseWebView.catch_toast(rawToast)
        stuAppraiseWebView.assertIn(rawToast, toast)
        time.sleep(2)

    @allure.story('仅输入描述提交')
    def test_case2(self, stuAppraiseWebView, faker):
        rawToast = '请上传作品'
        inputTexts = faker.paragraph()
        textarea = stuAppraiseWebView.textarea_webView()
        stuAppraiseWebView.InputTextarea_webView(inputTexts)
        stuAppraiseWebView.submit_webView()
        textarea.click()
        textarea.send_keys('delete')
        textareaValue = textarea.get_attribute('value')
        lens = len(textareaValue)
        stuAppraiseWebView.androidKey_Del(lens)
        time.sleep(1)

    @allure.story('仅上传作品进行提交:拍照上传')
    def test_case3(self, stuAppraiseWebView, stuAppraiseNative, androidCommonView):
        rawToast = '请输入作品描述'
        textarea = stuAppraiseWebView.textarea_webView()
        time.sleep(1)
        textarea.clear()
        stuAppraiseWebView.photoCore_webView()
        appraiseContext = stuAppraiseNative.driver.contexts
        # 切换原生native
        stuAppraiseNative.switch_native(appraiseContext[0])
        stuAppraiseNative.take_Picture()
        androidCommonView.take_picture_native('huawei')
        androidCommonView.save_picture('huawei')
        stuAppraiseNative.rotateButton(1)
        androidCommonView.rightButton()
        # 切换webView
        stuAppraiseNative.switch_h5(appraiseContext[1])
        stuAppraiseWebView.submit_webView()
        stuAppraiseNative.deleteUpload_picture()
        toast = stuAppraiseWebView.catch_toast(rawToast)
        stuAppraiseWebView.assertIn(rawToast, toast)
        time.sleep(2)

    @allure.story('仅上传作品进行提交:相册选择')
    def test_case4(self, stuAppraiseWebView, stuAppraiseNative, androidCommonView):
        rawToast = '请输入作品描述'
        textarea = stuAppraiseWebView.textarea_webView()
        textarea.clear()
        stuAppraiseWebView.photoCore_webView()
        appraiseContext = stuAppraiseNative.driver.contexts
        # 切换原生native
        stuAppraiseNative.switch_native(appraiseContext[0])
        stuAppraiseNative.photo_album()
        androidCommonView.checkPicture(1)
        androidCommonView.checkPic_save()
        stuAppraiseNative.rotateButton(1)
        androidCommonView.rightButton()
        # 切换webView
        stuAppraiseNative.switch_h5(appraiseContext[1])
        stuAppraiseWebView.submit_webView()
        stuAppraiseNative.deleteUpload_picture()
        toast = stuAppraiseWebView.catch_toast(rawToast)
        stuAppraiseWebView.assertIn(rawToast, toast)
        time.sleep(2)

    @allure.story('输入描述上传作品,进行提交')
    def test_case4(self, stuAppraiseWebView, stuAppraiseNative, androidCommonView, faker):
        rawToast = '请选择专业'
        inputTexts = faker.paragraph()
        stuAppraiseWebView.InputTextarea_webView(inputTexts)
        stuAppraiseWebView.photoCore_webView()
        appraiseContext = stuAppraiseNative.driver.contexts
        # 切换原生native
        stuAppraiseNative.switch_native(appraiseContext[0])
        stuAppraiseNative.photo_album()
        androidCommonView.checkPicture(1)
        androidCommonView.checkPic_save()
        stuAppraiseNative.rotateButton(1)
        androidCommonView.rightButton()
        # 切换webView
        stuAppraiseNative.switch_h5(appraiseContext[1])
        stuAppraiseWebView.submit_webView()

        stuAppraiseNative.deleteUpload_picture()
        toast = stuAppraiseWebView.catch_toast(rawToast)
        stuAppraiseWebView.assertIn(rawToast, toast)
        time.sleep(2)

    @allure.story('不选择专业提交')
    def test_case5(self, stuAppraiseWebView, stuAppraiseNative, androidCommonView, faker):
        rawToast = '请选择专业'
        inputTexts = faker.paragraph()
        stuAppraiseWebView.InputTextarea_webView(inputTexts)
        stuAppraiseWebView.photoCore_webView()
        appraiseContext = stuAppraiseNative.driver.contexts
        # 选择年级
        stuAppraiseWebView.chose_gradeBtn_WebView()
        stuAppraiseWebView.chose_gradeList_WebView(1)
        stuAppraiseWebView.chose_gradeConfirm_WebView()
        # 切换原生native
        stuAppraiseNative.switch_native(appraiseContext[0])
        stuAppraiseNative.photo_album()
        androidCommonView.checkPicture(1)
        androidCommonView.checkPic_save()
        stuAppraiseNative.rotateButton(1)
        androidCommonView.rightButton()
        # 切换webView
        stuAppraiseNative.switch_h5(appraiseContext[1])
        stuAppraiseWebView.submit_webView()

        stuAppraiseNative.deleteUpload_picture()
        toast = stuAppraiseWebView.catch_toast(rawToast)
        stuAppraiseWebView.assertIn(rawToast, toast)
        time.sleep(2)

    @allure.story('输入全部信息进行提交:不切换老师')
    @pytest.mark.runTest
    def test_case6(self, stuAppraiseWebView, stuAppraiseNative, androidCommonView, faker):
        """
        手机未安装支付宝,跳转H5页面进行支付
        :param stuAppraiseWebView:
        :param stuAppraiseNative:
        :param androidCommonView:
        :param faker:
        """
        inputTexts = faker.paragraph()
        stuAppraiseWebView.InputTextarea_webView(inputTexts)
        # 选择年级
        stuAppraiseWebView.chose_gradeBtn_WebView()
        stuAppraiseWebView.chose_gradeList_WebView(1)
        stuAppraiseWebView.chose_gradeConfirm_WebView()
        # 选择专业
        stuAppraiseWebView.choseSubjectBtn_webView()
        stuAppraiseWebView.choseSubjectList_webView(1)
        stuAppraiseWebView.choseSub_confirmWebView()
        # 切换原生native
        stuAppraiseWebView.photoCore_webView()
        appraiseContext = stuAppraiseNative.driver.contexts
        stuAppraiseNative.switch_native(appraiseContext[0])
        stuAppraiseNative.photo_album()
        androidCommonView.checkPicture(1)
        androidCommonView.checkPic_save()
        stuAppraiseNative.rotateButton(1)
        androidCommonView.rightButton()
        # 切换webView
        stuAppraiseNative.switch_h5(appraiseContext[1])
        stuAppraiseWebView.submit_webView()

        while stuAppraiseNative.driver.title == '求改画':
            time.sleep(1)

        # 切换native支付
        stuAppraiseNative.switch_native(appraiseContext[0])
        stuAppraiseNative.payBtn()
        stuAppraiseNative.payConfirm()
        stuAppraiseNative.alter_cancel()
        androidCommonView.btn_back(1)
        androidCommonView.btn_back(1)
        time.sleep(2)

    @allure.story('输入全部信息进行提交:切换老师提交')
    @pytest.mark.runTest
    def test_case7(self, stuAppraiseWebView, stuAppraiseNative, androidCommonView, faker):
        """
        手机未安装支付宝,跳转H5页面进行支付
        :param stuAppraiseWebView:
        :param stuAppraiseNative:
        :param androidCommonView:
        :param faker:
        """
        # 切换webView
        appraiseContext = stuAppraiseNative.driver.contexts
        stuAppraiseWebView.switch_h5(appraiseContext[1])
        # 选择老师
        stuAppraiseWebView.choseTeacher_webView(1)
        # 输入文本
        inputText = faker.paragraph()
        stuAppraiseWebView.InputTextarea_webView(inputText)
        # 选择年级
        stuAppraiseWebView.chose_gradeBtn_WebView()
        stuAppraiseWebView.chose_gradeList_WebView(1)
        stuAppraiseWebView.chose_gradeConfirm_WebView()
        # 切换原生native
        stuAppraiseWebView.photoCore_webView()
        appraiseContext = stuAppraiseNative.driver.contexts
        stuAppraiseNative.switch_native(appraiseContext[0])
        stuAppraiseNative.photo_album()
        androidCommonView.checkPicture(1)
        androidCommonView.checkPic_save()
        stuAppraiseNative.rotateButton(1)
        androidCommonView.rightButton()
        # 切换webView
        stuAppraiseNative.switch_h5(appraiseContext[1])
        # 切换老师
        stuAppraiseWebView.switch_teacher_webView()
        time.sleep(1)
        # 切换native
        stuAppraiseNative.switch_native(appraiseContext[0])
        stuAppraiseWebView.switchTeacher_confirm()
        # 切换webView
        stuAppraiseWebView.switch_h5(appraiseContext[1])
        stuAppraiseWebView.choseTeacher_webView(2)
        # 选择专业
        stuAppraiseWebView.choseSubjectBtn_webView()
        stuAppraiseWebView.choseSubjectList_webView(1)
        stuAppraiseWebView.choseSub_confirmWebView()
        stuAppraiseWebView.submit_webView()
        while stuAppraiseNative.driver.title == '求改画':
            time.sleep(1)
        # 切换native支付
        stuAppraiseNative.switch_native(appraiseContext[0])
        stuAppraiseNative.payBtn()
        stuAppraiseNative.payConfirm()
        stuAppraiseNative.alter_cancel()
        androidCommonView.btn_back(1)
        androidCommonView.btn_back(1)
