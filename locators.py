from selenium.webdriver.common.by import By

class Locators:
    # Главная
    MAIN_LOGIN_BUTTON = (By.XPATH, "//button[text()='Войти в аккаунт']")
    MAIN_PERSONAL_BUTTON = (By.XPATH, "//a[@href='/account']")

    # Логин
    LOGIN_EMAIL = (By.ID, "email")
    LOGIN_PASSWORD = (By.ID, "password")
    LOGIN_BUTTON = (By.XPATH, "//button[text()='Войти']")
    REGISTER_LINK = (By.LINK_TEXT, "Зарегистрироваться")
    FORGOT_LINK = (By.LINK_TEXT, "Восстановить пароль")
    LOGIN_FROM_REG = (By.LINK_TEXT, "Войти")

    # Регистрация
    REG_NAME = (By.ID, "name")
    REG_EMAIL = (By.ID, "email")
    REG_PASSWORD = (By.ID, "password")
    REG_BUTTON = (By.XPATH, "//button[text()='Зарегистрироваться']")
    PASSWORD_ERROR = (By.XPATH, "//p[contains(text(), 'Некорректный пароль')]")

    # Личный кабинет
    CABINET_CONSTRUCTOR = (By.XPATH, "//a[@href='/']")
    LOGOUT_BUTTON = (By.XPATH, "//button[text()='Выход']")

    # Конструктор
    BUNS_TAB = (By.XPATH, "//span[text()='Булки']")
    SAUCES_TAB = (By.XPATH, "//span[text()='Соусы']")
    FILLINGS_TAB = (By.XPATH, "//span[text()='Начинки']")
