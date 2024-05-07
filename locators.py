from selenium.webdriver.common.by import By


class StellarBurgersLocators:
    SIGNIN_BUTTON = (By.XPATH, "//button[text()='Войти в аккаунт']")  # Кнопка «Войти в аккаунт»
    NAME_FIELD = (By.XPATH, ".//label[text() = 'Имя']/../input")  # Поле «Имя»
    EMAIL_FIELD = (By.XPATH, ".//label[text() = 'Email']/../input")  # Поле «Email»
    PASSWORD_FIELD = (By.XPATH, ".//label[text() = 'Пароль']/../input")  # Поле «Пароль»
    REGISTER_BUTTON = (By.XPATH, "//button[text()='Зарегистрироваться']")  # Кнопка «Зарегистрироваться»
    LOGIN_BUTTON = (By.XPATH, "//button[text()='Войти']")  # Кнопка «Войти»
    MYACCOUNT_BUTTON = (By.LINK_TEXT, "Личный Кабинет")  # Кнопка «Личный Кабинет»
    ORDER_BUTTON = (By.XPATH, "//button[text()='Оформить заказ']")  # Кнопка «Оформить заказ»
    PROFILE = (By.LINK_TEXT, "Профиль")  # Кнопка «Профиль»
    LOGIN = (By.LINK_TEXT, "Войти")  # Кнопка «Войти»
    CONSTRUCTOR = (By.LINK_TEXT, "Конструктор")  # Кнопка «Конструктор»
    LOGO = (By.CLASS_NAME, "AppHeader_header__logo__2D0X2")  # Логитип «Stellar Burgers»
    LOGOUT = (By.XPATH, "//button[text()='Выход']")  # Кнопка «Выход»
    LAST_ITEM_TABLE = (By.XPATH, "//*[contains(text(), 'Сыр с астероидной плесенью')]")  # Последний объект в таблице
    BUNS_TAB = (By.XPATH, "//*[text()='Булки']")  # Вкладка «Булки»
    SAUCES_TAB = (By.XPATH, "//*[text()='Соусы']")  # Вкладка «Соусы»
    TOPPINGS_TAB = (By.XPATH, "//*[text()='Начинки']")  # Вкладка «Начинки»
    ACTIVE_TAB = (By.CLASS_NAME, "tab_tab_type_current__2BEPc")  # Активная вкладка
    TEXT_INVALID_PASSWORD = (By.XPATH, "//p[@class='input__error text_type_main-default']")  # Текст «Некорректный пароль»
