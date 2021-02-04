# -*- coding: utf-8 -*- 
# @Time : 2021/1/22 22:08 
# @Author : dujun
# @describe : describe
# @File : temp.py

def case1(*key):
    lenth = len(key)
    for i in range(0, lenth):
        print(key[i])


if __name__ == "__main__":
    case1("'2','2'")
