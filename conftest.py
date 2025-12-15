import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from locators import *

URL = "https://stellarburgers.education-services.ru/"
TEST_EMAIL = "britvina_36@yandex.ru"
TEST_PASSWORD = "12345678"

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
    driver.get(URL)
    driver.find_element(MAIN_LOGIN_BUTTON).click()
    driver.find_element(LOGIN_EMAIL).send_keys(TEST_EMAIL)
    driver.find_element(LOGIN_PASSWORD).send_keys(TEST_PASSWORD)
    driver.find_element(LOGIN_BUTTON).click()
    WebDriverWait(driver, 10).until(lambda d: "/account" in d.current_url)
    return {"email": TEST_EMAIL, "password": TEST_PASSWORD}