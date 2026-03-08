from selenium.webdriver.common.by import By


class OrderPageLocators:

    NAME = (By.XPATH, "//input[@placeholder='* Имя']")
    SURNAME = (By.XPATH, "//input[@placeholder='* Фамилия']")
    ADDRESS = (By.XPATH, "//input[contains(@placeholder,'Адрес')]")

    METRO_INPUT = (By.XPATH, "//input[@placeholder='* Станция метро']")

    METRO_OPTION = (
        By.XPATH,
        "//div[contains(@class,'select-search__select')]//button"
    )

    PHONE = (
        By.XPATH,
        "//input[@placeholder='* Телефон: на него позвонит курьер']"
    )

    NEXT_BUTTON = (
        By.XPATH,
        "//button[text()='Далее']"
    )

    DATE = (
        By.XPATH,
        "//input[@placeholder='* Когда привезти самокат']"
    )

    RENTAL_PERIOD = (
        By.XPATH,
        "//div[contains(@class,'Dropdown-root')]"
    )

    RENTAL_PERIOD_OPTION = (
        By.XPATH,
        "//div[@class='Dropdown-option' and text()='сутки']"
    )

    COLOR_BLACK = (By.ID, "black")
    COLOR_GREY = (By.ID, "grey")

    COMMENT = (
        By.XPATH,
        "//input[@placeholder='Комментарий для курьера']"
    )

    ORDER_BUTTON = (
        By.XPATH,
        "//div[contains(@class,'Order_Buttons')]//button[text()='Заказать']"
    )

    CONFIRM_BUTTON = (
        By.XPATH,
        "//button[text()='Да']"
    )

    
    ORDER_SUCCESS = (
        By.XPATH,
        "//div[contains(@class,'Order_ModalHeader')]"
    )