# -*- coding: utf-8 -*- 
# @Time : 2021/2/19 15:56 
# @Author : dujun
# @describe : describe
# @File : test.py
import hashlib
import shutil
import sys
from os.path import join, dirname, isdir
import os
import re
from faker import Faker
import operator
from PIL import Image
from os.path import abspath, dirname

# def screenCap(screenCapName):
#     os.popen(r'adb shell screencap -p /sdcard/%s.png' % screenCapName)
#     os.popen(r'adb pull /sdcard/%s.png D:\pythonProject\UI_Yss_App\screenCap' % screenCapName)

# def assert_photo():
#     path = r'D:\pythonProject\UI_Yss_App\photo'
#     os.path.join(path, 'A1.jpg')
#     os.path.join(path, 'A2.jpg')
#     os.path.join(path, 'B1.png')
#     A1 = Image.open(r'photo\A1.jpg')
#     A2 = Image.open(r'photo\A2.jpg')
#     B1 = Image.open(r'photo\B1.png')
#
#     A1cmd5 = hashlib.md5(A1.read()).hexdigest()
#     A2cmd5 = hashlib.md5(A2.read()).hexdigest()
#     print(A1cmd5, A2cmd5)


#
# #均值哈希算法
# def aHash(img):
#     #缩放为8*8
#     img=cv2.resize(img,(8,8))
#     #转换为灰度图
#     gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
#     #s为像素和初值为0，hash_str为hash值初值为''
#     s=0
#     hash_str=''
#     #遍历累加求像素和
#     for i in range(8):
#         for j in range(8):
#             s=s+gray[i,j]
#     #求平均灰度
#     avg=s/64
#     #灰度大于平均值为1相反为0生成图片的hash值
#     for i in range(8):
#         for j in range(8):
#             if  gray[i,j]>avg:
#                 hash_str=hash_str+'1'
#             else:
#                 hash_str=hash_str+'0'
#     return hash_str

from Interface_Yss.project.school import school_project
from Interface_Yss.project.examVideo import examVideo_project
from Interface_Yss.project.college import college_project

if __name__ == "__main__":
    college = college_project(environment='')
    print(college.login()["ticket"])
