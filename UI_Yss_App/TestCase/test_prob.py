# -*- coding: utf-8 -*-
# @Time : 2021/4/6 9:30
# @Author : dujun
# @describe : 录取概率
# @File : test_prob.py
import allure


class TestProb:

    def setup_class(self):
        pass

    def teardown_class(self):
        pass

    @allure.story('概率')
    def test_pre(self, mainView):
        mainView.probButton()
