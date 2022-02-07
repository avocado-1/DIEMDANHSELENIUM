from selenium import webdriver
import pytest


driver = None


def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="chrome"
    )


@pytest.fixture(scope="class")
def setup(request):
    global driver
    browser_name = request.config.getoption("browser_name")
    if browser_name == "chrome":
        driver= webdriver.Chrome(executable_path="C:\\Users\\PENGUIN\\Downloads\\chromedriver.exe")
    elif browser_name == "firefox":
        driver = webdriver.Firefox(executable_path="C:\\Users\\PENGUIN\\Downloads\\geckodriver.exe")
    elif browser_name == "IE":
        print("IE driver")
    driver.get("https://diemdanhais.aisenote.com/")
    driver.maximize_window()

    request.cls.driver = driver
    yield
    driver.close()