from bases.base_page import *






class document_page(Base_Page):
    title="//*[@id='title']/div/div[2]/div/span/span/input"
    submitter="//*[@id='submitterId']/div/div[2]/div/span/div"
    search="//*[@id='web']/div[7]/div/div[2]/div/div[2]/div[1]/div/div[2]/div/div/div[1]/div/div[1]/span/input"
    search_click="//*[@id='textDomId']"
    search_click_re="//*[@id='web']/div[7]/div/div[2]/div/div[2]/div[1]/div/div[3]/div[2]/div[2]/button"
    confirm_re="//button[@class='eui-button eui-button-primary-default eui-button-middle eui-button-shape-default']"
    expensedate="//*[@id='expenseDate']"
    date=f"//table[@class='eui-picker-content']/tbody/tr[2]/td[@title='2025-05-09']"
    expensedepartment="//input[@id='rc_select_3']"
    payee="//*[@id='payeeId']/div/div[2]/div/span/div/div/div"
    huadong="//div[@id='bill-info-editable-container']"

    def document_info(self,te_title,te_people,te_department):

        self.find_els(self.title).send_keys(te_title)
        # self.find_els(self.submitter).click()
        # self.find_els(self.search).send_keys(te_people)
        # self.find_els(self.search_click).click()
        # self.find_els(self.search_click_re).click()
        self.find_els(self.expensedate).click()
        self.find_els(self.date).click()
        self.find_els(self.huadong).click()
        self.find_els(self.expensedepartment).click()
        self.select(self.find_els(self.expensedepartment),te_department)
        # self.find_els(self.confirm_re).click()