from selenium.webdriver.common.by import By
from pageObject.HomePage import HomePage
from pageObject.ForgetPassPage import ForgetPassPage


class LoginPage:

    def __init__(self, driver):
        self.driver = driver

    username = (By.ID, "userName")
    password = (By.ID, "password")
    submit = (By.TAG_NAME, "button")
    forgetPass = (By.LINK_TEXT, "Quên mật khẩu")
    successMessage = (By.XPATH, "//body/div[3]/div[1]")

    def getUsername(self):
        return self.driver.find_element(*LoginPage.username)

    def getPassword(self):
        return self.driver.find_element(*LoginPage.password)

    def getSubmit(self):
        self.driver.find_element(*LoginPage.submit).click()
        homePage = HomePage(self.driver)
        return homePage

    def getForgetPass(self):
        self.driver.find_element(*LoginPage.forgetPass).click()
        forgetPassPage = ForgetPassPage(self.driver)
        return forgetPassPage

    def getSuccessMessage(self):
        return self.driver.find_element(*LoginPage.successMessage)
