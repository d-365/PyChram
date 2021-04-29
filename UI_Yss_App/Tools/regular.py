# -*- coding: utf-8 -*- 
# @Time : 2021/3/25 15:16 
# @Author : dujun
# @describe : 正则提取文件
# @File : re.py

import os


class regular:

    # 提取AdbCommand文本
    def reInt(self, command):
        reValue = os.popen(command).readlines()
        return reValue
