import pytest
import allure
from src.object_catalog_page import Catalog

@allure.step
@pytest.mark.catalog
@pytest.mark.parametrize("url", Catalog.common_url)
def test_catalogs_page(url, browser):
    """Проверяет общие элементы для разных категорий"""
    Catalog(browser=browser).catalog(url)

