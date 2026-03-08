import allure
from selenium.webdriver.common.keys import Keys

from pages.base_page import BasePage
from locators.order_page_locators import OrderPageLocators


class OrderPage(BasePage):

    @allure.step("Заполнить форму заказа")
    def fill_order_form(self, data):
        self.fill_first_form(data)
        self.fill_second_form(data)

    @allure.step("Заполнить первую страницу формы")
    def fill_first_form(self, data):

        self.find_element(OrderPageLocators.NAME).send_keys(data["name"])
        self.find_element(OrderPageLocators.SURNAME).send_keys(data["surname"])
        self.find_element(OrderPageLocators.ADDRESS).send_keys(data["address"])

        metro = self.find_element(OrderPageLocators.METRO_INPUT)
        metro.click()
        metro.send_keys("Черкизовская")

        self.click_element(OrderPageLocators.METRO_OPTION)

        self.find_element(OrderPageLocators.PHONE).send_keys(data["phone"])

        self.click_element(OrderPageLocators.NEXT_BUTTON)

    @allure.step("Заполнить вторую страницу формы")
    def fill_second_form(self, data):

        date = self.find_element(OrderPageLocators.DATE)
        date.send_keys("10.10.2026")

        # закрываем календарь
        date.send_keys(Keys.ENTER)

        self.click_element(OrderPageLocators.RENTAL_PERIOD)

        self.click_element(OrderPageLocators.RENTAL_PERIOD_OPTION)

        color = data.get("color", "black")

        if color == "grey":
            self.click_element(OrderPageLocators.COLOR_GREY)
        else:
            self.click_element(OrderPageLocators.COLOR_BLACK)

        self.find_element(OrderPageLocators.COMMENT).send_keys(data["comment"])

        self.click_element(OrderPageLocators.ORDER_BUTTON)

        self.click_element(OrderPageLocators.CONFIRM_BUTTON)

    @allure.step("Проверить успешное оформление заказа")
    def is_order_success(self):

        return self.find_element(
            OrderPageLocators.ORDER_SUCCESS
        ).is_displayed()