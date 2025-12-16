import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from locators import Locators
from helper import make_user, make_email
from urls import URL


class TestRegistration:

    def test_good_registration(self, driver):
        driver.get(URL)
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(Locators.MAIN_LOGIN_BUTTON)).click()
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(Locators.REGISTER_LINK)).click()

        user = make_user()
        driver.find_element(Locators.REG_NAME).send_keys(user['name'])
        driver.find_element(Locators.REG_EMAIL).send_keys(user['email'])
        driver.find_element(Locators.REG_PASSWORD).send_keys(user['password'])
        driver.find_element(Locators.REG_BUTTON).click()

        WebDriverWait(driver, 10).until(lambda d: "/account" in d.current_url)
        assert "/account" in driver.current_url

    def test_bad_password(self, driver):
        driver.get(URL)
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(Locators.MAIN_LOGIN_BUTTON)).click()
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(Locators.REGISTER_LINK)).click()
        driver.find_element(Locators.REG_NAME).send_keys("Тест")
        driver.find_element(Locators.REG_EMAIL).send_keys(make_email())
        driver.find_element(Locators.REG_PASSWORD).send_keys("123")
        driver.find_element(Locators.REG_BUTTON).click()

        error = WebDriverWait(driver, 10).until(EC.visibility_of_element_located(Locators.PASSWORD_ERROR))
        assert "Некорректный пароль" in error.text