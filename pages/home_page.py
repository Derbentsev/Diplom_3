import allure

from pages.base_page import BasePage
from locators.home_page_locators import HomePageLocators
from locators.base_page_locators import BasePageLocators


@allure.suite('Главная страница')
class HomePage(BasePage):
    @allure.step('Ожидаем загрузки домашней страницы')
    def wait_home_page_displayed(self):
        return self.wait_element_displayed(HomePageLocators.HEADER_TEXT_LOCATOR)


    @allure.step('Кликаем на кнопку "Конструктор"')
    def click_on_constructor_button(self):
        self.click_on_element(BasePageLocators.CONSTRUCTOR_HEADER_BUTTON_LOCATOR)


    @allure.step('Кликаем на карточку ингредиента')
    def click_on_ingredient_card(self, card_index: int):
        self.click_on_element(HomePageLocators.get_ingredient_card_locator(card_index))


    @allure.step('Ожидаем загрузки карточки ингредиента')
    def wait_ingredient_card_displayed(self):
        return self.wait_element_displayed(HomePageLocators.INGREDIENT_CARD_HEADER_TEXT_LOCATOR)


    @allure.step('Нажимаем на кнопку закрытия карточки ингредиента')
    def cick_on_close_ingredient_card_button(self):
        self.click_on_element(HomePageLocators.INGREDIENT_CARD_WINDOW_CLOSE_BUTTON_LOCATOR)


    @allure.step('Ожидаем исчезновения карточки ингредиента')
    def wait_ingredient_card_invisibility(self):
        return self.wait_element_invisibility(HomePageLocators.INGREDIENT_CARD_WINDOW_CLOSE_BUTTON_LOCATOR)


    @allure.step('Считываем идентификатор заказа')
    def get_order_indentifier_element(self):
        element = self.find_element(HomePageLocators.IDENTIFIER_ORDER_LOCATOR)
        return element
    

    @allure.step('Перетаскиваем ингредиент в поле заказа')
    def drag_and_drop_ingredient(self):
        self.drag_and_drop_element(
            HomePageLocators.get_ingredient_card_locator(1),
            HomePageLocators.BURGER_CONSTRUCTOR_BASKET_LOCATOR)


    @allure.step('Создаем заказ')
    def create_order(self):
        self.drag_and_drop_ingredient()
        self.click_on_element(HomePageLocators.PLACE_AN_ORDER_BUTTON_LOCATOR)


    @allure.step('Считываем счетчик заказов')
    def get_ingredient_counter(self):
        element_counter = self.find_element(HomePageLocators.get_ingredient_counter_locator(1))
        return int(element_counter.text)


    @allure.step('Закрываем окно оформленного заказа')
    def close_popup_order_window(self):        
        self.click_on_element(HomePageLocators.CLOSE_ORDER_POPUP_WINDOW_LOCATOR)
        self.wait_element_invisibility(HomePageLocators.CLOSE_ORDER_POPUP_WINDOW_LOCATOR)


    @allure.step('Ожидаем исчезновения overlay на домашней странице')
    def wait_overlay_invisibility(self):
        self.wait_element_invisibility(HomePageLocators.OVERLAY_LOCATOR)


    @allure.step('Ожидаем появления номера заказа во всплывающем окне')
    def wait_change_order_number_in_popup(self, order_number):
        self.wait_text_to_change(
            HomePageLocators.IDENTIFIER_ORDER_LOCATOR,
            order_number
        )
    