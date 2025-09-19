from selenium.webdriver.common.by import By


class OrdersPageLocators:
    HEADER_TEXT_LOCATOR = (By.XPATH, '//h1[text()="Лента заказов"]')


    def get_order_in_work_locator(order_number):
        return (
            By.XPATH,
            f'//ul[contains(@class, "OrderFeed_orderListReady")]/li[text()="{order_number}"]'
        )


    def get_orders_ready_all_time_counter_locator():
        return (
            By.XPATH, 
            '//p[text()="Выполнено за все время:"]/following-sibling::p[contains(@class, "OrderFeed_number")]'
        )


    def get_orders_ready_today_counter_locator():
        return (
            By.XPATH,
            '//p[text()="Выполнено за сегодня:"]/following-sibling::p[contains(@class, "OrderFeed_number")]'
        )
