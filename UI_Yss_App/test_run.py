# -*- coding: utf-8 -*-
# @Time : 2020/12/11 10:23
# @Author : dujun
# @describe : 用例加载执行界面
# @File : test_run.py

import os
import shutil
import time
import pytest

from UI_Yss_App.Base.driver_config import appium_start, appium_end


class Test_run:

    @staticmethod
    def setup_class():
        appium_start()

    @staticmethod
    def teardown_class():
        appium_end()

    def test_Run(self):
        # 执行测试用例
        # logger.adbLogCat()
        pytest.main(['-s', r'TestCase/test_prob.py'])
        # pytest.main(['-s','-m','runTest',r'TestCase/test_production_appraise.py', '--alluredir', './result/'])

        # # 关闭driver
        # @pytest.mark.run(order=-1)
        # def test_teardown(self, driver):
        #     try:
        #         # killAdb服务
        #         # logger.kill_adbServer()
        #
        #         time.sleep(5)
        #         driver.quit()
        #
        #         # # 生成xml格式测试报告
        #         # os.system('allure generate ./result/ -o ./report/ --clean')
        #         # # 删除allure生成的临时文件
        #         # resultPath = os.path.join(os.path.dirname(__file__), 'result')
        #         # if os.path.exists(resultPath):
        #             shutil.rmtree(resultPath)
        #         # else:
        #         #     os.makedirs(resultPath)
        #     except:
        #         pass

        # def test_run(self):
        #     for desired in desired_process:
        #         desired.start()
        #         pytest.main(['-s', r'TestCase/test_prob.py'])
        #     for desired in desired_process:
        #         desired.join()
