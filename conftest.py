#写fixture前后置，比如登录，连接数据库等
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options

from pom.login_page import LoginPage



@pytest.fixture(scope="function")
def all_case_fixture():
    print("打开登录页面")
    driver=login()
    yield driver
    time.sleep(5)
    driver.quit()
    print("关闭浏览器")



def login():
    # options = webdriver.ChromeOptions()
    # options.add_argument('--disable-blink-features=AutomationControlled')
    chrome_options = Options()
    chrome_options.add_experimental_option("detach", True)  # 关键参数
    # chrome_options.add_argument('--headless')
    chrome_options.page_load_strategy = "eager"
    chrome_options.add_argument("--disable-dev-shm-usage")
    # 初始化 WebDriver 时传入配置
    driver = webdriver.Chrome(options=chrome_options)
    driver.get('https://app.ekuaibao.com/web/app.html?_=1745474451918&corpId=ogUc2MYUUcc000&accessToken=#/login')

    return driver












    # time.sleep(3)
    # #填写登录信息，登录
    # cellphone=driver.find_element(By.XPATH,"//*[@id='app']/div/div/div/div[2]/div[2]/div[2]/form/div[1]/div/div/div/div/span/span/span/input")
    # cellphone.send_keys("15633870743")
    # #输入密码
    # driver.find_element(By.XPATH,"//input[@type='password']").send_keys("Quanli0028")
    # # time.sleep(2)
    # #点击同意协议
    # driver.find_element(By.XPATH,"//*[@id='app']/div/div/div/div[2]/div[2]/div[2]/form/div[5]/label/span/input").click()
    # time.sleep(3)
    # #登录
    # driver.find_element(By.XPATH,"//button[@class='ant-btn t-button ant-btn-primary ant-btn-block']").click()
    # time.sleep(2)
    # #定位容器
    # scroll_container=driver.find_element(By.CSS_SELECTOR,".eui-list")
    # # 将焦点切换到容器
    # scroll_container.click()
    # time.sleep(2)
    # # 选择企业
    # driver.find_element(By.XPATH,"//*[@id='app']/div/div/div/div[2]/div[1]/div[3]/div/div/div/div/ul/li[12]/div/div/span[2]").click()
    # # wait=WebDriverWait(driver,2).until(EC.visibility_of_element_located(tag1))
    # time.sleep(1)
    # # 确认进入企业
    # driver.find_element(By.XPATH, "//*[@id='app']/div/div/div/div[2]/div[2]/button[2]").click()
    # time.sleep(5)
    # return driver