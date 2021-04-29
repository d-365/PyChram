from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.select import Select
import random, time
import os


class TestStu:
    driver = webdriver.Chrome()
    login_url = 'http://user.51bm.net.cn/login'
    password = ['Test1234']
    list_wenTi = ['父母手机号码是多少', '爸爸的姓名是什么', '妈妈的姓名是什么', '我最喜欢的体育运动是什么', '我最喜欢的歌曲是哪一首',
                  '我最崇拜的偶像是谁', '我最喜欢的一本书是什么']
    list_answer = ['17637898368', '杜军', '杨勤', '羽毛球和运动', '大海', '周杰伦', '平凡的世界']
    shenFenZH_Stu = ['500108201601019862', '500108201601013188']
    stu_phone = ['18074290708', '18074291213']
    ShenFen_Photo = r'D:\pythonProject\UI_exercise\dujun.jpg'

    def test_register(self):
        self.driver.get(self.login_url)
        ##注册按钮+隐式等待
        register_button = WebDriverWait(self.driver, 10, 0.5).until(
            lambda X: self.driver.find_element_by_link_text('考生注册'), '未找到考试注册按钮')
        register_button.click()
        ##继续注册按钮
        J_goon_register = WebDriverWait(self.driver, 10, 0.5).until(
            lambda X: self.driver.find_element_by_id("J_goon_register"), '未找到继续注册按钮')
        J_goon_register.click()
        ##同意协议按钮
        agree_protocol = WebDriverWait(self.driver, 10, 0, 0.5).until(
            lambda X: self.driver.find_element_by_id('jReadProtocolLabel'), '未找到同意协议按钮')
        agree_protocol.click()



        ##登录密码
        yongHuKL = self.driver.find_element_by_id('yongHuKL')
        yongHuKL.send_keys(self.password[0])
        ##确认密码agginYongHuKL
        agginYongHuKL = self.driver.find_element_by_id("agginYongHuKL")
        agginYongHuKL.send_keys(self.password[0])
        ##安全问题下拉框wenTi
        ##生成随机整数
        random_int = random.randint(0, 6)
        wenTi = self.driver.find_element_by_id('wenTi')
        Select(wenTi).select_by_index(random_int)
        ##安全问题答案
        daAn = self.driver.find_element_by_name('daAn')
        daAn.send_keys(self.list_answer[random_int])
        ##输入验证码authCode
        authCode = self.driver.find_element_by_name('authCode')
        authCode.send_keys('YxYss')
        # ##查看协议J_look_protocol
        # J_look_protocol = self.driver.find_element_by_id('J_look_protocol')
        # J_look_protocol.click()
        # #同意注册协议
        # agree_protocol.click()
        ##进入注册页面,上传证件照片
        jUploadCard = WebDriverWait(self.driver, 10, 0, 0.5).until(
            lambda X: self.driver.find_element_by_id('jUploadCard'), 'jUploadCard不存在')
        jUploadCard.click()
        os.system(r"C:\Users\Administrator\Desktop\upload_file.exe")
        ##注册按钮jSubmit
        # jSubmit = self.driver.find_element_by_id('jSubmit')
        # jSubmit.click()

        print('考生注册成功')
