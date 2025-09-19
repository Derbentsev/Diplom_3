import allure

from pages.base_page import BasePage

from locators.orders_page_locators import OrdersPageLocators
from locators.base_page_locators import BasePageLocators


@allure.suite('Страница заказа')
class OrdersPage(BasePage):
    @allure.step('Ожидаем загрузки страницы заказа')
    def wait_orders_page_displayed(self):
        return self.wait_element_displayed(OrdersPageLocators.HEADER_TEXT_LOCATOR)


    @allure.step('Кликаем на кнопку "Заказать"')
    def click_orders_button(self):
        self.click_on_element(BasePageLocators.ORDERS_HEADER_BUTTON_LOCATOR)


    @allure.step('Считываем счетчик заказов "В работе"')
    def get_order_in_work_counter(self, order_number):
        element = self.find_element(
            OrdersPageLocators.get_order_in_work_locator(order_number)
        )
        return element.text


    @allure.step('Считываем счетчик заказов За все время"')
    def get_orders_ready_all_time_counter(self):
        element = self.find_element(
            OrdersPageLocators.get_orders_ready_all_time_counter_locator()
        )
        return element.text


    @allure.step('Считываем счетчик заказов за сегодня"')
    def get_orders_ready_today_counter(self):
        element = self.find_element(
            OrdersPageLocators.get_orders_ready_today_counter_locator()
        )
        return element.text
    

    @allure.step('Ожидаем появления номера заказа в поле "В работе"')
    def wait_text_in_element_orders_count_in_work(self, order_number):
        return self.wait_text_in_element(
            OrdersPageLocators.get_order_in_work_locator(order_number),
            order_number
        )


    @allure.step('Ожидаем увеличение счетчика в поле "Выполнено за всё время"')
    def wait_text_in_element_orders_count_ready_all_time(self):
        pass


    @allure.step('Ожидаем увеличение счетчика в поле Выполнено за сегодня"')
    def wait_text_in_element_orders_count_ready_today(self):
        pass

