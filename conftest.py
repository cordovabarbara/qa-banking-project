import os
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import pytest_html.extras as extras


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()

    if report.when == "call" and report.failed:
        driver = item.funcargs.get('browser', None)
        if driver:
            try:
                # Carpeta de screenshots
                screenshots_dir = os.path.join(os.getcwd(), "reports", "screenshots")
                os.makedirs(screenshots_dir, exist_ok=True)

                # Nombre del screenshot = nombre del test
                screenshot_file = os.path.join(screenshots_dir, f"{item.name}.png")
                driver.save_screenshot(screenshot_file)
                print(f"📸 Screenshot saved: {screenshot_file}")

                # Incrusta en el reporte HTML
                if not hasattr(report, "extra"):
                    report.extra = []

                report.extra.append(extras.image(screenshot_file))

            except Exception as e:
                print(f"❌ Error capturing screenshot: {e}")


# Opción para seleccionar navegador

def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="chrome", help="Browser to run tests"
    )


# Fixture del navegador
@pytest.fixture(scope="function")
def browser(request):
    browser_name = request.config.getoption("browser_name")

    if browser_name.lower() == "chrome":
        chrome_options = Options()
        chrome_options.add_argument("--headless")  # necesario para CI
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-dev-shm-usage")
        chrome_options.add_argument("--start-maximized")
        chrome_options.add_argument("--incognito")
        chrome_options.add_argument("--log-level=3")

        # Desactivar guardado de contraseñas
        prefs = {
            "credentials_enable_service": False,
            "profile.password_manager_enabled": False
        }
        chrome_options.add_experimental_option("prefs", prefs)
        chrome_options.add_argument("--disable-save-password-bubble")
        chrome_options.add_argument("--disable-features=PasswordManager,AutofillSaveCard")

        driver = webdriver.Chrome(service=Service(), options=chrome_options)

    elif browser_name.lower() == "firefox":
        driver = webdriver.Firefox()

    else:
        raise ValueError(f"Browser '{browser_name}' no soportado")

    driver.maximize_window()
    driver.implicitly_wait(5)

    yield driver
    driver.quit()

# Fixture de la URL base
BASE_URL = "https://parabank.parasoft.com/parabank/index.htm"

@pytest.fixture(scope="session")
def base_url():
    return BASE_URL