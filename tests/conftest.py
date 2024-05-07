import pytest
from selenium import webdriver
from config import URL


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.get(URL)
    yield driver
    driver.quit()
