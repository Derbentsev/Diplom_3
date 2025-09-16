from selenium.webdriver.common.by import By


class BasePageLocators:
    CONSTRUCTOR_HEADER_BUTTON_LOCATOR = (By.XPATH, '//p[text()="Конструктор"]')

    ORDERS_HEADER_BUTTON_LOCATOR = (
        By.XPATH,
        '//p[contains(@class, "AppHeader") and text()="Лента Заказов"]'
    )

    PERSONAL_ACCOUNT_BUTTON_LOCATOR = (By.XPATH, '//p[text()="Личный Кабинет"]')
