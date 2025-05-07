#写测试用例的文件
import allure
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


from pom.Create_Documents_Page import create_document_page
from pom.login_page import LoginPage
from pom.Document_page import document_page
from bases.base_page import  *
from common.read_excel_util import  *
import allure
import  pytest
@allure.epic("测试项目名称：报销系统-单据用例")
class Test_saas:
    def test_login(self,all_case_fixture):
        LoginPage(all_case_fixture).loginpage("15633870743", "Quanli0028")

    def test_create(self,all_case_fixture):
        #定制allure测试报告
        allure.dynamic.feature("模块名称：单据模板")
        allure.dynamic.story("页面名称：选择模板")
        allure.dynamic.title("用例名称：搜索模板名称")
        Test_saas().test_login(all_case_fixture)
        # LoginPage(all_case_fixture).loginpage("15633870743", "Quanli0028")
        create_document_page(all_case_fixture).create_document(document_name="日常报销单")


    @pytest.mark.parametrize("caseinfo",read_excel_to_login(r"C:\Program Files\pycharmproject\testcases01\login_caseinfo.xlsx","单据信息"))
    def test_document(self,all_case_fixture,caseinfo):
        allure.dynamic.feature("模块名称：单据页面")
        allure.dynamic.story("页面名称：填写单据信息")
        allure.dynamic.title("用例名称：填写标题，部门")
        Test_saas().test_create(all_case_fixture)
        document_page(all_case_fixture).document_info(caseinfo["标题"],caseinfo["提交人"],caseinfo["报销部门"])










        #打开菜单
        # menu=WebDriverWait(driver,20,2).until(EC.visibility_of_element_located((By.XPATH,"//div[@id='immersivebtn_wrapper']/span")))
        # menu.click()
        #
        # #点击我的单据
        # driver.find_element(By.XPATH,"//ul[@id='layout5-menu-wrap-new']/li[2]").click()
        #
        # #点击新建
        # driver.find_element(By.XPATH,"//span[text()='新建']").click()
        #
        # #搜索框输入小圈
        # search=WebDriverWait(driver,10,2).until(EC.visibility_of_element_located((By.CSS_SELECTOR,".ant-input")))
        # search.send_keys("小圈报销")
        #
        # search.send_keys(Keys.RETURN)
        #
        #
        # #进入单据模板
        # driver.find_element(By.XPATH,"//*[@id='changeTemplateModal']/div[3]/div[2]/div/div/div[2]/div/div/div[2]").click()
        # time.sleep(5)
























    # def test_login(self):
    #     driver = webdriver.Chrome()
    #     driver.get('https://app.ekuaibao.com/web/app.html#/login')
    #     time.sleep(3)
    #     #填写登录信息，登录
    #     cellphone=driver.find_element(By.XPATH,"//*[@id='app']/div/div/div/div[2]/div[2]/div[2]/form/div[1]/div/div/div/div/span/span/span/input")
    #     cellphone.send_keys("15633870743")
    #     #输入密码
    #     driver.find_element(By.XPATH,"//input[@type='password']").send_keys("Quanli0028")
    #     time.sleep(2)
    #     #点击同意协议
    #     driver.find_element(By.XPATH,"//*[@id='app']/div/div/div/div[2]/div[2]/div[2]/form/div[5]/label/span/input").click()
    #     time.sleep(1)
    #     #登录
    #     driver.find_element(By.XPATH,"//button[@class='ant-btn t-button ant-btn-primary ant-btn-block']").click()
    #     time.sleep(2)
    #     #定位容器
    #     scroll_container=driver.find_element(By.CSS_SELECTOR,".eui-list")
    #     # 将焦点切换到容器
    #     scroll_container.click()
    #     time.sleep(2)
    #
    #     # 模拟 PAGE_DOWN 按键滚动
    #     scroll_container.send_keys(Keys.PAGE_DOWN)
    #     time.sleep(2)
    #
    #     #选择企业
    #     driver.find_element(By.XPATH,"//*[@id='app']/div/div/div/div[2]/div[1]/div[3]/div/div/div/div/ul/li[12]/div/div/span[2]").click()
    #     # wait=WebDriverWait(driver,2).until(EC.visibility_of_element_located(tag1))
    #     time.sleep(1)
    #     #确认进入企业
    #     driver.find_element(By.XPATH,"//*[@id='app']/div/div/div/div[2]/div[2]/button[2]").click()
    #     # time.sleep(20)









#
# #打开菜单
# menu=WebDriverWait(driver,20,2).until(EC.visibility_of_element_located((By.XPATH,"//div[@id='immersivebtn_wrapper']/span")))
# menu.click()
# time.sleep(2)
# #点击我的单据
# driver.find_element(By.XPATH,"//ul[@id='layout5-menu-wrap-new']/li[2]").click()
# time.sleep(2)
# #点击新建
# driver.find_element(By.XPATH,"//span[text()='新建']").click()
# # time.sleep(2)
# #搜索框输入小圈
# search=WebDriverWait(driver,10,2).until(EC.visibility_of_element_located((By.CSS_SELECTOR,".ant-input")))
# search.send_keys("小圈报销")
# time.sleep(3)
# search.send_keys(Keys.RETURN)
# time.sleep(1)
#
# #进入单据模板
# driver.find_element(By.XPATH,"//*[@id='changeTemplateModal']/div[3]/div[2]/div/div/div[2]/div/div/div[2]").click()
# time.sleep(5)



