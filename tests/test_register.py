import pytest
import random
import string
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.register_page import RegisterPage


@pytest.mark.usefixtures("browser")
class TestRegisterPage:

    def test_registro_exitoso(self, browser):
        browser.get("https://parabank.parasoft.com/")
        register_page = RegisterPage(browser)
        register_page.click_register_link()

        # Generar datos dinámicos
        random_suffix = ''.join(random.choices(string.ascii_lowercase + string.digits, k=5))
        unique_username = f"user_{random_suffix}"
        random_phone = f"300{random.randint(1000000, 9999999)}"
        random_zip = f"{random.randint(10000, 99999)}"

        register_page.fill_registration_form(
            first_name="Ana",
            last_name=f"Lopez{random_suffix}",
            address=f"Calle {random.randint(1, 300)}",
            city="New York",
            state="NY",
            zipcode=random_zip,
            phonenumber=random_phone,
            ssnnumber=str(random.randint(10000, 99999)),
            username=unique_username,
            password="pass123"
        )
        register_page.click_register_button()

        # Esperar mensaje de éxito
        wait = WebDriverWait(browser, 10)
        success_text = wait.until(
            EC.visibility_of_element_located((By.XPATH, "//h1[contains(text(),'Welcome')]"))
        ).text

        assert "Welcome" in success_text, f"❌ Registro fallido. Texto mostrado: {success_text}"
