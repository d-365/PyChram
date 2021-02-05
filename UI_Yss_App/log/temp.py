# -*- coding: utf-8 -*- 
# @Time : 2021/2/3 9:42 
# @Author : dujun
# @describe : describe
# @File : temp.py 
# coding:utf-8

import logging

if __name__ == "__main__":
    ##实例化logger对象
    logger = logging.getLogger('father_logger')
    logger.setLevel(logging.INFO)

    ##创建handle_file
    logfile = './log.text'
    handle_file = logging.FileHandler(logfile, mode='w')
    ##handle_file = RotatingFileHandler(logfile,maxBytes=1*1024,backupCount=3)
    handle_file.setLevel(logging.INFO)

    ##创建handle_stream
    handle_stream = logging.StreamHandler()
    handle_stream.setLevel(logging.INFO)

    ##定义输出格式
    formatter = logging.Formatter("%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s")
    handle_stream.setFormatter(formatter)
    handle_file.setFormatter(formatter)

    ##将logger添加到handler里面
    logger.addHandler(handle_stream)
    logger.addHandler(handle_file)
