from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TransferPage:
    #Localizadores
    TRANSFER_FUNDS_LINK = (By.XPATH,"//a[@href='transfer.htm']")
    AMOUNT_INPUT = (By.ID,"amount")
    FROM_ACCOUNT_SELECT = (By.ID,"fromAccountId")
    TO_ACCOUNT_SELECT = (By.ID,"toAccountId")
    TRANSFER_BUTTON = (By.XPATH,"//input[@type='submit' and @value='Transfer']")
    SUCCESS_MESSAGE = (By.XPATH,"//h1[contains(text(),'Transfer Complete')]")
    ERROR_TITLE = (By.CSS_SELECTOR, "#showError .title")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    def open_transfer_page(self):
        self.wait.until(EC.element_to_be_clickable(self.TRANSFER_FUNDS_LINK)).click()

    def get_available_from_accounts(self):
        from_select = Select(self.driver.find_element(*self.FROM_ACCOUNT_SELECT))
        accounts = {}
        for option in from_select.options:
            value = option.get_attribute("value")
            text = option.text
            accounts[value] = text
        return accounts

    def get_available_to_accounts(self):
        to_select = Select(self.driver.find_element(*self.TO_ACCOUNT_SELECT))
        accounts = {}
        for option in to_select.options:
            value = option.get_attribute('value')
            text = option.text
            accounts[value] = text
        return accounts

    def transfer(self, amount, from_account=None, to_account=None):
        self.driver.find_element(*self.AMOUNT_INPUT).send_keys(amount)

        # Seleccionar cuenta FROM (si no se especifica, usa la primera)
        from_select = Select(self.driver.find_element(*self.FROM_ACCOUNT_SELECT))
        if not from_account:
            from_account = list(self.get_available_from_accounts().keys())[0]
        from_select.select_by_value(from_account)

        # Seleccionar cuenta TO (si no se especifica, usa la primera)
        to_select = Select(self.driver.find_element(*self.TO_ACCOUNT_SELECT))
        if not to_account:
            to_account = list(self.get_available_to_accounts().keys())[0]
        to_select.select_by_value(to_account)

        self.driver.find_element(*self.TRANSFER_BUTTON).click()

    def get_success_message(self):
        return self.wait.until(EC.visibility_of_element_located(self.SUCCESS_MESSAGE)).text

    def get_error_message(self):
        #Mensaje de error después de una transferencia fallida
        try:
            error_element = WebDriverWait(self.driver, 5).until(
                EC.visibility_of_element_located(self.ERROR_TITLE)
            )
            return error_element.text
        except:
            return ""