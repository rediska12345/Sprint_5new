import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import *
from conftest import URL, TEST_EMAIL, TEST_PASSWORD

@pytest.mark.login
def test_login_main_button(driver):
    driver.get(URL)
    driver.find_element(MAIN_LOGIN_BUTTON).click()
    driver.find_element(LOGIN_EMAIL).send_keys(TEST_EMAIL)
    driver.find_element(LOGIN_PASSWORD).send_keys(TEST_PASSWORD)
    driver.find_element(LOGIN_BUTTON).click()
    assert "/account" in driver.current_url

@pytest.mark.login
def test_login_personal_cabinet(driver):
    driver.get(URL)
    driver.find_element(MAIN_PERSONAL_BUTTON).click()
    driver.find_element(LOGIN_EMAIL).send_keys(TEST_EMAIL)
    driver.find_element(LOGIN_PASSWORD).send_keys(TEST_PASSWORD)
    driver.find_element(LOGIN_BUTTON).click()
    assert "/account" in driver.current_url

@pytest.mark.login
def test_login_from_register(driver):
    driver.get(URL)
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable(MAIN_LOGIN_BUTTON)).click()
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable(REGISTER_LINK)).click()
    driver.find_element(LOGIN_FROM_REG).click()
    driver.find_element(LOGIN_EMAIL).send_keys(TEST_EMAIL)
    driver.find_element(LOGIN_PASSWORD).send_keys(TEST_PASSWORD)
    driver.find_element(LOGIN_BUTTON).click()
    assert "/account" in driver.current_url

@pytest.mark.login
def test_login_from_forgot_password(driver):
    driver.get(URL)
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable(MAIN_LOGIN_BUTTON)).click()
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable(FORGOT_LINK)).click()
    driver.find_element(LOGIN_BUTTON).click()
    driver.find_element(LOGIN_EMAIL).send_keys(TEST_EMAIL)
    driver.find_element(LOGIN_PASSWORD).send_keys(TEST_PASSWORD)
    driver.find_element(LOGIN_BUTTON).click()
    assert "/account" in driver.current_url