import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import *

@pytest.mark.constructor
def test_constructor_tabs(logged_user, driver):
    # Переход в конструктор
    driver.find_element(CABINET_CONSTRUCTOR).click()
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable(BUNS_TAB))
    
    # Булки
    driver.find_element(BUNS_TAB).click()
    WebDriverWait(driver, 5).until(EC.visibility_of_element_located(BUNS_TAB))
    
    # Соусы
    driver.find_element(SAUCES_TAB).click()
    WebDriverWait(driver, 5).until(EC.visibility_of_element_located(SAUCES_TAB))
    
    # Начинки
    driver.find_element(FILLINGS_TAB).click()
    WebDriverWait(driver, 5).until(EC.visibility_of_element_located(FILLINGS_TAB))