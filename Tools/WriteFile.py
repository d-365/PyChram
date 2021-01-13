# -*- coding: utf-8 -*- 
# @Time : 2021/1/8 16:42 
# @Author : dujun
# @describe : 批量生成Excel数据（考生资格库 + 考生考卷导入）
# @File : WriteFile.py
import xlwt
import xlrd
from xlutils.copy import copy
from Interface_Yss.Common.Random import random_str, random_int


class createExcel:

    @staticmethod
    def createExcel():
        # 文件地址
        savePath = r'C:\Users\Administrator\Downloads\test.xlsx'
        file = xlwt.Workbook(encoding='utf-8')
        file.add_sheet('sheetName', cell_overwrite_ok=True)
        file.save(savePath)

    @staticmethod
    def photoUpdate():
        ##文件地址
        path = r'C:\Users\Administrator\Downloads\photo.xlsx'
        with open(path) as file:
            ##视频地址
            videoUrl = 'http://art-video-shanghai.artstudent.cn/img/10355/3893/2855/ffb491c649ce445f99c6d008d624e19c_uid38058042.jpg'
            ##科目名称
            subjectName = '画画'
            ##打分项名称
            scoreName = '画图实物'
            ##准考证号
            examCard = ''

            file = xlrd.open_workbook(path)
            newFile = copy(file)
            sheet = newFile.get_sheet(0)

            for i in range(1, 60000):
                ##准考证号
                examCard = 60000
                ##科目名称行,列(row , col)
                sheet.write(i, 0, subjectName)
                ##打分项名称
                sheet.write(i, 1, scoreName)
                ##准考证号
                sheet.write(i, 2, examCard + i)
                ##视频地址
                sheet.write(i, 3, videoUrl)

            ##保存复制的excel
            newFile.save(path)

    @staticmethod
    def stuUpdate():
        filePath = r'C:\Users\Administrator\Downloads\qualification.xlsx'
        with open(filePath) as file:
            ##考生姓名
            stuName = ''
            ##性别
            sex = '男'
            ##考试开始时间
            startTime = "2018-01-01 08:30"
            ##考试结束时间
            endTime = '2018-01-02 08:30'
            ##考试专业名称
            professional = '画画'
            ##考生ID
            stuId = random_int(3)
            ##考生号
            stuNumber = random_int(3)
            ##考生证件照片
            stuPhoto = "http://img.artstudent.cn/pr/2020-11-08/040b28aa3dc249d496553290a5f1d8ea.jpg"

            ##额外信息
            extraInformation = random_str(3)

            file = xlrd.open_workbook(filePath)
            newFile = copy(file)
            sheet = newFile.get_sheet(0)

            for i in range(1, 60000):
                ##准考证号
                examCard = 60000
                ##证件号码
                shenFen = 100
                ##准考证号
                sheet.write(i, 0, i + examCard)
                ##证件号码
                sheet.write(i, 1, i + shenFen)
                ##考生姓名
                sheet.write(i, 2, random_str(2))
                ##性别
                sheet.write(i, 3, sex)
                ##考试开始时间
                sheet.write(i, 4, startTime)
                ##考试结束时间
                sheet.write(i, 5, endTime)
                ##考试专业名称
                sheet.write(i, 6, professional)
                ##考生号
                sheet.write(i, 8, stuNumber)
                ##考生证件照片
                sheet.write(i, 9, stuPhoto)
                ##额外信息
                sheet.write(i, 12, extraInformation)

            ##保存复制的excel
            newFile.save(filePath)


if __name__ == "__main__":
    run = createExcel()
    run.photoUpdate()
    run.stuUpdate()
    # run.createExcel()
