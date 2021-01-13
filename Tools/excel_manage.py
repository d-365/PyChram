# -*- coding: utf-8 -*- 
# @Time : 2021/1/11 17:51 
# @Author : dujun
# @describe : 处理excel数据
# @File : excel_manage.py 

import xlrd
from xlutils.copy import copy


##读取Excel
def read_excel(path):
    with open(path):
        excel = xlrd.open_workbook(path)
        ##获取excel中第一个sheet
        sheet = excel.sheet_by_index(0)
        ##获取总行数
        rows = sheet.nrows
        ##获取总列数
        cols = sheet.ncols
        newExcel = copy(excel)
        newSheet = newExcel.get_sheet(0)
        for i in range(1, rows):
            list_score = []
            cellValue = sheet.cell(i, 7).value
            floatValue = float(cellValue)
            list_score.append(floatValue)
            cellValue = sheet.cell(i, 8).value
            floatValue = float(cellValue)
            list_score.append(floatValue)
            cellValue = sheet.cell(i, 9).value
            floatValue = float(cellValue)
            list_score.append(floatValue)
            cellValue = sheet.cell(i, 10).value
            floatValue = float(cellValue)
            list_score.append(floatValue)
            cellValue = sheet.cell(i, 11).value
            floatValue = float(cellValue)
            list_score.append(floatValue)
            list_score.sort(reverse=True)
            ##祛除最低分
            list_score.pop(0)
            ##祛除最高分
            list_score.pop()
            ##计算总分
            total = list_score[0] + list_score[1] + list_score[2]
            ##计算平均分
            ave = total / len(list_score)
            ##复制写入excel
            newSheet.write(0, 13, '祛除最高最低总分')
            newSheet.write(i, 13, total)
            newSheet.write(0, 14, '祛除最高最低平均分')
            newSheet.write(i, 14, ave)
            newExcel.save(path)
