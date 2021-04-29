# -*- coding: utf-8 -*-
# @Time : 2021/4/20 17:12
# @Author : dujun
# @describe : describe
# @File : file.py
from pprint import pprint
import operator

import json_tools

result1 = {
    "jsessionid": 'case',
    "datas": {
        "limit": 15,
        "dataList": [
            {
                "limitNone": True,
                "createdOnStr": "2021-01-09 20:04:02",
            }
        ],
        "pageCount": 10,
    }
}

result2 = {
    "datas": {
        "limit": 15,
        "dataList": [
            {
                "limitNone": True,
                "createdOnStr": "2021-01-09",
            }
        ],
        "pageCount": 10,
    }
}

if __name__ == "__main__":
    r = json_tools.diff(result1, result2)
    if not r:
        print(r)
    else:
        print(r)
        raise AssertionError('json串不一致')
