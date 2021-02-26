# -*- coding: utf-8 -*- 
# @Time : 2020/12/17 19:31 
# @Author : dujun
# @describe : describe
# @File : test_Create_Stu.py

import pytest
from Interface_Yss.data import Account
from Interface_Yss.Common.Random import random_str
from Interface_Yss.data.province import shenFen


class Test_CreateStu:

    ##管理员创建考生
    def test_Create_Stu(self, platSetUp, stuData):

        for i in range(0, len(stuData)):
            datas = {
                "yongHuMing": stuData[i],
                "yongHuKL": "Test1234",
                "agginYongHuKL": "Test1234",
                "yongHuLB": 100,
                "ticket": platSetUp[1]
            }
            response = platSetUp[0].createStu(data=datas)

    ##完善上传考生信息
    def test_stuComplete(self, userRequest, stuData):
        for i in range(0, len(stuData)):
            ##考生登录
            datas = {
                "loginName": stuData[i],
                "password": "Test1234"
            }
            stuResponse = userRequest.stuLogin(data=datas)
            stuTicket = stuResponse['ticket']
            ##提交个人信息
            datas = {"m": "",
                     "p": {"zhengJianLX": "4", "shenFenZH": stuData[i], "kaoShengXM": random_str(2),
                           "xingBie": "男",
                           "chuShengRQ": "1992-01-01", "minZu": "汉族", "tongXinDZExt": "330000-330100-330110",
                           "tongXinDZ": "科创园",
                           "linkAddress": "浙江省/杭州市/余杭区", "addressee": random_str(2), "shouJi": "15552352535",
                           "tongXinYB": "100000",
                           "qQ": "12437367", "xueLi": "高中", "stuType": 3, "gaoKaoSFH": shenFen("上海市")[1],
                           "gaoKaoSF": shenFen("上海市")[0],
                           "zhengZhiMM": "团员", "suoZaiXX": "浙江大学", "kaoShengHao": "21310000000000", "yingWangJie": "应届",
                           "wenLiKe": "不分文理", "jiaZhangDH": "15557846664", "dingPhone": "",
                           "name": ["云豹", "云豹"],
                           "relation": ["其他", "其他"], "companyName": ["亦闲", "亦闲"], "job": ["技术", "技术"],
                           "phoneNumber": ["15576676767", "15373736767"], "huKou": "", "qualifyAuth": "",
                           "passFlag": "", "grade": ""}}
            payload = {
                'data': str(datas),
                'ticket': stuTicket
            }
            response = userRequest.save_stuinfo(data=payload)
            print(stuData[i], '完善资料', response)

    ##上传报考资料
    def test_uploadStuPhoto(self, userRequest, stuData):
        for i in range(0, len(stuData)):
            ##考生登录
            datas = {
                "loginName": stuData[i],
                "password": "Test1234"
            }
            stuResponse = userRequest.stuLogin(data=datas)
            stuTicket = stuResponse['ticket']

            ##给考生拍照
            datas_one = '{"p":{  "statusText" : "未上传",  "resUrl" : "http://img.artstudent.cn/pr/2020-11-07/6a0c0a137a384e63b9bb7a05f3fc94f2.jpg",  "typeCode" : "Photo",  "resType" : 1,  "commited" : false,  "auditDate2Str" : "",  "commitDateStr" : "",  "auditDate1Str" : "",  "icon" : "http:\\/\\/img.artstudent.cn\\/pic\\/ic_rz_user_icon.png",  "ord" : 1,  "stuType" :3,  "subTitleColor" : "#bbbbbb",  "tId" : 1,  "auditPass" : false,  "statusTextColor" : "#ff9f37",  "typeName" : "给考生拍照"},"m":""}'
            payload_one = {
                "data": datas_one,
                "ticket": stuTicket
            }
            response_one = userRequest.uploadStuPhoto(data=payload_one)

            ##上传身份证正面照
            datas_two = '{"p":{  "ord" : 2,  "nameFlag" : "2",  "subTitleColor" : "#bbbbbb",  "resType" : 1,  "auditPass" : false,  "statusTextColor" : "#ff9f37",  "typeName" : "上传身份证正面照",  "commitDateStr" : "",  "icon" : "http:\\/\\/img.artstudent.cn\\/pic\\/ic_rz_idcard_icon.png",  "resUrl" : "http:\\/\\/img.artstudent.cn\\/pr\\/2020-11-05\\/bacc3dc3e6ac4aeebbf185d5dcb6fe02.jpg",  "avatarUrl" : "http:\\/\\/img.artstudent.cn\\/pr\\/2020-11-05\\/dab3791f2fd347c58b2f71d317fa0baf.jpg",  "cardFlag" : "2",  "auditDate2Str" : "",  "cardUrl" : "http:\\/\\/img.artstudent.cn\\/pr\\/2020-11-05\\/dab3791f2fd347c58b2f71d317fa0baf.jpg",  "commited" : false,  "auditDate1Str" : "",  "stuType" : 3,  "statusText" : "未上传",  "tId" : 2,  "typeCode" : "IDPhoto"},"m":""}'
            payload_two = {
                "data": datas_two,
                "ticket": stuTicket
            }
            response_two = userRequest.uploadStuPhoto(data=payload_two)

            ##上传艺术证
            datas_three = '{"p":{  "statusText" : "未上传",  "resUrl" : "http:\\/\\/img.artstudent.cn\\/pr\\/2020-11-05\\/529e0024eb274535919faa2f63dc8b2d.jpg",  "typeCode" : "ArtPhoto",  "resType" : 1,  "commited" : false,  "auditDate2Str" : "",  "commitDateStr" : "",  "auditDate1Str" : "",  "icon" : "http:\\/\\/img.artstudent.cn\\/pic\\/ic_rz_art_icon.png",  "ord" : 3,  "stuType" : 3,  "subTitleColor" : "#bbbbbb",  "tId" : 3,  "auditPass" : false,  "statusTextColor" : "#ff9f37",  "typeName" : "上传艺术类专业报考证"},"m":""}'
            payload_three = {
                "data": datas_three,
                "ticket": stuTicket
            }
            response_three = userRequest.uploadStuPhoto(data=payload_three)

            ##上传考生视频
            datas_four = '{"p":{  "statusText" : "未上传",  "resUrl" : "http:\\/\\/img.artstudent.cn\\/pr\\/2020-11-05\\/bd86e242bfe3426d820787521c8d1e93.mp4",  "typeCode" : "video",  "resType" : 2,  "commited" : false,  "auditDate2Str" : "",  "commitDateStr" : "",  "auditDate1Str" : "",  "icon" : "http:\\/\\/img.artstudent.cn\\/pic\\/ic_rz_video_icon.png",  "ord" : 4,  "stuType" : 3,  "subTitleColor" : "#bbbbbb",  "tId" : 4,  "auditPass" : false,  "statusTextColor" : "#ff9f37",  "typeName" : "录制考生视频"},"m":""}'
            payload_four = {
                "data": datas_four,
                "ticket": stuTicket
            }
            response_four = userRequest.uploadStuPhoto(data=payload_four)

            ##提交报考资料
            datas_last = {"p": {"serviceType": "1"}, "m": ""}
            payload_last = {
                "data": str(datas_last),
                "ticket": stuTicket
            }
            response_last = userRequest.submitStuInfo(data=payload_last)
            print(stuData[i], '提交报考资料', response_last)

    ##登录客服账号，进行审核操作
    def test_check(self, stuData, platSetUp, auditRequest):
        datas = Account.kefu_account
        response = platSetUp[0].plat_login(data=datas)
        kefu_ticket = response['ticket']
        for i in range(0, len(stuData)):
            datas = stuData[i]
            payload = {
                "idcardNo": datas,
                "ticket": kefu_ticket
            }
            ##获取考生psId
            responsePsid = auditRequest.query_psId(data=payload)
            psId = responsePsid['datas']['page']['dataList'][0]['psId']

            ##审核
            checkPayload = {
                "psId": psId,
                "auditFlag": 1,
                "applyTicket": 1,
                "ticket": kefu_ticket
            }
            responseCheck = auditRequest.check_stuInfo(data=checkPayload)
            print(stuData[i], '审核成功', responseCheck)


if __name__ == "__main__":
    pytest.main()
