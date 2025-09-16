from pages.base_page import BasePage
from locators.personal_account_locators import AccountLocators
from locators.base_page_locators import BasePageLocators
from locators.orders_page_locators import OrdersPageLocators
from locators.home_page_locators import HomePageLocators


class AccountPage(BasePage):
    def click_on_personal_account_button(self):
        self.click_on_element(BasePageLocators.PERSONAL_ACCOUNT_BUTTON_LOCATOR)


    def fill_email_input(self, login):
        self.send_keys(AccountLocators.EMAIL_INPUT_LOCATOR, login)

    
    def fill_password_input(self, password):
        self.send_keys(AccountLocators.PASSWORD_INPUT_LOCATOR, password)

    
    def click_login_button(self):
        self.click_on_element(AccountLocators.LOGIN_BUTTON_LOCATOR)


    def wait_login(self):
        self.wait_element_displayed(OrdersPageLocators.PLACE_AN_ORDER_BUTTON_LOCATOR)


    def wait_overlay_invisibility(self):
        self.wait_element_invisibility(HomePageLocators.OVERLAY_LOCATOR)
        

    def user_login(self, login, password):
        self.click_on_personal_account_button()
        self.wait_overlay_invisibility()
        self.fill_email_input(login)
        self.fill_password_input(password)
        self.click_login_button()
        self.wait_element_displayed(HomePageLocators.HEADER_TEXT_LOCATOR)
