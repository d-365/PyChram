from selenium.webdriver.support.wait import WebDriverWait
from selenium import webdriver


class BasePage(object):
    ##driver
    def __init__(self, driver):
        self.driver = driver

    ##打开浏览器
    def get(self, url):
        self.driver.get(url)

    ##Xpath定位
    def By_Xpath(self, element=None, OverText=None):
        return WebDriverWait(self.driver, 6, 0.5).until(lambda X: self.driver.find_element_by_xpath(element), OverText)

    ##Link_Text 定位
    def By_Text(self, element=None, OverText=None):
        return WebDriverWait(self.driver, 6, 0.5).until(lambda X: self.driver.find_element_by_link_text(element),
                                                        OverText)

    ##ID 定位
    def By_ID(self,element=None,OverText=None):
        return WebDriverWait(self.driver,6,0.5).until(lambda X: self.driver.find_element_by_id(element),OverText)

    ##partial_link_text定位
    def By_partial_link_tex(self, element=None, OverText=None):
        return WebDriverWait(self.driver, 6, 0.5).until(
            lambda X: self.driver.find_element_by_partial_link_text(element),
            OverText)

    ##Class_Name定位
    def ByClass_Name(self, element=None, OverText=None):
        return WebDriverWait(self.driver, 6, 0.5).until(lambda X: self.driver.find_element_by_class_name(element),
                                                        OverText)

    ##By_Name
    def By_Name(self, element=None, OverText=None):
        return WebDriverWait(self.driver, 6, 0.5).until(lambda X: self.driver.find_element_by_name(element), OverText)
