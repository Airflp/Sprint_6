import pytest
import allure

from pages.main_page import MainPage
from pages.order_page import OrderPage
from locators.main_page_locators import MainPageLocators


TEST_DATA = [
    {
        "name": "Иван",
        "surname": "Иванов",
        "address": "ул. Мира 10",
        "phone": "79772227722",
        "comment": "Позвонить",
        "color": "black"
    },
    {
        "name": "Анна",
        "surname": "Петрова",
        "address": "пр. Ленина 5",
        "phone": "79665455465",
        "comment": "Оставить у двери",
        "color": "grey"
    }
]


class TestOrderScooter:

    @allure.title("Проверка заказа самоката")
    @pytest.mark.parametrize("data, locator", [

        (TEST_DATA[0], MainPageLocators.ORDER_BUTTON_TOP),
        (TEST_DATA[1], MainPageLocators.ORDER_BUTTON_TOP),
        (TEST_DATA[0], MainPageLocators.ORDER_BUTTON_BOTTOM)

    ])
    def test_order_scooter(self, driver, data, locator):

        main_page = MainPage(driver)
        order_page = OrderPage(driver)

        main_page.go_to_site()
        main_page.accept_cookies()

        main_page.click_order_button(locator)

        order_page.fill_order_form(data)

        assert order_page.is_order_success()

    @allure.title("Проверка перехода по логотипу Самоката")
    def test_scooter_logo_redirect(self, driver):

        main_page = MainPage(driver)

        main_page.go_to_site()
        main_page.accept_cookies()

        main_page.click_scooter_logo()

        assert main_page.url_contains("scooter")

    @allure.title("Проверка перехода на Дзен")
    def test_yandex_logo_redirect(self, driver):

        main_page = MainPage(driver)

        main_page.go_to_site()
        main_page.accept_cookies()

        main_window = main_page.get_current_window()

        main_page.click_yandex_logo()

        main_page.switch_to_new_window(main_window)

        assert main_page.url_contains("dzen")