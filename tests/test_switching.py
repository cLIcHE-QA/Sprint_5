from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from config import URL
from locators import StellarBurgersLocators
from data import user_credentials


class TestStellaBurgerSwitching:
    def test_switching_from_personal_cabinet_to_designer(self, driver):
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
        WebDriverWait(driver, 2).until(expected_conditions.element_to_be_clickable(StellarBurgersLocators.ORDER_BUTTON))
        myaccount_button = driver.find_element(*StellarBurgersLocators.MYACCOUNT_BUTTON)
        myaccount_button.click()
        WebDriverWait(driver, 2).until(expected_conditions.element_to_be_clickable(StellarBurgersLocators.PROFILE))
        constructor = driver.find_element(*StellarBurgersLocators.CONSTRUCTOR)
        constructor.click()
        assert driver.current_url == f'{URL}/'

    def test_switching_from_personal_cabinet_to_logo(self, driver):
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
        WebDriverWait(driver, 2).until(expected_conditions.element_to_be_clickable(StellarBurgersLocators.ORDER_BUTTON))
        myaccount_button = driver.find_element(*StellarBurgersLocators.MYACCOUNT_BUTTON)
        myaccount_button.click()
        WebDriverWait(driver, 2).until(expected_conditions.element_to_be_clickable(StellarBurgersLocators.PROFILE))
        logo = driver.find_element(*StellarBurgersLocators.LOGO)
        logo.click()
        assert driver.current_url == f'{URL}/'

    def test_switching_to_personal_cabinet(self, driver):
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
        WebDriverWait(driver, 2).until(expected_conditions.element_to_be_clickable(StellarBurgersLocators.ORDER_BUTTON))
        myaccount_button = driver.find_element(*StellarBurgersLocators.MYACCOUNT_BUTTON)
        myaccount_button.click()
        WebDriverWait(driver, 2).until(expected_conditions.element_to_be_clickable(StellarBurgersLocators.PROFILE))
        profile = driver.find_element(*StellarBurgersLocators.PROFILE)
        assert profile.is_displayed()
