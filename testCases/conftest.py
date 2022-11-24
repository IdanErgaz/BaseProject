from selenium import webdriver
import pytest
from selenium.webdriver.chrome.service import Service


@pytest.fixture()
def setup():
    service = Service("C://Drivers/chromedriver.exe")
    global driver
    driver = webdriver.Chrome(service=service)
    driver.maximize_window()
    return driver
