import pytest
from src.object_change_currency import Currency

@pytest.mark.currency
def test_catalogs_page(browser):
    """Изменние валюты на странице"""
    Currency(browser=browser).currency()

