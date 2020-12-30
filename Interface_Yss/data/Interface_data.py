# -*- coding: utf-8 -*- 
# @Time : 2020/12/17 16:07 
# @Author : dujun
# @describe : 用户登录数据
# @File : Interface_data.py


##请求头
header = {
    "platformType": "2",
    "udid": "1519fbbacd907027e734fbf8b17b2a7a",
    "tkn": "yx001",
    "yks": "1"
}

##后台登录接口
login_url = "http://user.51bm.net.cn/login"

##系统管理员创建考生接口
Create_StuUrl = "http://user.51bm.net.cn/auth/admin/user/saveUser.htm"

##App考生登录接口
stu_loginUrl = 'http://192.168.18.202:10100/login'

##考生账号
stu_Base_data = {
    "loginName": 'HAITUN13',
    'password': 'Csk001'
}
