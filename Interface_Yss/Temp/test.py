# -*- coding: utf-8 -*- 
# @Time : 2020/12/10 19:41 
# @Author : dujun
# @describe : describe
# @File : test.py 

from Interface_Yss.Common.Base_Request import Base_requests
import requests


class TestCase:
    request = Base_requests()

    def test_schLogin(self):
        url = "http://college.51bm.net.cn/login"
        datas = {
            "loginName": 'yuanxiao',
            "password": 'Test1234'
        }
        response = self.request.post(url=url, data=datas)
        self.schTicket = response["ticket"]
        print("学校ticket", self.schTicket)

    def test_stuLogin(self):
        url = 'http://user.51bm.net.cn/login'
        datas = {
            "loginName": 'haitun100',
            "password": 'Csk001'
        }
        response = self.request.post(url=url, data=datas)
        self.stuTicket = response["ticket"]
        print('考生ticket', self.stuTicket)

    def test_queryVideo(self):
        url = "http://examvideo.51bm.net.cn/auth/school/assignDetail/loadExaminerAssignDetailData.htm"
        datas = {
            "stuIDCard": "haitun100",
            "riChengID": "11109768",
            "riChengID": "11109768",
            "kaoShiID": "13165",
            "kaoDianID": "728",
            "esId": "3233",
            "ticket": self.schTicket
        }

        response = self.request.post(url=url, data=datas)
        print("查询视频", response)

    def test_commitVideo(self):
        url = 'http://stu.51bm.net.cn/api/m/auth/video/commitVideo.ws'
        data = {
            "p": {
                "videoCode": "v1609817911695",
                "ticket": "XwovGmYkb9$2VFZSTlBRPT07T2p3NlBEbzZQRFU2UFR3PTsxMzEz",
                "esId": 3233,
                "videoFileSize": 13355599,
                "svId": "11328",
                "kaoShengID": "247253",
                "fileValidCode": "52ffda1ac0ec7e8bda8d8eac84b627c7",
                "baoKaoId": 2634769,
                "riChengId": 11109768,
                "shootTime": "1609817940432",
                "recordPhoto": "http://art-video.artstudent.cn/photo/test/6666/1224543/3233/dc7fbfa5376f4124887a59ab5ba9e1fc_uid1078177.jpg",
                "photoAttachment": "",
                "xueXiaoID": 6666,
                "stuVideoLength": 23,
                "shenFenZH": "HAITUN100",
                "yongHuID": 1078177,
                "videoUrl": "http://art-video.artstudent.cn/pr/test/6666/1224543/3233/45656a7f351c44da961bd390894fe6fc_uid1078177.mp4",
                "zhuanYeId": 1224543,
                "supplement": "",
                "zhuanYeMC": "基本专业",
                "seId": "",
                "shootArea": " ",
                "subjectCode": "1",
                "subjectName": "客观题非同时考"
            },
            "m": ""
        }
        datas = {
            "data": str(data),
            "ticket": self.stuTicket
        }
        response = self.request.post(url=url, data=datas)
        print('提交视频', response)


if __name__ == "__main__":
    run = TestCase()
    run.test_schLogin()
    run.test_stuLogin()
    run.test_queryVideo()
    run.test_commitVideo()
