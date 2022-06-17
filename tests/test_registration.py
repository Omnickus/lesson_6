import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


from src.object_registration import Registration
import time

@pytest.mark.registration
def test_registration_page(browser):
    Registration(browser=browser).registration_user()

