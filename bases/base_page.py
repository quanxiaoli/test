#该文件是配置共用的方法，比如定位元素的方法
import time

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as  ex
import logging


class Base_Page:
    log=logging.getLogger(__name__)
    #用于传driver
    def __init__(self, driver):
        self.driver = driver

    #定位一个元素
    def find_els(self,xpath):
        try:
            # self.driver.implicitly_wait(10)
            # ele = self.driver.find_element(By.XPATH, xpath)
            #显性等待
            ele=WebDriverWait(self.driver,20).until(ex.visibility_of_element_located((By.XPATH,xpath)))
            self.log.info("元素定位成功："+xpath)
            return ele
        except Exception as e:
            self.log.error("元素定位失败:"+xpath)
    #定位多个元素
    def find_eles(self,xpath):
        try:
            self.driver.implicitly_wait(10)
            ele_list = self.driver.find_elements(By.XPATH, xpath)
            return ele_list

        except Exception as e:
            print("元素定位失败：" + xpath + "")

    #操作回车
    def find_els_enter(self,find_els):
        find_els.send_keys(Keys.ENTER)

    #confirm弹框点击确认
    def confirm(self):
        self.driver.switch_to.alert.accept()

    #select下拉选择框
    def select(self,find_els,value):
        Select(find_els).select_by_value(value)



