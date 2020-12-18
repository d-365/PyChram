# -*- coding: utf-8 -*- 
# @Time : 2020/12/17 14:38 
# @Author : dujun
# @describe : 去读文件
# @File : Read_File.py

##按照行读取Txt文档,存为列表
def ReadTxt_List(path):
    with open(path, encoding='utf-8') as file:
        data_line = file.readlines()
        datas = []
        for line in data_line:
            data = str(line).replace("\n","")
            newdata = data.split(':')
            datas.append(newdata)
        print(datas)


##按照行读取Txt文档，存为dict
def ReadTxt_Dict(path):
    with open(path,encoding='utf-8') as file:
        data_line = file.readlines()
        datas = {}
        for line in data_line:
            data = str(line).replace("\n","")
            newdata = data.split(':')
            datas[newdata[0]] = newdata[1]
        print(datas)


if __name__ == "__main__":
    ReadTxt_Dict(r'D:\pythonProject\Interface_Yss\File\data.txt')
    ReadTxt_List(r'D:\pythonProject\Interface_Yss\File\data.txt')
