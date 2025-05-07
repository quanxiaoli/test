#pom模式，主要负责操作行为，类代表页面，属性代表元素，方法代表操作的行为，比如点击
from selenium.webdriver import Keys

from bases.base_page import *


class LoginPage(Base_Page):
    #写登录页面的操作元素
    cellphone="//span[@class='ant-input-wrapper ant-input-group']/input"
    password="//input[@type='password']"
    argee="//span[@class='ant-checkbox']"
    clc="//button[@class='ant-btn t-button ant-btn-primary ant-btn-block']"
    # scroll_container=".eui-list"
    select="//span[@class='corp-name-span']"
    ret="//*[@id='app']/div/div/div/div[2]/div[2]/button[2]"
    def loginpage(self,phone,passwords):
        self.find_els(self.cellphone).send_keys(phone)
        self.find_els(self.password).send_keys(passwords)
        self.find_els(self.argee).click()
        self.find_els(self.clc).click()
        # self.find_els(self.scroll_container).click()
        self.find_els(self.select).click()
        self.find_els(self.ret).click()


