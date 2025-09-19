import pytest
from selenium import webdriver


@pytest.fixture(params=["chrome", "firefox"], scope="function")
def web_driver(request):
    browser_type = request.param

    if browser_type == "chrome":
        driver = webdriver.Chrome()
    elif browser_type == "firefox":
        driver = webdriver.Firefox()

    driver.maximize_window()
    
    yield driver
    driver.quit()
