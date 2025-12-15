import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import *
from conftest import URL, TEST_EMAIL, TEST_PASSWORD

@pytest.mark.profile
def test_profile_transitions_and_logout(driver):
    # Вход
    driver.get(URL)
    driver.find_element(MAIN_LOGIN_BUTTON).click()
    driver.find_element(LOGIN_EMAIL).send_keys(TEST_EMAIL)
    driver.find_element(LOGIN_PASSWORD).send_keys(TEST_PASSWORD)
    driver.find_element(LOGIN_BUTTON).click()
    assert "/account" in driver.current_url
    
    # Переход в конструктор
    driver.find_element(CABINET_CONSTRUCTOR).click()
    WebDriverWait(driver, 10).until(lambda d: URL in d.current_url)
    assert URL in driver.current_url
    
    # Выход
    driver.find_element(MAIN_PERSONAL_BUTTON).click()
    driver.find_element(LOGOUT_BUTTON).click()
    WebDriverWait(driver, 10).until(lambda d: "/login" in d.current_url)
    assert "/login" in driver.current_url