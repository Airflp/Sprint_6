from selenium.webdriver.common.by import By


class MainPageLocators:
    COOKIE_BUTTON = (By.ID, "rcc-confirm-button")

    ORDER_BUTTON_TOP = (
        By.XPATH,
        "//div[contains(@class,'Header_Nav')]//button[text()='Заказать']"
    )

    ORDER_BUTTON_BOTTOM = (
        By.XPATH,
        "//div[contains(@class,'Home_FinishButton')]//button[text()='Заказать']"
    )

    FAQ_SECTION = (
        By.XPATH,
        "//div[contains(@class,'Home_FAQ')]"
    )

    YANDEX_LOGO = (
        By.XPATH,
        "//a[contains(@class,'Header_LogoYandex')]"
    )

    SCOOTER_LOGO = (
        By.XPATH,
        "//a[contains(@class,'Header_LogoScooter')]"
    )

    QUESTION_PREFIX = (By.ID, "accordion__heading-")
    ANSWER_PREFIX = (By.ID, "accordion__panel-")