import pytest
import allure
from src.object_main_page import Main_page


@pytest.mark.main_page
class Test_main_page:

    @allure.step
    def test_check_slider(self, browser):
        Main_page(browser=browser).check_slider()

    @allure.step
    def test_check_shopping_cart(self, browser):
        Main_page(browser=browser).check_shopping_cart()

    @allure.step
    def test_main_page_menu(self, browser):
        Main_page(browser=browser).main_page_menu()

    @allure.step
    def test_main_page_fetured_items(self, browser):
        Main_page(browser=browser).main_page_fetured_items()

    @allure.step
    def test_main_page_footer_blocks(self, browser):
        Main_page(browser=browser).main_page_footer_blocks()

    @allure.step
    def test_main_page_open_product(self, browser):
        Main_page(browser=browser).main_page_open_product()

