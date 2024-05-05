from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators import StellarBurgersLocators


class TestStellaBurgerSection:
    def test_moving_toppings_section(self, driver):
        toppings_tab = driver.find_element(*StellarBurgersLocators.TOPPINGS_TAB)
        toppings_tab.click()
        active_tab = driver.find_element(*StellarBurgersLocators.ACTIVE_TAB)
        assert active_tab.text == "Начинки"
