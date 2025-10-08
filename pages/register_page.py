from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class RegisterPage:
    #Localizadores
    REGISTER_LINK = (By.XPATH, "//a[@href='register.htm']")
    INPUT_FIRST_NAME = (By.ID, "customer.firstName")
    INPUT_LAST_NAME = (By.ID, "customer.lastName")
    INPUT_ADDRESS = (By.ID, "customer.address.street")
    INPUT_CITY = (By.ID, "customer.address.city")
    INPUT_STATE = (By.ID, "customer.address.state")
    INPUT_ZIP = (By.ID, "customer.address.zipCode")
    INPUT_PHONE = (By.ID, "customer.phoneNumber")
    INPUT_SSN = (By.ID, "customer.ssn")
    USERNAME = (By.ID, "customer.username")
    PASSWORD = (By.ID, "customer.password")
    CONFIRM_PASSWORD = (By.ID, "repeatedPassword")
    REGISTER_BUTTON = (By.XPATH, "//input[@value='Register']")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    #Metodos
    def click_register_link(self):
        wait = WebDriverWait(self.driver, 10)
        register_link = wait.until(EC.element_to_be_clickable(self.REGISTER_LINK))
        register_link.click()

    def enter_first_name(self, first_name):
        self.driver.find_element(*self.INPUT_FIRST_NAME).send_keys(first_name)

    def enter_last_name(self, last_name):
        self.driver.find_element(*self.INPUT_LAST_NAME).send_keys(last_name)

    def enter_address(self, address):
        self.driver.find_element(*self.INPUT_ADDRESS).send_keys(address)

    def enter_city(self, city):
        self.driver.find_element(*self.INPUT_CITY).send_keys(city)

    def enter_state(self, state):
        self.driver.find_element(*self.INPUT_STATE).send_keys(state)

    def enter_zip(self, zipcode):
        self.driver.find_element(*self.INPUT_ZIP).send_keys(zipcode)

    def enter_phone(self, phonenumber):
        self.driver.find_element(*self.INPUT_PHONE).send_keys(phonenumber)

    def enter_ssn(self, ssnnumber):
        self.driver.find_element(*self.INPUT_SSN).send_keys(ssnnumber)

    def enter_username(self, username):
        self.driver.find_element(*self.USERNAME).send_keys(username)

    def enter_password(self, password):
        self.driver.find_element(*self.PASSWORD).send_keys(password)

    def confirm_password(self, password):
        self.driver.find_element(*self.CONFIRM_PASSWORD).send_keys(password)

    def fill_registration_form(self, first_name, last_name, address, city, state, zipcode, phonenumber, ssnnumber,
                               username, password):
        self.enter_first_name(first_name)
        self.enter_last_name(last_name)
        self.enter_address(address)
        self.enter_city(city)
        self.enter_state(state)
        self.enter_zip(zipcode)
        self.enter_phone(phonenumber)
        self.enter_ssn(ssnnumber)
        self.enter_username(username)
        self.enter_password(password)
        self.confirm_password(password)

    def click_register_button(self):
        self.wait.until(EC.element_to_be_clickable(self.REGISTER_BUTTON)).click()