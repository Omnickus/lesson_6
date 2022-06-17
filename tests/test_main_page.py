import pytest
from src.object_main_page import Main_page


@pytest.mark.main_page
class Test_main_page:

    def test_check_slider(self, browser):
        Main_page(browser=browser).check_slider()

    def test_check_shopping_cart(self, browser):
        Main_page(browser=browser).check_shopping_cart()

    def test_main_page_menu(self, browser):
        Main_page(browser=browser).main_page_menu()

    def test_main_page_fetured_items(self, browser):
        Main_page(browser=browser).main_page_fetured_items()

    def test_main_page_footer_blocks(self, browser):
        Main_page(browser=browser).main_page_footer_blocks()

    def test_main_page_open_product(self, browser):
        Main_page(browser=browser).main_page_open_product()

