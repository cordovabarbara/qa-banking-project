from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginPage:
    #Localizadores
    USERNAME_INPUT = (By.NAME, 'username')
    PASSWORD_INPUT = (By.NAME, 'password')
    LOGIN_BUTTON = (By.XPATH, '//input[@type="submit" and @value="Log in"]')

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    #Metodos
    def enter_username(self, username):
       element = self.wait.until(EC.visibility_of_element_located(self.USERNAME_INPUT))
       element.clear()
       element.send_keys(username)

    def enter_password(self, password):
        element = self.wait.until(EC.visibility_of_element_located(self.PASSWORD_INPUT))
        element.clear()
        element.send_keys(password)

    def click_login_button(self):
        self.driver.find_element(*self.LOGIN_BUTTON).click()


    # Metodo flujo completo de login
    def login(self, username, password):
        self.enter_username(username)
        self.enter_password(password)
        self.click_login_button()