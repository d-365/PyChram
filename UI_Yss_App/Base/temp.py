# -*- coding: utf-8 -*- 
# @Time : 2020/12/21 19:54 
# @Author : dujun
# @describe : describe
# @File : temp.py 

from selenium import webdriver

driver = webdriver.Chrome()

su = driver.find_element_by_xpath('su')
su.send_keys()
