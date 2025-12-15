import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import Locators
<<<<<<< HEAD
=======
from urls import *
>>>>>>> adbcbcba29dded21b565fc25e01bf28dd00c52bc

class TestConstructorTabs:
    @pytest.mark.parametrize("tab_locator, tab_name", [
        (Locators.BUNS_TAB, "Булки"),
        (Locators.SAUCES_TAB, "Соусы"),
        (Locators.FILLINGS_TAB, "Начинки"),
    ])
    def test_constructor_tab_switching(self, logged_user, driver, tab_locator, tab_name):
<<<<<<< HEAD
        driver.find_element(Locators.CABINET_CONSTRUCTOR).click()
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(Locators.BUNS_TAB))
        
        driver.find_element(tab_locator).click() 
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located(tab_locator))
        
        assert driver.find_element(tab_locator).is_displayed(), f"Вкладка '{tab_name}' не отображается"
        assert "tab_tab_active" in driver.find_element(tab_locator).get_attribute("class"), \
=======
        
        driver.find_element(*Locators.CABINET_CONSTRUCTOR).click()
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(*Locators.BUNS_TAB))
        
        driver.find_element(*tab_locator).click() 
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located(*tab_locator))
        
        assert driver.find_element(*tab_locator).is_displayed(), f"Вкладка '{tab_name}' не отображается"
        assert "tab_tab_active" in driver.find_element(*tab_locator).get_attribute("class"), \
>>>>>>> adbcbcba29dded21b565fc25e01bf28dd00c52bc
            f"Вкладка '{tab_name}' не активна"