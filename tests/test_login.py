import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from locators import Locators
from urls import URL
from data import Credentials


class TestLogin:

    def test_login_main_button(self, driver):
        driver.get(URL)
        driver.find_element(Locators.MAIN_LOGIN_BUTTON).click()
        driver.find_element(Locators.LOGIN_EMAIL).send_keys(Credentials.TEST_EMAIL)
        driver.find_element(Locators.LOGIN_PASSWORD).send_keys(Credentials.TEST_PASSWORD)
        driver.find_element(Locators.LOGIN_BUTTON).click()
        assert "/account" in driver.current_url

    def test_login_personal_cabinet(self, driver):
        driver.get(URL)
        driver.find_element(Locators.MAIN_PERSONAL_BUTTON).click()
        driver.find_element(Locators.LOGIN_EMAIL).send_keys(Credentials.TEST_EMAIL)
        driver.find_element(Locators.LOGIN_PASSWORD).send_keys(Credentials.TEST_PASSWORD)
        driver.find_element(Locators.LOGIN_BUTTON).click()
        assert "/account" in driver.current_url

    def test_login_from_register(self, driver):
        driver.get(URL)
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(Locators.MAIN_LOGIN_BUTTON)).click()
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(Locators.REGISTER_LINK)).click()
        driver.find_element(Locators.LOGIN_FROM_REG).click()
        driver.find_element(Locators.LOGIN_EMAIL).send_keys(Credentials.TEST_EMAIL)
        driver.find_element(Locators.LOGIN_PASSWORD).send_keys(Credentials.TEST_PASSWORD)
        driver.find_element(Locators.LOGIN_BUTTON).click()
        assert "/account" in driver.current_url

    def test_login_from_forgot_password(self, driver):
        driver.get(URL)
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(Locators.MAIN_LOGIN_BUTTON)).click()
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(Locators.FORGOT_LINK)).click()
        driver.find_element(Locators.LOGIN_BUTTON).click()
        driver.find_element(Locators.LOGIN_EMAIL).send_keys(Credentials.TEST_EMAIL)
        driver.find_element(Locators.LOGIN_PASSWORD).send_keys(Credentials.TEST_PASSWORD)
        driver.find_element(Locators.LOGIN_BUTTON).click()
        assert "/account" in driver.current_url
        #Тесты для проверки различных способов входа в аккаунт