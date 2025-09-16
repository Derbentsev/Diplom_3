from selenium import webdriver


class Helpers:
    @staticmethod
    # Подсветка элемента желтым
    def set_element_color(web_driver: webdriver.Remote, element_target):
        web_driver.execute_script(
            "arguments[0].setAttribute('style', arguments[1]);",
            element_target,
            "border: 3px solid red; background-color: yellow;"
        )
