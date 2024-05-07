from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from config import URL
from locators import StellarBurgersLocators
from helpers import get_signup_data


class TestStellaBurgerSignUp:
    def test_signup_successful(self, driver):
        driver.get(f'{URL}/register')
        name_data, email_data, password_data = get_signup_data()
        name_field = driver.find_element(*StellarBurgersLocators.NAME_FIELD)
        name_field.send_keys(name_data)
        email_field = driver.find_element(*StellarBurgersLocators.EMAIL_FIELD)
        email_field.send_keys(email_data)
        password_field = driver.find_element(*StellarBurgersLocators.PASSWORD_FIELD)
        password_field.send_keys(password_data)
        register_button = driver.find_element(*StellarBurgersLocators.REGISTER_BUTTON)
        register_button.click()
        WebDriverWait(driver, 2).until(expected_conditions.element_to_be_clickable(StellarBurgersLocators.LOGIN_BUTTON))
        assert 'login' in driver.current_url

    def test_signup_incorrect_password(self, driver):
        driver.get(f'{URL}/register')
        name_data, email_data, password_data = get_signup_data()
        name_field = driver.find_element(*StellarBurgersLocators.NAME_FIELD)
        name_field.send_keys(name_data)
        email_field = driver.find_element(*StellarBurgersLocators.EMAIL_FIELD)
        email_field.send_keys(email_data)
        password_field = driver.find_element(*StellarBurgersLocators.PASSWORD_FIELD)
        password_field.send_keys('small')
        register_button = driver.find_element(*StellarBurgersLocators.REGISTER_BUTTON)
        register_button.click()
        text_invalid_password = driver.find_element(*StellarBurgersLocators.TEXT_INVALID_PASSWORD)
        assert text_invalid_password.text == "Некорректный пароль"