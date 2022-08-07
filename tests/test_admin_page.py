import pytest
import allure
from src.object_admin_page import Admin_page


@allure.feature('Auth')
@allure.step
@pytest.mark.admin
def test_login_page_admin(browser):
    Admin_page(browser).admin_page()

@allure.feature('Add item')
@allure.step
@pytest.mark.admin
def test_add_new_item(browser):
    Admin_page(browser).add_new_item()

@allure.feature('Del item')
@allure.step
@pytest.mark.admin
def test_del_item(browser):
    Admin_page(browser).del_item()

