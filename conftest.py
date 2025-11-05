import pytest
from selenium import webdriver


@pytest.fixture(scope='session')
def browser():
    driver = webdriver.Chrome()
    # browser.set_window_size(1000, 1000)
    yield driver
    driver.quit()