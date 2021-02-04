# -*- coding: utf-8 -*- 
# @Time : 2021/1/20 17:38 
# @Author : dujun
# @describe : describe
# @File : case1.py 
from Interface_Yss.project.stu import stu_project
from Interface_Yss.project.user import userProject
import requests


class case:
    user = userProject()
    stu = stu_project()
    ticket = ''

    def login(self):
        datas = kefu_account = {
            "loginName": "SS0",
            "password": "Test1234"
        }
        response = self.user.stuLogin(data=datas)
        self.ticket = response['ticket']
        print(self.ticket)

    def save(self):
        datas = {"m": "", "p": {"paperResultList": [
            {"userAnswerId": 13979, "questionId": 10656, "userQuestionAnswer": "A", "userQuestionAnswerRandom": "",
             "xueXiaoId": 6666, "kaoShiId": 13161, "zhuanYeId": 1224917, "esId": 3381, "baoKaoID": 2649294,
             "simulationQuesIdList": [13979, 13980, 13981, 13982], "userAnswerIdList": [13979, 13980, 13981, 13982],
             "userId": 1078754},
            {"userAnswerId": 13980, "questionId": 10652, "userQuestionAnswer": "", "userQuestionAnswerRandom": "",
             "xueXiaoId": 6666, "kaoShiId": 13161, "zhuanYeId": 1224917, "esId": 3381, "baoKaoID": 2649294,
             "simulationQuesIdList": [13979, 13980, 13981, 13982], "userAnswerIdList": [13979, 13980, 13981, 13982],
             "userId": 1078754},
            {"userAnswerId": 13981, "questionId": 10651, "userQuestionAnswer": "", "userQuestionAnswerRandom": "",
             "xueXiaoId": 6666, "kaoShiId": 13161, "zhuanYeId": 1224917, "esId": 3381, "baoKaoID": 2649294,
             "simulationQuesIdList": [13979, 13980, 13981, 13982], "userAnswerIdList": [13979, 13980, 13981, 13982],
             "userId": 1078754},
            {"userAnswerId": 13982, "questionId": 10653, "userQuestionAnswer": "", "userQuestionAnswerRandom": "",
             "xueXiaoId": 6666, "kaoShiId": 13161, "zhuanYeId": 1224917, "esId": 3381, "baoKaoID": 2649294,
             "simulationQuesIdList": [13979, 13980, 13981, 13982], "userAnswerIdList": [13979, 13980, 13981, 13982],
             "userId": 1078754}]}}
        payload = {
            "data": str(datas),
            "ticket": self.ticket
        }
        for i in range(0, 2):
            response = self.stu.saveQuestionResultAll(data=payload)
            print(response)

    def stuInfo(self):
        datas = '{"p":{  "statusText" : "未上传",  "resUrl" : "http://img.artstudent.cn/pr/2020-11-07/6a0c0a137a384e63b9bb7a05f3fc94f2.jpg",  "typeCode" : "Photo",  "resType" : 1,  "commited" : false,  "auditDate2Str" : "",  "commitDateStr" : "",  "auditDate1Str" : "",  "icon" : "http:\\/\\/img.artstudent.cn\\/pic\\/ic_rz_user_icon.png",  "ord" : 1,  "stuType" : 3,  "subTitleColor" : "#bbbbbb",  "tId" : 1,  "auditPass" : false,  "statusTextColor" : "#ff9f37",  "typeName" : "给考生拍照"},"m":""}'
        payload = {
            "data": datas,
            "ticket": self.ticket
        }
        url = 'http://192.168.18.202:23000/api/m/auth/service/v191119/upload_auth_res.ws'
        headers = {
            "platformType": "2",
            "udid": "1519fbbacd907027e734fbf8b17b2a7a",
            "tkn": "yx001",
            "yks": "1"
        }

        response = requests.post(url=url, data=payload, headers=headers)
        result = response.json()
        result_text = response.text
        print(result)
        print(result_text)


if __name__ == "__main__":
    run = case()
    run.login()
    # run.save()
    run.stuInfo()
