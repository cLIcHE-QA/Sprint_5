from locators import StellarBurgersLocators


class TestStellaBurgerSection:
    def test_moving_buns_section(self, driver):
        last_item_table = driver.find_element(*StellarBurgersLocators.LAST_ITEM_TABLE)
        driver.execute_script("arguments[0].scrollIntoView();", last_item_table)
        buns_tab = driver.find_element(*StellarBurgersLocators.BUNS_TAB)
        buns_tab.click()
        active_tab = driver.find_element(*StellarBurgersLocators.ACTIVE_TAB)
        assert active_tab.text == "Булки"

    def test_moving_sauces_section(self, driver):
        sauces_tab = driver.find_element(*StellarBurgersLocators.SAUCES_TAB)
        sauces_tab.click()
        active_tab = driver.find_element(*StellarBurgersLocators.ACTIVE_TAB)
        assert active_tab.text == "Соусы"

    def test_moving_toppings_section(self, driver):
        toppings_tab = driver.find_element(*StellarBurgersLocators.TOPPINGS_TAB)
        toppings_tab.click()
        active_tab = driver.find_element(*StellarBurgersLocators.ACTIVE_TAB)
        assert active_tab.text == "Начинки"
