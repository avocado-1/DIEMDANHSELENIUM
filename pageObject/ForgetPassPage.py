from selenium.webdriver.common.by import By
from pageObject.LoginPage import LoginPage

class ForgetPassPage:
    def __init__(self, driver):
        self.driver = driver

    email = (By.XPATH, "//input[@id='quenMatKhau_email']")
    submit = (By.XPATH, "//span[contains(text(),'Gửi')]")
    linkText = (By.LINK_TEXT, "Quay lại trang đăng nhập")

    def getEmail(self):
        return self.driver.find_element(*ForgetPassPage.email)

    def getSubmit(self):
        return self.driver.find_element(*ForgetPassPage.submit)

    def getLinkText(self):
        self.driver.find_element(*ForgetPassPage.linkText).click()
        loginPage = LoginPage(self.driver)
        return loginPage
