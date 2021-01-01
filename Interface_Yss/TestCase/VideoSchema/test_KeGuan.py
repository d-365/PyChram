# -*- coding: utf-8 -*- 
# @Time : 2020/12/23 17:23 
# @Author : dujun
# @describe : 客观题考试模式  非同时考
# @File : test_KeGuan.py
from Interface_Yss.Common.Base_Request import Base_requests
from Interface_Yss.data import VideoSchema_Url, VideoSchema_Data
import pytest


class Test_stuExam:

    def setup_class(self):
        self.re = Base_requests()
        ##考生登录
        response = self.re.post(VideoSchema_Url.stu_loginUrl, data=VideoSchema_Data.stu_Login_data)
        self.stu_ticket = response[0]['ticket']
        ##assert response[0]['datas']['user']['extInfo']['shenFenZH'] == VideoSchema_Data.stu_Login_data['loginName']
        return self.stu_ticket

    # querySubjectInfo接口
    @pytest.mark.run(order=1)
    def test_querySubjectInfo(self):
        data = {
            "ticket": self.stu_ticket,
            "data": str(VideoSchema_Data.queryData)
        }
        response = self.re.post(url=VideoSchema_Url.querySubject_url, data=data)
        assert '客观题非同时考', response[0]['datas']["data"]["subjectList"][0]["subjectName"]


if __name__ == "__main__":
    run = Test_stuExam()
    run.test_stuLogin()
    run.test_querySubjectInfo()
