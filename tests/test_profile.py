import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from locators import Locators
from urls import URL
from data import Credentials


class TestProfile:

    def test_profile_transitions_and_logout(self, driver):
        # Вход
        driver.get(URL)
        driver.find_element(Locators.MAIN_LOGIN_BUTTON).click()
        driver.find_element(Locators.LOGIN_EMAIL).send_keys(Credentials.TEST_EMAIL)
        driver.find_element(Locators.LOGIN_PASSWORD).send_keys(Credentials.TEST_PASSWORD)
        driver.find_element(Locators.LOGIN_BUTTON).click()
        assert "/account" in driver.current_url

        # Переход в конструктор
        driver.find_element(Locators.CABINET_CONSTRUCTOR).click()
        WebDriverWait(driver, 10).until(lambda d: URL in d.current_url)
        assert URL in driver.current_url

        # Выход
        driver.find_element(Locators.MAIN_PERSONAL_BUTTON).click()
        driver.find_element(Locators.LOGOUT_BUTTON).click()
        WebDriverWait(driver, 10).until(lambda d: "/login" in d.current_url)
        assert "/login" in driver.current_url