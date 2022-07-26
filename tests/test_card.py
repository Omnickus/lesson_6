import pytest
from src.object_card import Card

@pytest.mark.card
@pytest.mark.parametrize("path", Card.featured)
def test_main_page_featured(path, browser):
    browser.get(browser.url)
    Card(browser=browser).card(path = path)

