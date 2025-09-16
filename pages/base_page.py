from selenium import webdriver
from seletools.actions import drag_and_drop

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from helpers.helpers import Helpers


class BasePage:
    def __init__(self, web_driver: webdriver.Remote):
        self.driver = web_driver


    def click_on_element(self, locator):
        WebDriverWait(self.driver, 8).until(
            EC.element_to_be_clickable(locator)
        ).click()


    def wait_element_displayed(self, locator):
        return WebDriverWait(self.driver, 8).until(
            EC.visibility_of_element_located(locator)
        ).is_displayed()


    def wait_element_invisibility(self, locator):
        return WebDriverWait(self.driver, 5).until(
            EC.invisibility_of_element_located(locator)
        )


    def find_element(self, locator):
        return WebDriverWait(self.driver, 8).until(
            EC.visibility_of_element_located(locator)
        )


    def send_keys(self, locator, text):
        WebDriverWait(self.driver, 8).until(
            EC.visibility_of_element_located(locator)
        ).send_keys(text)


    def drag_and_drop_element(self, locator_from, locator_to):
        element_source = self.find_element(locator_from)
        element_target = self.find_element(locator_to)        
        drag_and_drop(self.driver, element_source, element_target)
