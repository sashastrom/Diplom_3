import allure
import pytest
from selenium.webdriver.chrome import webdriver
from selenium.webdriver.firefox import webdriver
from selenium import webdriver
from data.urls import Urls
from pages import AllWorkingPages
from web_locators import UsedElements


@allure.step('Браузеры Chrome & Firefox')
@pytest.fixture(params=['chrome', 'firefox'])
def set_up_driver(request):

    if request.param == 'chrome':
        options = webdriver.ChromeOptions()
        driver = webdriver.Chrome(options=options)
        driver.maximize_window()

    elif request.param == 'firefox':
        options = webdriver.FirefoxOptions()
        driver = webdriver.Firefox(options=options)
        driver.set_window_size(1920, 1080)

    driver.get(Urls.main_url)
    yield driver
    driver.quit()

@pytest.fixture(scope='function')
def pages(set_up_driver):
    driver = set_up_driver
    pages = AllWorkingPages(driver, UsedElements())
    return pages

@pytest.fixture(scope='function')
def login(pages):
    pages.login()