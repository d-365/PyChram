# -*- coding: utf-8 -*- 
# @Time : 2020/12/9 17:23 
# @Author : dujun
# @describe : describe
# @File : pymysql.py

import pymysql

def Mysql():
    ##连接数据库
    conn1 = pymysql.connect(host='192.168.18.203', port=3307, user='root', password='testtest', db='user')
    ##创建数据库游标
    cursor = conn1.cursor()
    sql_up = "update user.us_unite_examqualify  SET matchingStatus = 0 where ShenFenZH ='500108201601013188';"
    cursor.execute(sql_up)
    data = cursor.fetchone()
    conn1.commit()
    conn1.close()
    print('修改考生资格库状态为未匹配')


