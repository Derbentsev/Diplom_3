import allure

from seletools.actions import drag_and_drop

from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@allure.suite('Базовая страница')
class BasePage:
    def __init__(self, web_driver: webdriver.Remote):
        self.driver = web_driver


    @allure.step('Нажимаем на элемент')
    def click_on_element(self, locator):
        WebDriverWait(self.driver, 8).until(
            EC.element_to_be_clickable(locator)
        ).click()


    @allure.step('Ожидаем появление элемента')
    def wait_element_displayed(self, locator):
        return WebDriverWait(self.driver, 8).until(
            EC.visibility_of_element_located(locator)
        ).is_displayed()


    @allure.step('Ожидаем исчезновение элемента')
    def wait_element_invisibility(self, locator):
        try:
            return WebDriverWait(self.driver, 5).until(
                EC.invisibility_of_element_located(locator)
            )
        except:
            return None


    @allure.step('Находим элемент')
    def find_element(self, locator):
        return WebDriverWait(self.driver, 8).until(
            EC.visibility_of_element_located(locator)
        )


    @allure.step('Заполняем поле')
    def send_keys(self, locator, text):
        WebDriverWait(self.driver, 8).until(
            EC.visibility_of_element_located(locator)
        ).send_keys(text)


    @allure.step('Перетаскиваем элемент')
    def drag_and_drop_element(self, locator_from, locator_to):
        element_source = self.find_element(locator_from)
        element_target = self.find_element(locator_to)        
        drag_and_drop(self.driver, element_source, element_target)


    @allure.step('Ожидаем появления текста в элементе')
    def wait_text_in_element(self, element_locator, text):
        return WebDriverWait(self.driver, 15).until(
            EC.text_to_be_present_in_element(element_locator, text)
        )
    

    def wait_text_to_change(self, locator, original_text):
        return WebDriverWait(self.driver, 10).until(
            lambda driver: driver.find_element(*locator).text != original_text
        )


    # Подсветка элемента желтым
    def set_element_color(web_driver: webdriver.Remote, element_target):
        web_driver.execute_script(
            "arguments[0].setAttribute('style', arguments[1]);",
            element_target,
            "border: 3px solid red; background-color: yellow;"
        )
