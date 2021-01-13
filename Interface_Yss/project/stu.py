# -*- coding: utf-8 -*- 
# @Time : 2021/1/9 20:24 
# @Author : dujun
# @describe : stu
# @File : stu.py 
from Interface_Yss.Common.Base_Request import Base_requests
from Interface_Yss.data.caps import Caps


class stu_project:
    re = Base_requests()
    cap = Caps()

    ##科目列表
    def querySubjectVideoInfo(self, data):
        url = self.cap['stu'] + '/api/m/auth/video/querySubjectVideoInfo.htm'
        response = self.re.post(url=url, data=data)
        return response

    ##进考场,checkTimeByType
    def checkTimeByType(self, data):
        url = self.cap['stu'] + '/api/m/auth/video/check_time_by_type.htm'
        response = self.re.post(url=url, data=data)
        return response

    ##进入录制，保存考生录制次数saveCount
    def saveCount(self, data):
        url = self.cap['stu'] + "/api/m/auth/video/saveCount.htm"
        response = self.re.post(url=url, data=data)
        return response

    ##进入录制，保存考生考试状态（saveStudentExamStatus）
    def saveStudentExamStatus(self, data):
        url = self.cap['stu'] + '/api/m/auth/student/log/saveStudentExamStatus.htm'
        response = self.re.post(url=url, data=data)
        return response

    ##进入录制，保存单个试题答案
    def saveQuestionResult(self, data):
        url = self.cap['stu'] + "/api/m/auth/video/save_examination_paper_question_result.htm"
        response = self.re.post(url=url, data=data)
        return response

    ##结束录制，保存所有试题答案
    def saveQuestionResultAll(self, data):
        url = self.cap['stu'] + "/api/m/auth/video/save_examination_paper_question_result_all.htm"
        response = self.re.post(url=url, data=data)
        return response

    ##提交视频,检查考试时间checkAllowToExam
    def checkAllowToExam(self, data):
        url = self.cap['stu'] + '/api/m/auth/video/check_allow_to_exam.htm'
        response = self.re.post(url=url, data=data)
        return response

    ##考生提交考试视频
    def commitVideo(self, data):
        url = self.cap['stu'] + '/api/m/auth/video/commitVideo.ws'
        response = self.re.post(url=url, data=data)
        return response
