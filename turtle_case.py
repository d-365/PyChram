# -*- coding: utf-8 -*- 
# @Time : 2021/3/13 18:45 
# @Author : dujun
# @describe : describe
# @File : turtle_case.py.py 
import turtle as t

if __name__ == "__main__":
    t.pensize(1)

    for x in range(1, 100):
        t.forward(10)
        t.right(x)

    t.done()
