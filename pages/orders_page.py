import time

from pages.base_page import BasePage

from locators.orders_page_locators import OrdersPageLocators
from locators.base_page_locators import BasePageLocators


class OrdersPage(BasePage):
    def wait_orders_page_displayed(self):
        return self.wait_element_displayed(OrdersPageLocators.HEADER_TEXT_LOCATOR)


    def click_orders_button(self):
        self.click_on_element(BasePageLocators.ORDERS_HEADER_BUTTON_LOCATOR)


    def get_order_in_work_counter(self, order_number):
        element = self.find_element(OrdersPageLocators.get_order_in_work_locator(order_number))
        return element.text


    def get_orders_ready_all_time_counter(self):
        element = self.find_element(OrdersPageLocators.get_orders_ready_all_time_counter_locator())
        return element.text


    def get_orders_ready_today_counter(self):
        element = self.find_element(OrdersPageLocators.get_orders__ready_today_counter_locator())
        return element.text
