from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from locators import *


class TestConstructorTabs:
    ("tab_locator, tab_name", [
        (BUNS_TAB, "Булки"),
        (SAUCES_TAB, "Соусы"),
        (FILLINGS_TAB, "Начинки"),
    ])
    def test_constructor_tab_switching(self, logged_user, driver, tab_locator, tab_name):
        
        driver.find_element(CABINET_CONSTRUCTOR).click()
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(BUNS_TAB))
        
        
        driver.find_element(tab_locator).click()
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located(tab_locator))
        
        
        assert driver.find_element(tab_locator).is_displayed(), f"Вкладка '{tab_name}' не отображается"
        assert driver.find_element(tab_locator).get_attribute("class").find("tab_tab_active") != -1, \
            f"Вкладка '{tab_name}' не активна"