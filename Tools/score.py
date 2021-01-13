# -*- coding: utf-8 -*- 
# @Time : 2021/1/11 11:25 
# @Author : dujun
# @describe : 打分计算
# @File : score.py 
from Interface_Yss.Common.Read_File import read_excel
from xlutils.copy import copy


##祛除最高最低分算平均分
def top_low():
    path = r"C:\Users\Administrator\Downloads\考生打分项考官成绩导出.xlsx"
    file = read_excel(path)
    ##获取excel
    excel = file[0]
    ##获取sheet
    sheet = file[1]
    ##获取行数
    rows = file[2]
    ##获取列数
    cols = file[3]
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
        sums = list_score[0] + list_score[1] + list_score[2] + list_score[3] + list_score[4]
        qq = sums / 5
        newSheet.write(i, 15, qq)

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


if __name__ == "__main__":
    top_low()
