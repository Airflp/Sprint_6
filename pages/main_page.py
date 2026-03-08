import allure

from pages.base_page import BasePage
from locators.main_page_locators import MainPageLocators
from urls import Urls


class MainPage(BasePage):

    @allure.step("Открыть сайт")
    def go_to_site(self):
        self.open_url(Urls.MAIN_PAGE)

    @allure.step("Принять cookies")
    def accept_cookies(self):
        try:
            self.click_element(MainPageLocators.COOKIE_BUTTON)
        except:
            pass

    @allure.step("Прокрутить до FAQ")
    def scroll_to_faq_section(self):
        element = self.find_element(MainPageLocators.FAQ_SECTION)
        self.scroll_to_element(element)

    @allure.step("Нажать вопрос FAQ")
    def click_question(self, index):
        locator = MainPageLocators.FAQ_QUESTIONS[index]
        self.click_element(locator)

    @allure.step("Проверить видимость ответа FAQ")
    def is_answer_visible(self, index):
        locator = MainPageLocators.FAQ_ANSWERS[index]
        return self.is_element_visible(locator)

    @allure.step("Нажать кнопку заказа")
    def click_order_button(self, locator):
        self.click_element(locator)

    @allure.step("Клик по логотипу Самоката")
    def click_scooter_logo(self):
        self.click_element(MainPageLocators.SCOOTER_LOGO)

    @allure.step("Клик по логотипу Яндекса")
    def click_yandex_logo(self):
        self.click_element(MainPageLocators.YANDEX_LOGO)