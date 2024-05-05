from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators import StellarBurgersLocators


class TestStellaBurgerSection:
    def test_moving_sauces_section(self, driver):
        sauces_tab = driver.find_element(*StellarBurgersLocators.SAUCES_TAB)
        sauces_tab.click()
        active_tab = driver.find_element(*StellarBurgersLocators.ACTIVE_TAB)
        assert active_tab.text == "Соусы"
