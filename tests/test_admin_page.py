import pytest
from src.object_admin_page import Admin_page

@pytest.mark.admin
def test_login_page_admin(browser):
    Admin_page(browser).admin_page()

@pytest.mark.admin
def test_add_new_item(browser):
    Admin_page(browser).add_new_item()

@pytest.mark.admin
def test_del_item(browser):
    Admin_page(browser).del_item()