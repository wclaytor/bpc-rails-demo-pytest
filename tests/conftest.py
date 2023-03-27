import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

@pytest.fixture
def driver():
    url = "http://demo.billclaytor.com"
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

    driver.get(url)
    yield driver
    driver.close()