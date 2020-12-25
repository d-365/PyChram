from Interface_Yss.TestCase.others.manage import TestManage
import requests
from Interface_Yss.Common.Random import random_str


class TestStu_login():

    def Test_stulg(self):

        run = TestManage()
        run.Testmanage_login()
        run.TestCreate_stu()
        stu_loginUrl = "http://192.168.18.202:10100/login"
        header_stu = {
            "platformType": "2",
            "udid": "1519fbbacd907027e734fbf8b17b2a7a",
            "tkn": "yx001",
            "yks": "1"
        }
        for i in range(0, len(run.list_data)):
            stu_datas = {
                "loginName": run.list_data[i],
                "password": "Test1234",
            }
            ##考生登录，获取考生ticket
            response_login = requests.post(url=stu_loginUrl, headers=header_stu, data=stu_datas)
            print(run.list_data[i] + '登录', response_login.json())
            ticket_stu = response_login.json()["ticket"]
            ##提交考生个人信息
            StUpload_url = "http://user.51bm.net.cn/api/m/auth/user/save_stuinfo.htm"
            data_Stubasic = {"m": "",
                             "p": {"zhengJianLX": "4", "shenFenZH": run.list_data[i], "kaoShengXM": random_str(2),
                                   "xingBie": "男",
                                   "chuShengRQ": "1992-01-01", "minZu": "汉族", "tongXinDZExt": "330000-330100-330110",
                                   "tongXinDZ": "科创园",
                                   "linkAddress": "浙江省/杭州市/余杭区", "addressee": "云豹", "shouJi": "15552352535",
                                   "tongXinYB": "100000",
                                   "qQ": "12437367", "xueLi": "大学", "stuType": 5, "gaoKaoSFH": "330000",
                                   "gaoKaoSF": "浙江省",
                                   "zhengZhiMM": "团员", "suoZaiXX": "浙江大学", "kaoShengHao": "", "yingWangJie": "应届",
                                   "wenLiKe": "不分文理", "jiaZhangDH": "15557846664", "dingPhone": "",
                                   "name": ["云豹", "云豹"],
                                   "relation": ["其他", "其他"], "companyName": ["亦闲", "亦闲"], "job": ["技术", "技术"],
                                   "phoneNumber": ["15576676767", "15373736767"], "huKou": "", "qualifyAuth": "",
                                   "passFlag": "", "grade": ""}}
            payload = {
                'data': str(data_Stubasic),
                'ticket': ticket_stu
            }
            requests.options(url=StUpload_url, headers=header_stu)
            ##提交个人信息
            response_upload = requests.post(url=StUpload_url, headers=header_stu, data=payload)
            print('提交个人信息', response_upload.json())

            ##给考生拍照
            stuPhoto_url = "http://192.168.18.202:23000/api/m/auth/service/v191119/upload_auth_res.ws"
            data_one = '{"p":{  "statusText" : "未上传",  "resUrl" : "http://img.artstudent.cn/pr/2020-11-07/6a0c0a137a384e63b9bb7a05f3fc94f2.jpg",  "typeCode" : "Photo",  "resType" : 1,  "commited" : false,  "auditDate2Str" : "",  "commitDateStr" : "",  "auditDate1Str" : "",  "icon" : "http:\/\/img.artstudent.cn\/pic\/ic_rz_user_icon.png",  "ord" : 1,  "stuType" : 3,  "subTitleColor" : "#bbbbbb",  "tId" : 1,  "auditPass" : false,  "statusTextColor" : "#ff9f37",  "typeName" : "给考生拍照"},"m":""}'
            photo_oneData = {
                "data": data_one,
                "ticket": ticket_stu,
                "ts": "20201105195432"
            }
            requests.post(url=stuPhoto_url, headers=header_stu, data=photo_oneData)

            ##上传身份证正面照
            data_two = '{"p":{  "ord" : 2,  "nameFlag" : "2",  "subTitleColor" : "#bbbbbb",  "resType" : 1,  "auditPass" : false,  "statusTextColor" : "#ff9f37",  "typeName" : "上传身份证正面照",  "commitDateStr" : "",  "icon" : "http:\/\/img.artstudent.cn\/pic\/ic_rz_idcard_icon.png",  "resUrl" : "http:\/\/img.artstudent.cn\/pr\/2020-11-05\/bacc3dc3e6ac4aeebbf185d5dcb6fe02.jpg",  "avatarUrl" : "http:\/\/img.artstudent.cn\/pr\/2020-11-05\/dab3791f2fd347c58b2f71d317fa0baf.jpg",  "cardFlag" : "2",  "auditDate2Str" : "",  "cardUrl" : "http:\/\/img.artstudent.cn\/pr\/2020-11-05\/dab3791f2fd347c58b2f71d317fa0baf.jpg",  "commited" : false,  "auditDate1Str" : "",  "stuType" : 3,  "statusText" : "未上传",  "tId" : 2,  "typeCode" : "IDPhoto"},"m":""}'
            photo_twoData = {
                "data": data_two,
                "ticket": ticket_stu,
                "ts": "20201105195432"
            }
            requests.post(url=stuPhoto_url, headers=header_stu, data=photo_twoData)

            ##上传艺术证
            data_there = '{"p":{  "statusText" : "未上传",  "resUrl" : "http:\/\/img.artstudent.cn\/pr\/2020-11-05\/529e0024eb274535919faa2f63dc8b2d.jpg",  "typeCode" : "ArtPhoto",  "resType" : 1,  "commited" : false,  "auditDate2Str" : "",  "commitDateStr" : "",  "auditDate1Str" : "",  "icon" : "http:\/\/img.artstudent.cn\/pic\/ic_rz_art_icon.png",  "ord" : 3,  "stuType" : 3,  "subTitleColor" : "#bbbbbb",  "tId" : 3,  "auditPass" : false,  "statusTextColor" : "#ff9f37",  "typeName" : "上传艺术类专业报考证"},"m":""}'
            photo_thereData = {
                "data": data_there,
                "ticket": ticket_stu,
                "ts": "20201105195432"
            }
            requests.post(url=stuPhoto_url, headers=header_stu, data=photo_thereData)

            ##上传考生视频
            data_four = '{"p":{  "statusText" : "未上传",  "resUrl" : "http:\/\/img.artstudent.cn\/pr\/2020-11-05\/bd86e242bfe3426d820787521c8d1e93.mp4",  "typeCode" : "video",  "resType" : 2,  "commited" : false,  "auditDate2Str" : "",  "commitDateStr" : "",  "auditDate1Str" : "",  "icon" : "http:\/\/img.artstudent.cn\/pic\/ic_rz_video_icon.png",  "ord" : 4,  "stuType" : 3,  "subTitleColor" : "#bbbbbb",  "tId" : 4,  "auditPass" : false,  "statusTextColor" : "#ff9f37",  "typeName" : "录制考生视频"},"m":""}'
            photo_fourData = {
                "data": data_four,
                "ticket": ticket_stu,
                "ts": "20201105195432"
            }
            requests.post(url=stuPhoto_url, headers=header_stu, data=photo_fourData)

            ##提交报考资料
            StuPhoto_uploadUrl = 'http://192.168.18.202:23000/api/m/auth/service/v191119/commit_auth_res.ws'
            photo_submit = '{"p":{  "serviceType" : "1"},"m":""}'
            photo_upload = {
                "data": photo_submit,
                "ticket": ticket_stu,
                "ts": "20201105195432"
            }
            response = requests.post(url=StuPhoto_uploadUrl, headers=header_stu, data=photo_upload)
            print('提交个人资料', response.json())


run = TestStu_login()
run.Test_stulg()
