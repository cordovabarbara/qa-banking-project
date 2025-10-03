import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

#URL

BASE_URL = "https://parabank.parasoft.com/parabank/index.htm"

@pytest.fixture()
def browser():
    #inicia y cierra el navegador
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.maximize_window()
    yield driver
    driver.quit()

@pytest.fixture
def base_url():
    return BASE_URL