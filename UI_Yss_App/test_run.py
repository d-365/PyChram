# -*- coding: utf-8 -*- 
# @Time : 2020/12/11 10:23 
# @Author : dujun
# @describe : 执行文件
# @File : test_run.py
import pytest


class Test_run:
    try:
        ##App登录
        pytest.main(['-s', r'TestCase\test_LoginPyTest.py'])
    except Exception:
        pass


if __name__ == "__main__":
    run = Test_run()
