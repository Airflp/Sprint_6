import allure
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    @allure.step("Открыть страницу")
    def open_url(self, url):
        self.driver.get(url)

    @allure.step("Найти элемент")
    def find_element(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located(locator)
        )

    @allure.step("Кликнуть по элементу")
    def click_element(self, locator):
        element = self.find_element(locator)
        element.click()

    @allure.step("Получить текст элемента")
    def get_text(self, locator):
        element = self.find_element(locator)
        return element.text

    @allure.step("Прокрутить до элемента")
    def scroll_to_element(self, element):
        self.driver.execute_script(
            "arguments[0].scrollIntoView();",
            element
        )

    @allure.step("Проверить видимость элемента")
    def is_element_visible(self, locator):
        try:
            self.find_element(locator)
            return True
        except:
            return False

    @allure.step("Получить текущее окно")
    def get_current_window(self):
        return self.driver.current_window_handle

    @allure.step("Переключиться на новую вкладку")
    def switch_to_new_window(self, main_window):

        WebDriverWait(self.driver, 10).until(
            lambda driver: len(driver.window_handles) > 1
        )

        for window in self.driver.window_handles:
            if window != main_window:
                self.driver.switch_to.window(window)
                return

    @allure.step("Проверить URL")
    def url_contains(self, text):
        return text in self.driver.current_url