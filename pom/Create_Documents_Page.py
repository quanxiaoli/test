from selenium.webdriver import Keys

from bases.base_page import *

class create_document_page(Base_Page):
    menu_1="//*[@id='immersivebtn_wrapper']/span"
    mydocument="//*[@id='layout5-menu-wrap-new']/li[2]/span[2]/span"
    create="//span[text()='新建']"
    input="//*[@id='changeTemplateModal']/div[2]/span/input"
    select="//*[@id='changeTemplateModal']/div[3]/div[2]/div/div/div[2]/div/div/div[2]/span/mark"


    def create_document(self,document_name):
        #点击展开菜单
        self.find_els(self.menu_1).click()
        #点击我的单据
        self.find_els(self.mydocument).click()
        #点击新建
        self.find_els(self.create).click()
        #搜索单据模板
        self.find_els(self.input).send_keys(document_name)
        #搜索之后回车
        self.find_els_enter(self.find_els(self.input))
        #选中模板打开
        self.find_els(self.select).click()