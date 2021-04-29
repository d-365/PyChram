# -*- coding: utf-8 -*- 
# @Time : 2021/3/11 18:32 
# @Author : dujun
# @describe : describe
# @File : case.py
import base64
import hashlib
import pytest


@pytest.mark.flaky(1)
def md5_base64_byte(string):
    m = hashlib.md5()
    m.update(string.encode('utf-8'))
    # 二进制数据字符串值
    md5_str = m.digest()
    b64_str = base64.b64encode(md5_str)
    print(b64_str.decode('utf-8'))
    return b64_str.decode('utf-8')


@md5_base64_byte()
def md5_base64_hex(string):
    m = hashlib.md5()
    m.update(string.encode('utf-8'))
    # 十六进制数据字符串值
    md5_str = m.hexdigest()
    b64_str = base64.b64encode(md5_str.encode('utf-8'))
    return b64_str.decode('utf-8')


if __name__ == "__main__":
    raw_passWord = 'Test1234'
    cipher = md5_base64_hex(raw_passWord)
    print(cipher)
