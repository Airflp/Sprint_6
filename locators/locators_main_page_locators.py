from locators.main_page_locators import MainPageLocators

class MainPageLocators:
    ORDER_BUTTON_TOP = (By.XPATH, "//button[contains(text(), 'Заказать')]")
    ORDER_BUTTON_BOTTOM = (By.XPATH, "//button[contains(text(), 'Заказать')]")
    DROPDOWN_QUESTION_1 = (By.XPATH, "//div[text()='Question 1']")
    DROPDOWN_QUESTION_2 = (By.XPATH, "//div[text()='Question 2']")
    LOGO_SAMOKAT = (By.XPATH, "//img[@alt='Самокат']")
    LOGO_YANDEX = (By.XPATH, "//img[@alt='Яндекс']")