# -*- coding: utf-8 -*- 
# @Time : 2021/3/11 14:47 
# @Author : dujun
# @describe : describe
# @File : timeUpdate.py
import xlrd
from xlutils.copy import copy


def writeExcel(path, col_write_one, col_write_two):
    newPath = r'C:\Users\Administrator\Desktop\test1.xlsx'
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
            cellValue = sheet.cell(i, 0)
            if cellValue.value == "3月14日14:30-16:30":
                newSheet.write(i, col_write_one, '2021-03-14 14:30')
                newSheet.write(i, col_write_two, '2021-03-14 16:30')

            elif cellValue.value == '3月13日12:30-14:30':
                newSheet.write(i, col_write_one, '2021-03-13 12:30')
                newSheet.write(i, col_write_two, '2021-03-13 14:30')

            elif cellValue.value == '3月13日14:30-16:30':
                newSheet.write(i, col_write_one, '2021-03-13 14:30')
                newSheet.write(i, col_write_two, '2021-03-13 16:30')

            elif cellValue.value == '3月13日8:00-9:30':
                newSheet.write(i, col_write_one, '2021-03-13 08:00')
                newSheet.write(i, col_write_two, '2021-03-13 09:30')

            elif cellValue.value == '3月13日9:30-11:00':
                newSheet.write(i, col_write_one, '2021-03-13 09:30')
                newSheet.write(i, col_write_two, '2021-03-13 11:00')

            elif cellValue.value == '3月14日12:30-14:30':
                newSheet.write(i, col_write_one, '2021-03-14 12:30')
                newSheet.write(i, col_write_two, '2021-03-14 14:30')

            elif cellValue.value == '3月14日14:30-16:30':
                newSheet.write(i, col_write_one, '2021-03-14 14:30')
                newSheet.write(i, col_write_two, '2021-03-14 16:30')

            elif cellValue.value == '3月14日8:00-9:30':
                newSheet.write(i, col_write_one, '2021-03-14 08:00')
                newSheet.write(i, col_write_two, '2021-03-14 09:30')

            elif cellValue.value == '3月14日9:30-11:00':
                newSheet.write(i, col_write_one, '2021-03-14 09:30')
                newSheet.write(i, col_write_two, '2021-03-14 11:00')

            elif cellValue.value == '3月15日12:30-14:30':
                newSheet.write(i, col_write_one, '2021-03-15 12:30')
                newSheet.write(i, col_write_two, '2021-03-15 14:30')

            elif cellValue.value == '3月15日14:30-16:30':
                newSheet.write(i, col_write_one, '2021-03-15 14:30')
                newSheet.write(i, col_write_two, '2021-03-15 16:30')

            elif cellValue.value == '3月15日8:00-9:30':
                newSheet.write(i, col_write_one, '2021-03-15 08:00')
                newSheet.write(i, col_write_two, '2021-03-15 09:30')

            elif cellValue.value == '3月15日9:30-11:00':
                newSheet.write(i, col_write_one, '2021-03-15 09:30')
                newSheet.write(i, col_write_two, '2021-03-15 11:00')

            elif cellValue.value == '3月16日12:30-14:30':
                newSheet.write(i, col_write_one, '2021-03-16 12:30')
                newSheet.write(i, col_write_two, '2021-03-16 14:30')

            elif cellValue.value == '3月16日14:30-16:30':
                newSheet.write(i, col_write_one, '2021-03-16 14:30')
                newSheet.write(i, col_write_two, '2021-03-16 16:30')

            elif cellValue.value == '3月16日8:00-9:30':
                newSheet.write(i, col_write_one, '2021-03-16 08:00')
                newSheet.write(i, col_write_two, '2021-03-16 09:30')

            elif cellValue.value == '3月16日9:30-11:00':
                newSheet.write(i, col_write_one, '2021-03-16 09:30')
                newSheet.write(i, col_write_two, '2021-03-16 11:00')
        newExcel.save(newPath)
        print('共处理%s 行数据' % rows)


if __name__ == "__main__":
    writeExcel(path=r'C:\Users\Administrator\Desktop\case.xlsx', col_write_one=0, col_write_two=1)
