# -*- coding: utf-8 -*- 
# @Time : 2020/12/17 14:38 
# @Author : dujun
# @describe : 去读文件
# @File : Read_File.py

##按照行读取Txt文档,存为列表
import xlrd


def ReadTxt_List(path):
    with open(path, encoding='utf-8') as file:
        data_line = file.readlines()
        datas = []
        for line in data_line:
            data = str(line).replace("\n", "")
            newdata = data.split(':')
            datas.append(newdata)
        print(datas)


##按照行读取Txt文档，存为dict
def ReadTxt_Dict(path):
    with open(path, encoding='utf-8') as file:
        data_line = file.readlines()
        datas = {}
        for line in data_line:
            print('line', line)
            data = str(line).replace("\n", "")
            print('data', data)
            newdata = data.split()
            print('newdata', newdata)
            datas[newdata[1]] = newdata[0]
        print(datas)


##读取Excel
def read_excel(path):
    with open(path):
        excel = xlrd.open_workbook(path)
        sheet = excel.sheet_by_index(0)
        ##获取总行数
        rows = sheet.nrows
        ##获取总列数
        cols = sheet.ncols
        return excel, sheet, rows, cols


if __name__ == "__main__":
    ReadTxt_Dict(r'C:\Users\Administrator\Desktop\new1.txt')
    # ReadTxt_List(r'D:\pythonProject\Interface_Yss\File\data.txt')
    # read_excel(r"C:\Users\Administrator\Downloads\考生打分项考官成绩导出.xlsx")
