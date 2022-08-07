import pytest
import allure
from src.object_change_currency import Currency

@allure.step
@pytest.mark.currency
def test_catalogs_page(browser):
    """Изменние валюты на странице"""
    Currency(browser=browser).currency()

