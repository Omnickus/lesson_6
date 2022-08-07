import pytest
import os

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromiumService
from selenium.webdriver.firefox.service import Service as FFService


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="firefox")
    parser.addoption("--url", action="store", default="http://localhost:80")
    parser.addoption("--drivers", action="store", default=os.path.expanduser("~/drivers"))
    parser.addoption("--executor", action="store", default="172.29.39.82")


@pytest.fixture
def browser(request):
    # Сбор параметров запуска для pytest
    browser = request.config.getoption("--browser")
    url = request.config.getoption("--url")
    drivers = request.config.getoption("--drivers")
    executor = request.config.getoption("--executor")

    # if browser == "chrome":
    #     # В selenium 4 рекомендуют использование такого подхода
    #     service = ChromiumService(executable_path=drivers + "/chromedriver")
    #     try:
    #         driver = webdriver.Chrome(service=service)
    #     except Exception as e:
    #         options = webdriver.ChromeOptions()
    #         driver_path = drivers + "/chromedriver"
    #         driver = webdriver.Chrome(  
    #                                 executable_path = driver_path,
    #                                 options = options
    #                             )
    # elif browser == "firefox":
    #     service = FFService(executable_path=drivers + "/geckodriver")
    #     driver = webdriver.Firefox(service=service)
    # elif browser == "opera":
    #     driver = webdriver.Opera(executable_path=drivers + "/operadriver")
    # else:
    #     driver = webdriver.Safari()

    driver = webdriver.Remote(
        command_executor=f"http://{executor}:4444/wd/hub",
        desired_capabilities= {"browserName" : browser}
    )

    driver.maximize_window()

    request.addfinalizer(driver.close)

    driver.get(url)
    driver.url = url

    return driver
