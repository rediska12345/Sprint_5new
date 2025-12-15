import pytest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options

from locators import Locators
from data import Credentials
from urls import *

@pytest.fixture(scope="session")
def driver():
    options = Options()
    options.add_argument("--window-size=1600,900")
    driver = webdriver.Chrome(options=options)
    driver.implicitly_wait(10)
    yield driver
    
    driver.quit()

@pytest.fixture
def logged_user(driver):
    driver.find_element(*Locators.MAIN_LOGIN_BUTTON).click()
    driver.find_element(*Locators.LOGIN_EMAIL).send_keys(Credentials.TEST_EMAIL)
    driver.find_element(*Locators.LOGIN_PASSWORD).send_keys(Credentials.TEST_PASSWORD)
    driver.find_element(*Locators.LOGIN_BUTTON).click()
    WebDriverWait(driver, 10, poll_frequency=0.1).until(lambda d: "/account" in d.current_url)
    return {"email": Credentials.TEST_EMAIL, "password": Credentials.TEST_PASSWORD}
