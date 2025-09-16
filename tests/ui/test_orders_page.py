import allure
from selenium import webdriver

from data.data import Data
from urls.urls import Urls

from pages.home_page import HomePage
from pages.orders_page import OrdersPage
from pages.account_page import AccountPage


@allure.suite('Страница заказа')
class TestOrderPage:
    @allure.title('Проверяем переход на вкладку "Лента заказов"')
    def test_click_orders_button_success(self, web_driver: webdriver.Remote):
        web_driver.get(Urls.HOME_PAGE_URL)
        
        home_page = HomePage(web_driver)
        home_page.wait_home_page_displayed()
        home_page.wait_overlay_invisibility()

        orders_page = OrdersPage(web_driver)        
        orders_page.click_orders_button()

        assert orders_page.wait_orders_page_displayed()


    @allure.title('После оформления заказа его номер появляется в разделе "В работе"')
    def test_order_appears_in_progress_section_success(self, web_driver: webdriver.Remote):
        user = Data.USER_ALREADY_EXISTS_DATA
        web_driver.get(Urls.HOME_PAGE_URL)

        home_page = HomePage(web_driver)
        home_page.wait_home_page_displayed()
        home_page.wait_overlay_invisibility()
        
        personal_account_page = AccountPage(web_driver)
        personal_account_page.user_login(user['email'], user['password'])

        home_page.create_order()
        order_number = home_page.get_order_indentifier()
        home_page.close_popup_order_window()
        home_page.wait_overlay_invisibility()

        orders_page = OrdersPage(web_driver)
        orders_page.click_orders_button()
        orders_page.wait_orders_page_displayed()
        order_number_current = orders_page.get_order_in_work_counter(order_number)

        assert str(int(order_number)) == str(int(order_number_current))


    @allure.title('При создании нового заказа счётчик "Выполнено за всё время" увеличивается')
    def test_order_counter_all_time_increases_success(self, web_driver: webdriver.Remote):
        web_driver.get(Urls.HOME_PAGE_URL)
        user = Data.USER_ALREADY_EXISTS_DATA

        home_page = HomePage(web_driver)
        home_page.wait_home_page_displayed()
        home_page.wait_overlay_invisibility()

        personal_account_page = AccountPage(web_driver)
        personal_account_page.user_login(user['email'], user['password'])

        orders_page = OrdersPage(web_driver)
        orders_page.click_orders_button()
        orders_page.wait_orders_page_displayed()
        orders_counter_before = orders_page.get_orders_ready_all_time_counter()

        home_page.click_on_constructor_button()
        home_page.create_order()
        home_page.close_popup_order_window()
        home_page.wait_overlay_invisibility()
    
        orders_page.click_orders_button()
        orders_page.wait_orders_page_displayed()
        orders_counter_after = orders_page.get_orders_ready_all_time_counter()

        assert int(orders_counter_before) < int(orders_counter_after)


    @allure.title('При создании нового заказа счётчик "Выполнено за сегодня" увеличивается')
    def test_order_counter_today_increases_success(self, web_driver: webdriver.Remote):
        web_driver.get(Urls.HOME_PAGE_URL)
        user = Data.USER_ALREADY_EXISTS_DATA

        home_page = HomePage(web_driver)
        home_page.wait_home_page_displayed()
        home_page.wait_overlay_invisibility()

        personal_account_page = AccountPage(web_driver)
        personal_account_page.user_login(user['email'], user['password'])

        orders_page = OrdersPage(web_driver)
        orders_page.click_orders_button()
        orders_page.wait_orders_page_displayed()
        orders_counter_before = orders_page.get_orders_ready_today_counter()
    
        home_page.click_on_constructor_button()
        home_page.create_order()
        home_page.close_popup_order_window()
        home_page.wait_overlay_invisibility()

        orders_page.click_orders_button()
        orders_page.wait_orders_page_displayed()
        orders_counter_after = orders_page.get_orders_ready_today_counter()

        assert int(orders_counter_before) < int(orders_counter_after)
