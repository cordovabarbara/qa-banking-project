import os
from dotenv import load_dotenv
import pytest
from pages.login_page import LoginPage

load_dotenv()

@pytest.mark.usefixtures("browser", "base_url")
class TestLogin:
    def test_login_page(self, browser, base_url):
        browser.get(base_url)
        login_page = LoginPage(browser)
        login_page.login(os.getenv("USERNAME"), os.getenv("PASSWORD"))

        assert "Accounts Overview" in browser.page_source, "El login valido Fallo"

    def test_login_invalido(self, browser, base_url):
        browser.get(base_url)
        login_page = LoginPage(browser)
        login_page.login("invalidUser", "invalidPass")

        # Mensaje de error login
        assert "El usuario y/o la clave es incorrecta" in browser.page_source, \
            "No se mostro mensaje de error para login invalido"

    def test_campos_vacios(self, browser, base_url):
        browser.get(base_url)
        login_page = LoginPage(browser)
        login_page.login("", "")

        # Mostrar mensaje de error/ no dejar loguear
        assert "The username and password could not be verified" in browser.page_source, \
            "No se validó login con campos vacios"
