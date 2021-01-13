import requests
import random
import unittest


##管理员登录
class TestManage(unittest.TestCase):
    ##登录接口
    login_url = "http://user.51bm.net.cn/login"
    create_UserUrl = "http://user.51bm.net.cn/auth/admin/user/saveUser.htm"
    headers = {
        "Content-Type": "application/x-www-form-urlencoded",
        "charset": "utf-8",
        "X - Requested - With": "XMLHttpRequest",
        "platformType": "1",
        "udid": "divice-liker365",
        "tkn": "yx001"
    }

    ##登录系统管理员账号
    def Testmanage_login(self):
        datas = {
            "loginName": "haitun",
            "password": "Test1234"
        }
        response = requests.post(url=self.login_url, headers=self.headers, data=datas)
        self.ticket = response.json()['ticket']
        print("系统管理员登录成功", response.json())
        return self.ticket

    ##创建考生
    def TestCreate_stu(self):
        self.list_data = []
        for datas in range(2, 10):
            str_datas = str(datas)
            username = "shengfen" + str_datas
            self.list_data.append(username)

        for list_ele in range(0, len(self.list_data)):
            headers_ticket = {
                "Content-Type": "application/x-www-form-urlencoded",
                "charset": "utf-8",
                "X - Requested - With": "XMLHttpRequest",
                "platformType": "1",
                "udid": "divice-liker365",
                "tkn": "yx001",
            }
            data_user = {
                "yongHuMing": self.list_data[list_ele],
                "yongHuKL": "Test1234",
                "agginYongHuKL": "Test1234",
                "yongHuLB": "100",
                "ticket": self.ticket
            }
            response = requests.post(url=self.create_UserUrl, headers=headers_ticket, data=data_user)
            print('创建考生成功', response.json())
        return self.list_data


run = TestManage()
run.Testmanage_login()
run.TestCreate_stu()
print('生成的考生' + run.list_data)
