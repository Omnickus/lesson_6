import pytest
import allure
from src.object_card import Card
from src.base.logger import Logger

@allure.step
@pytest.mark.card
@pytest.mark.parametrize("path", Card.featured)
def test_main_page_featured(path, browser):
    browser.get(browser.url)
    Logger(f'Открыл страницу - {browser.url}').infolog
    Card(browser=browser).card(path = path)

