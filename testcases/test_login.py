from pageObject.LoginPage import LoginPage
from testData.loginData import LoginData
from utilities.BaseClass import BaseClass
import pytest
from selenium import webdriver


class Login(BaseClass):
    def test_login(self, getData):
        log = self.getLogger()
        loginPage = LoginPage(self.driver)
        log.info("Dang nhap")
        loginPage.getUsername().send_keys(getData["username"])
        loginPage.getPassword().send_keys(getData["password"])
        loginPage.getSubmit().click()
        alertText = loginPage.getSuccessMessage().text
        assert ("Dang nhap thanh cong" in alertText)
        self.driver.refresh()

    @pytest.fixture(params=LoginData.getLoginData("maint"))
    def getData(self, request):
        return request.params
