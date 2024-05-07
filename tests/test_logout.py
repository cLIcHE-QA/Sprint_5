from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators import StellarBurgersLocators
from data import user_credentials


class TestStellaBurgerLogout:
    def test_logout_successful(self, driver):
        email, password = user_credentials()
        signin_button = driver.find_element(*StellarBurgersLocators.SIGNIN_BUTTON)
        signin_button.click()
        WebDriverWait(driver, 2).until(expected_conditions.element_to_be_clickable(StellarBurgersLocators.LOGIN_BUTTON))
        email_field = driver.find_element(*StellarBurgersLocators.EMAIL_FIELD)
        email_field.send_keys(email)
        password_field = driver.find_element(*StellarBurgersLocators.PASSWORD_FIELD)
        password_field.send_keys(password)
        login_button = driver.find_element(*StellarBurgersLocators.LOGIN_BUTTON)
        login_button.click()
        WebDriverWait(driver, 2).until(
            expected_conditions.element_to_be_clickable(StellarBurgersLocators.MYACCOUNT_BUTTON))
        myaccount_button = driver.find_element(*StellarBurgersLocators.MYACCOUNT_BUTTON)
        myaccount_button.click()
        WebDriverWait(driver, 2).until(expected_conditions.element_to_be_clickable(StellarBurgersLocators.LOGOUT))
        logout = driver.find_element(*StellarBurgersLocators.LOGOUT)
        logout.click()
        WebDriverWait(driver, 2).until(expected_conditions.element_to_be_clickable(StellarBurgersLocators.LOGIN_BUTTON))
        assert 'login' in driver.current_url
