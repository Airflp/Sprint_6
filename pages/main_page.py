import allure
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.base_page import BasePage
from locators.main_page_locators import MainPageLocators
from urls import BASE_URL


class MainPage(BasePage):

    @allure.step("Открыть главную страницу")
    def go_to_site(self):
        self.driver.get(BASE_URL)

    @allure.step("Принять cookies")
    def accept_cookies(self):
        try:
            self.click_element(MainPageLocators.COOKIE_BUTTON)
        except Exception:
            pass

    @allure.step("Прокрутить до секции FAQ")
    def scroll_to_faq_section(self):
        self.scroll_to_element(MainPageLocators.FAQ_SECTION)

    @allure.step("Кликнуть по вопросу FAQ")
    def click_question(self, index):
        question_locator = (
            MainPageLocators.QUESTION_PREFIX[0],
            f"{MainPageLocators.QUESTION_PREFIX[1]}{index}"
        )
        self.click_element(question_locator)

    @allure.step("Проверить, что ответ отображается")
    def is_answer_visible(self, index):
        answer_locator = (
            MainPageLocators.ANSWER_PREFIX[0],
            f"{MainPageLocators.ANSWER_PREFIX[1]}{index}"
        )
        return self.find_element(answer_locator).is_displayed()

    @allure.step("Нажать верхнюю кнопку Заказать")
    def click_order_button_top(self):
        self.click_element(MainPageLocators.ORDER_BUTTON_TOP)

    @allure.step("Нажать нижнюю кнопку Заказать")
    def click_order_button_bottom(self):
        self.scroll_to_element(MainPageLocators.ORDER_BUTTON_BOTTOM)
        self.click_element(MainPageLocators.ORDER_BUTTON_BOTTOM)

    @allure.step("Клик по логотипу Самоката")
    def click_scooter_logo(self):
        self.click_element(MainPageLocators.SCOOTER_LOGO)

    @allure.step("Клик по логотипу Яндекса и переход в новое окно")
    def click_yandex_logo_and_wait_for_new_window(self, main_window):
        self.click_element(MainPageLocators.YANDEX_LOGO)

        WebDriverWait(self.driver, 10).until(
            EC.number_of_windows_to_be(2)
        )

        for window in self.driver.window_handles:
            if window != main_window:
                self.driver.switch_to.window(window)
                break