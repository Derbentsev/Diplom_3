from selenium.webdriver.common.by import By


class HomePageLocators:    
    HEADER_TEXT_LOCATOR = (By.XPATH, '//h1[text()="Соберите бургер"]')
    IDENTIFIER_ORDER_LOCATOR = (By.XPATH, '//h2[contains(@class, "Modal_modal__title")]')
    PLACE_AN_ORDER_BUTTON_LOCATOR = (By.XPATH, '//button[text()="Оформить заказ"]')
    CLOSE_ORDER_POPUP_WINDOW_LOCATOR = (By.XPATH, '//button[contains(@class, "modal__close")]')
    OVERLAY_LOCATOR = (By.XPATH, '//div[contains(@class, "Modal_modal_overlay")]')
    

    BURGER_CONSTRUCTOR_BASKET_LOCATOR = (
        By.XPATH,
        '//ul[contains(@class, "BurgerConstructor_basket__list")]'
    )

    INGREDIENT_CARD_WINDOW_CLOSE_BUTTON_LOCATOR = (
        By.XPATH,
        '//button[contains(@class, "Modal_modal__close")]'
    )

    INGREDIENT_CARD_HEADER_TEXT_LOCATOR = (
        By.XPATH,
        '//h2[text()="Детали ингредиента"]'
    )


    def get_ingredient_card_locator(card_index: int):
        return (By.XPATH, f'//a[contains(@class, "BurgerIngredient")][{card_index}]')


    def get_ingredient_counter_locator(card_index: int):
        return (By.XPATH, f'//p[contains(@class, "counter_counter")][{card_index}]')
