# -*- coding: utf-8 -*- 
# @Time : 2021/1/4 20:33 
# @Author : dujun
# @describe : 客观题接口数据准备_考生端
# @File : stu_raw.py
from Interface_Yss.data import VideoSchema_Data
from Interface_Yss.project.stu import stu_project


class Base_Class:
    ticket = ''
    stu_data = VideoSchema_Data.stuData()
    re = stu_project()

    # ##App端登录( 考生 )
    # def App_login(self, data=None):
    #     url = self.cap["user"] + '/login'
    #     if data is None:
    #         response = self.re.post(url=url, data=self.stu_data.stu_Login_data)
    #         self.ticket = response['ticket']
    #         return response["ticket"]
    #     else:
    #         response = self.re.post(url=url, data=data)
    #         return response["ticket"]

    ##进入科目列表
    def querySubjectVideoInfo(self, data=None):
        datas = {
            "data": str(self.stu_data.querySubjectVideoInfo_data),
            "ticket": self.ticket
        }
        response = self.re.querySubjectVideoInfo(data=datas)
        return response

    ##进考场,checkTimeByType
    def checkTimeByType(self):
        datas = {
            "data": str(self.stu_data.checkTimeByType_data),
            "ticket": self.ticket
        }
        response = self.re.checkTimeByType(data=datas)
        return response

    ##进入录制，保存考生录制次数saveCount
    def saveCount(self):
        datas = {
            "data": str(self.stu_data.saveCount_data),
            "ticket": self.ticket
        }
        response = self.re.saveCount(data=datas)
        return response

    ##进入录制，保存考生考试状态（saveStudentExamStatus）
    def saveStudentExamStatus(self):
        datas = {
            "data": str(self.stu_data.saveStudentExamStatus_data),
            "ticket": self.ticket
        }
        response = self.re.saveStudentExamStatus(data=datas)
        return response

    ##进入录制，保存单个试题答案
    def saveQuestionResult(self):
        datas = {
            "data": str(),
            "ticket": self.ticket
        }
        response = self.re.saveQuestionResult(data=datas)
        return response

    ##结束录制，保存所有试题答案
    def saveQuestionResultAll(self):
        datas = {
            "data": str(),
            "ticket": self.ticket
        }
        response = self.re.saveQuestionResultAll(data=datas)
        return response

    ##提交视频,检查考试时间checkAllowToExam
    def checkAllowToExam(self):
        datas = {
            "data": str(),
            "ticket": self.ticket
        }
        response = self.re.checkAllowToExam(data=datas)
        return response

    ##考生提交考试视频
    def commitVideo(self):
        datas = {
            "data": str(),
            "ticket": self.ticket
        }
        response = self.re.commitVideo(data=datas)
        return response


if __name__ == "__main__":
    run = Base_Class()
    run.App_login()
    run.querySubjectVideoInfo()
