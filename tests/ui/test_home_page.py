import allure
from selenium import webdriver

from urls.urls import Urls
from pages.home_page import HomePage


@allure.suite('Главная страница')
class TestHomePage:
    @allure.title('Проверяем переход на вкладку "Конструктор"')
    def test_click_on_constructor_button_success(self, web_driver: webdriver.Remote):
        web_driver.get(Urls.ORDERS_PAGE_URL)

        home_page = HomePage(web_driver)
        home_page.wait_overlay_invisibility()
        home_page.click_on_constructor_button()
        home_page.wait_home_page_displayed()
        home_page.wait_overlay_invisibility() 

        assert home_page.wait_home_page_displayed()


    @allure.title('При клике на ингредиент появляется всплывающее окно с деталями')
    def test_click_on_ingredient_success(self, web_driver: webdriver.Remote):
        web_driver.get(Urls.HOME_PAGE_URL)
        
        home_page = HomePage(web_driver)
        home_page.wait_home_page_displayed()
        home_page.wait_overlay_invisibility()
        home_page.click_on_ingredient_card(1)

        assert home_page.wait_ingredient_card_displayed()


    @allure.title('Всплывающее окно карточки ингредиента закрывается кликом по крестику')
    def test_close_order_window_by_click(self, web_driver: webdriver.Remote):
        web_driver.get(Urls.HOME_PAGE_URL)

        home_page = HomePage(web_driver)
        home_page.wait_home_page_displayed()
        home_page.wait_overlay_invisibility()
        home_page.click_on_ingredient_card(1)
        home_page.wait_ingredient_card_displayed()
        home_page.cick_on_close_ingredient_card_button()

        assert home_page.wait_ingredient_card_invisibility()


    @allure.title('При добавлении ингредиента в заказ счётчик этого ингредиента увеличивается')
    def test_add_ingredient_counter_increase_success(self, web_driver: webdriver.Remote):
        web_driver.get(Urls.HOME_PAGE_URL)

        home_page = HomePage(web_driver)
        home_page.wait_home_page_displayed()
        home_page.wait_overlay_invisibility()

        ingredient_counter_before = home_page.get_ingredient_counter()
        home_page.drag_and_drop_ingredient()
        ingredient_counter_after = home_page.get_ingredient_counter()

        assert ingredient_counter_before + 2 == ingredient_counter_after
