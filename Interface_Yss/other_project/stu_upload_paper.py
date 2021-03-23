# -*- coding: utf-8 -*- 
# @Time : 2021/3/4 15:59 
# @Author : dujun
# @describe : 考生端提交专业评测试卷
# @File : stu_upload_paper.py
from Interface_Yss.project.eval import eval_project
import pytest
from Interface_Yss.project.pay import pay_project
from Interface_Yss.project.user import userProject


class TeststuUpload_paper:

    @pytest.fixture(scope='session')
    def evaluation(self):
        evaluation = eval_project(environment='')
        return evaluation

    @pytest.fixture(scope='session')
    def user(self):
        users = userProject(environment='')
        return users

    @pytest.fixture(scope='session')
    def pay(self):
        pays = pay_project(environment='')
        return pays

    def test_run(self, evaluation, user, pay):
        ##yunbao1
        yunbao1 = {
            "teacherId": 2,
            "teacherUserId": 1077111
        }
        ##yunbao2
        yunbao2 = {
            "teacherId": 12,
            "teacherUserId": 1077112
        }

        login_data = {
            "loginName": "haitun60",
            "password": "Csk001"
        }
        stuLogin = user.stuLogin(login_data)
        stuTicket = stuLogin['ticket']
        for i in range(0, 2):
            ##考生上传评画作品
            evalData = {
                "data": str({"m": "",
                             "p": {"teacherId": yunbao2['teacherId'], "teacherUserId": yunbao2['teacherUserId'],
                                   "teacherName": "天美云豹老师", "classId": 1, "className": "美术类", "profId": 1,
                                   "profName": "素描",
                                   "paintUrl": "http://img.artstudent.cn/pr/2021-03-04/cfda71b9fc074d00944d2599416052e9.jpg",
                                   "stuGrade": "其他",
                                   "describe": "专业评测,考生账号%s" % login_data['loginName']
                                   }}),
                'ticket': stuTicket
            }
            eval = evaluation.save_stu_evaluation(evalData)
            evaluationId = eval['datas']['evaluationId']

            ##查询我的折扣
            disData = {
                "data": str({"m": "", "p": {}}),
                "ticket": stuTicket
            }
            discounts = evaluation.query_my_discounts(data=disData)

            ##提交评画订单
            order_data = {
                "data": str({"m": "", "p": {"evaluationId": evaluationId, "teacherId": yunbao2['teacherId'],
                                            "userDiscountsId": ""}}),
                "ticket": stuTicket
            }
            order_re = evaluation.commit_evaluation_order(data=order_data)
            orderId = order_re['datas']['orderId']

            ##调用支付接口完成支付
            payResponse = pay.pay(orderId=orderId)
            print(payResponse)
        print(yunbao2)
