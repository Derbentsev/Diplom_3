import time

from pages.base_page import BasePage
from locators.home_page_locators import HomePageLocators
from locators.base_page_locators import BasePageLocators


class HomePage(BasePage):
    def wait_home_page_displayed(self):
        return self.wait_element_displayed(HomePageLocators.HEADER_TEXT_LOCATOR)


    def click_on_constructor_button(self):
        self.click_on_element(BasePageLocators.CONSTRUCTOR_HEADER_BUTTON_LOCATOR)


    def click_on_ingredient_card(self, card_index: int):
        self.click_on_element(HomePageLocators.get_ingredient_card_locator(card_index))


    def wait_ingredient_card_displayed(self):
        return self.wait_element_displayed(HomePageLocators.INGREDIENT_CARD_HEADER_TEXT_LOCATOR)


    def cick_on_close_ingredient_card_button(self):
        self.click_on_element(HomePageLocators.INGREDIENT_CARD_WINDOW_CLOSE_BUTTON_LOCATOR)


    def wait_ingredient_card_invisibility(self):
        return self.wait_element_invisibility(HomePageLocators.INGREDIENT_CARD_WINDOW_CLOSE_BUTTON_LOCATOR)

    
    def get_order_indentifier(self):
        element = self.find_element(HomePageLocators.IDENTIFIER_ORDER_LOCATOR)
        return element.text
    

    def drag_and_drop_ingredient(self):
        self.drag_and_drop_element(
            HomePageLocators.get_ingredient_card_locator(1),
            HomePageLocators.BURGER_CONSTRUCTOR_BASKET_LOCATOR)


    def create_order(self):
        self.drag_and_drop_ingredient()
        self.click_on_element(HomePageLocators.PLACE_AN_ORDER_BUTTON_LOCATOR)
        time.sleep(5)


    def get_ingredient_counter(self):
        element_counter = self.find_element(HomePageLocators.get_ingredient_counter_locator(1))
        return int(element_counter.text)


    def close_popup_order_window(self):        
        self.click_on_element(HomePageLocators.CLOSE_ORDER_POPUP_WINDOW_LOCATOR)


    def wait_overlay_invisibility(self):
        self.wait_element_invisibility(HomePageLocators.OVERLAY_LOCATOR)
        time.sleep(1)
