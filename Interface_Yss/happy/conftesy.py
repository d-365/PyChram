# -*- coding: utf-8 -*-
# @Time : 2021/4/26 11:00
# @Author : dujun
# @describe : describe
# @File : conftesy.py.py
import pytest


@pytest.fixture(scope='session')
def data():
    phone = 18397858213
    return phone
