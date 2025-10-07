import pytest
from selenium.webdriver.common.by import By
from pages.login_page import LoginPage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.mark.usefixtures("browser", "base_url")
class TestLogin:
    def test_login_page(self, browser, base_url):
        browser.get(base_url)
        login_page = LoginPage(browser)
        login_page.login(("john"), ("dem"))

        WebDriverWait(browser, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "title")))

        assert "Accounts Overview" in browser.page_source, "El login valido Fallo"

    def test_login_invalido(self, browser, base_url):
        browser.get(base_url)
        login_page = LoginPage(browser)
        login_page.login("invalidUser", "invalidPass")

        # Mensaje de error login
        assert "The username and password could not be verified" in browser.page_source, \
            "No se mostro mensaje de error para login invalido"

    def test_campos_vacios(self, browser, base_url):
        browser.get(base_url)
        login_page = LoginPage(browser)
        login_page.login("", "")

        # Mostrar mensaje de error/ no dejar loguear
        assert "Please enter a username and password." in browser.page_source, \
            "No se validó login con campos vacios"
