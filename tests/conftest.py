import pytest
from selenium import webdriver
from config import URL


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.get(URL)
    yield driver
    driver.quit()


@pytest.fixture
def user_credentials():
    return {
        "email": "artembesf8132@practicum.ru",
        "password": "Practicum!23"
    }
