import pytest
from selenium import webdriver


@pytest.fixture(scope="session")
def browser():
    driver = webdriver.Chrome('chromedriver.exe')
    yield driver
    driver.quit()

