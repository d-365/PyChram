# -*- coding: utf-8 -*-
# @Time : 2021/4/6 11:17
# @Author : dujun
# @describe : 图片裁剪
# @File : photoTailor.py

from PIL import Image


def imgTailor(path, imgSaveName):
    img = Image.open(path)
    cropped = img.crop((0, 110, 1080, 2240))  # (left, upper, right, lower)
    cropped.save(r'D:\pythonProject\UI_Yss_App\photo\%s.png' % imgSaveName)


if __name__ == "__main__":
    path = r'D:\pythonProject\UI_Yss_App\photo\screen.png'
    imgTailor(path, 'zixunInfo.png')
