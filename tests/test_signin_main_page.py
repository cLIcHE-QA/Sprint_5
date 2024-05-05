from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators import StellarBurgersLocators


class TestStellaBurgerSignIn:
    def test_signin_main_page(self, driver, user_credentials):
        signin_button = driver.find_element(*StellarBurgersLocators.SIGNIN_BUTTON)
        signin_button.click()
        WebDriverWait(driver, 2).until(expected_conditions.element_to_be_clickable(StellarBurgersLocators.LOGIN_BUTTON))
        email_field = driver.find_element(*StellarBurgersLocators.EMAIL_FIELD)
        email_field.send_keys(user_credentials['email'])
        password_field = driver.find_element(*StellarBurgersLocators.PASSWORD_FIELD)
        password_field.send_keys(user_credentials['password'])
        login_button = driver.find_element(*StellarBurgersLocators.LOGIN_BUTTON)
        login_button.click()
        WebDriverWait(driver, 2).until(
            expected_conditions.element_to_be_clickable(StellarBurgersLocators.ORDER_BUTTON))
        order_button = driver.find_element(*StellarBurgersLocators.ORDER_BUTTON)
        assert order_button.is_displayed()
