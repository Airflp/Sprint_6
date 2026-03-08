import pytest
import allure
from pages.main_page import MainPage


class TestFAQ:

    @allure.title("Проверка FAQ")
    @pytest.mark.parametrize("question_index", list(range(8)))
    def test_faq_questions(self, driver, question_index):

        main_page = MainPage(driver)

        main_page.go_to_site()
        main_page.accept_cookies()
        main_page.scroll_to_faq_section()

        main_page.click_question(question_index)

        assert main_page.is_answer_visible(question_index)