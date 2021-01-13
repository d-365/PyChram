# -*- coding: utf-8 -*- 
# @Time : 2020/12/31 11:45 
# @Author : dujun
# @describe : 客观题数据,非同时考
# @File : VideoSchema_Data.py

class stuData:
    ##日程ID
    riChengId = ''
    ##报考ID
    baoKaoId = ''
    ##学校ID
    xueXiaoId = ''

    ##考生账号
    stu_Login_data = {
        "loginName": 'HAITUN100',
        'password': 'Csk001'
    }

    ##进入科目列表querySubjectVideoInfo
    querySubjectVideoInfo_data = {
        "m": "",
        "p": {
            "riChengId": riChengId,
            "riChengID": riChengId,
            "baoKaoId": baoKaoId,
            "simulation": 0
        }
    }

    ##查询科目列表
    queryData = {
        "m": "",
        "p": {
            "riChengId": 11109768,
            "riChengID": 11109768,
            "baoKaoId": 2634769,
            "simulation": 0
        }
    }

    ##进考场,checkTimeByType
    checkTimeByType_data = {
        "m": "",
        "p": {
            "xueXiaoId": 6666,
            "subjectName": "客观题非同时考",
            "zhuanYeMC": "基本专业",
            "esId": 3233,
            "riChengId": 11109768,
            "baseRiChengId": 11109768,
            "svId": 11328,
            "drawQuestion": 2,
            "checkTimeType": 2
        }
    }

    ##进入录制，保存考生录制次数saveCount
    saveCount_data = {
        "m": "",
        "p": {
            "subjectName": "客观题非同时考",
            "esId": 3233,
            "riChengId": 11109768,
            "updateNum": 1
        }
    }
    ##进入录制，保存考生考试状态（saveStudentExamStatus）
    saveStudentExamStatus_data = {

    }

    ##提交视频,检查考试时间checkAllowToExam
    checkAllowToExam_data = {

    }

    ##考生提交考试视频
    commitVideo_data = {

    }

    ##进入录制，保存单个试题答案
    saveQuestionResult_data = {

    }

    ##进入录制，保存所有试题答案
    saveQuestionResultAll_data = {

    }


class platData:
    ##考生身份证号
    stuIDCard = 'haitun100'
    ##日程ID
    riChengID = ''
    ##考试ID
    kaoShiID = ''
    ##考点ID
    kaoDianID = ''
    ##科目ID
    esId = ''

    ##查询视频data
    schoolQueryVideo = {
        "stuIDCard": stuIDCard,
        "riChengID": riChengID,
        "riChengID": riChengID,
        "kaoShiID": kaoShiID,
        "kaoDianID": kaoDianID,
        "esId": esId
    }
