# -*- coding: utf-8 -*-
# @Time : 2020/12/11 10:23
# @Author : dujun
# @describe : 用例加载执行界面
# @File : test_run.py
import os
import shutil
import time
import pytest


class Test_run:

    def test_Run(self, logger):
        # 执行测试用例
        try:
            # logger.adbLogCat()
            pytest.main(['-s', r'TestCase', '--alluredir', './result/'])
        except:
            pass

    ##关闭driver
    @pytest.mark.run(order=-1)
    def test_teardown(self, driver, logger):
        try:
            ##killadb服务
            # logger.kill_adbServer()

            time.sleep(10)
            driver.quit()

            ##生成xml格式测试报告
            os.system('allure generate ./result/ -o ./report/ --clean')
            ##删除allure生成的临时文件
            resultPath = os.path.join(os.path.dirname(__file__), 'result')
            if os.path.exists(resultPath):
                shutil.rmtree(resultPath)
            else:
                os.makedirs(resultPath)
        except:
            pass
