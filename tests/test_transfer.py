import pytest
from pages.login_page import LoginPage
from pages.transfer_page import TransferPage

@pytest.mark.usefixtures("browser","base_url")
class TestTransferFunds:

    def login_and_open_transfer(self, browser, base_url):
        browser.get(base_url)
        login_page = LoginPage(browser)
        login_page.login("john", "demo")
        transfer_page = TransferPage(browser)
        transfer_page.open_transfer_page()
        return transfer_page


    def test_transferencia_exitosa(self, browser, base_url):
        transfer_page = self.login_and_open_transfer(browser, base_url)
        from_accounts = list(transfer_page.get_available_from_accounts().keys())
        to_accounts = list(transfer_page.get_available_to_accounts().keys())

        from_account = from_accounts[0]
        to_account = to_accounts[0]

        # Evitar transferir a la misma cuenta si hay más de una
        if from_account == to_account and len(to_accounts) > 1:
            to_account = to_accounts[1]

        transfer_page.transfer(amount='150', from_account=from_account, to_account=to_account)

        # Mensaje de exito
        success_message = transfer_page.get_success_message()
        assert "Transfer Complete" in success_message, "❌ La transferencia no se completó correctamente"

    def test_transfer_sin_monto(self, browser, base_url):
        #Verifica que no se permita transferir sin ingresar monto
        transfer_page = self.login_and_open_transfer(browser, base_url)
        transfer_page.transfer(amount="")
        error_message = transfer_page.get_error_message()
        assert "Error" in error_message, "❌ No se mostró el mensaje de error al dejar el monto vacío"