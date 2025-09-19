from selenium.webdriver.common.by import By


class AccountLocators:
    EMAIL_INPUT_LOCATOR = (By.NAME, 'name')
    PASSWORD_INPUT_LOCATOR = (By.NAME, 'Пароль')
    LOGIN_BUTTON_LOCATOR = (By.XPATH, '//button[text()="Войти"]')
