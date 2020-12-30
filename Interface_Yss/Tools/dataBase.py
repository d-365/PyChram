# -*- coding: utf-8 -*- 
# @Time : 2020/12/28 20:37 
# @Author : dujun
# @describe : 数据库封装
# @File : dataBase.py
import pymysql
import pytest


class TestDataBase:
    def __init__(self):
        ##测试环境
        host = '192.168.18.203'
        port = '3307'
        user = 'root'
        password = 'testtest '
        self.conn = pymysql.connect(host=host, port=port, user=user, password=password)
        self.cursor = self.conn.cursor()

    ##select
    def test_select(self, sql=''):
        try:
            self.cursor.execute(sql)
            self.conn.commit()
        except BaseException:
            self.conn.rollback()


if __name__ == '__main__':
    run = TestDataBase()
    run.test_select("SELECT * from  be_exam_stuvideo  where  baoKaoId ='2628541' ")
