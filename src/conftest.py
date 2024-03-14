import time

import pytest
from selenium import webdriver
from src.utilities.test_data import TestData

@pytest.fixture
def initialize_driver():
    driver = webdriver.Chrome()
    driver.get(TestData.url)
    driver.maximize_window()
    yield driver
    time.sleep(5)
    driver.quit()
