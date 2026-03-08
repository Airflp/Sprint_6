import pytest
import allure
from pages.main_page import MainPage
from pages.order_page import OrderPage


TEST_DATA = [
    {
        "name": "Иван",
        "surname": "Иванов",
        "address": "ул. Мира 10",
        "phone": "79772227722",
        "comment": "Позвонить"
    },
    {
        "name": "Анна",
        "surname": "Петрова",
        "address": "пр. Ленина 5",
        "phone": "79665455465",
        "comment": "Оставить у двери"
    }
]


class TestOrderScooter:

    @allure.title("Проверка заказа самоката")
    @pytest.mark.parametrize("data, button", [
        (TEST_DATA[0], "top"),
        (TEST_DATA[1], "top"),
        (TEST_DATA[0], "bottom")
    ])
    def test_order_scooter(self, driver, data, button):

        main_page = MainPage(driver)
        order_page = OrderPage(driver)

        main_page.go_to_site()
        main_page.accept_cookies()

        if button == "top":
            main_page.click_order_button_top()
        else:
            main_page.click_order_button_bottom()

        order_page.fill_order_form(data)

        assert order_page.is_order_success()

    def test_scooter_logo_redirect(self, driver):

        main_page = MainPage(driver)

        main_page.go_to_site()
        main_page.accept_cookies()

        main_page.click_order_button_top()
        main_page.click_scooter_logo()

        assert "scooter" in driver.current_url

    def test_yandex_logo_redirect(self, driver):

        main_page = MainPage(driver)

        main_page.go_to_site()
        main_page.accept_cookies()

        main_window = driver.current_window_handle

        main_page.click_yandex_logo_and_wait_for_new_window(main_window)

        assert "dzen" in driver.current_url