import pytest
from selenium.webdriver.common.by import By
from pages.login_page import LoginPage
from pages.transfer_page import TransferPage

@pytest.mark.usefixtures("browser","base_url")
class TestTrasnferFunds:

    def test_transfer_success(self, browser, base_url):
        browser.get(base_url)

        # Login
        login_page = LoginPage(browser)
        login_page.login("john", "demo")

        #Dentro de la pagina
        transfer_page = TransferPage(browser)
        transfer_page.open_transfer_page()

        from_select = browser.find_element(By.ID, "fromAccountId")
        options = from_select.find_elements(By.TAG_NAME, "option")
        print("\nOpciones disponibles en 'fromAccountId':")
        for opt in options:
            print("-", opt.get_attribute("value"), "=>", opt.text)

        #Hacer transferencia
        transfer_page.transfer(amount='150', from_account='54321', to_account='13344' )

        # Mensaje de exito
        success_message = transfer_page.get_success_message()
        assert "Transfer Complete" in success_message, "❌ La transferencia no se completó correctamente"

    def test_transfer_without_amount(self, browser, base_url):
        """Verifica que no se permita transferir sin ingresar monto"""
        browser.get(base_url)

        login_page = LoginPage(browser)
        login_page.login("john", "demo")

        transfer_page = TransferPage(browser)
        transfer_page.open_transfer_page()

        # No ingresar monto
        transfer_page.transfer(amount="")

        error_message = transfer_page.get_error_message()
        assert "Error" in error_message, "❌ No se mostró el mensaje de error al dejar el monto vacío"
        print("✅ Se mostró correctamente el mensaje de error al intentar transferir sin monto")