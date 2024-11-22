from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginPage:
    def __init__(self, driver_chrome):
        self.driver_chrome = driver_chrome

    def authorization(self, user_name, password):
        # ввод Username
        (WebDriverWait(self.driver_chrome, 30)
         .until(EC.element_to_be_clickable((By.ID, "user-name")))
         .send_keys(user_name))
        print("Ввод Username.")
        # ввод Password
        (WebDriverWait(self.driver_chrome, 30)
         .until(EC.element_to_be_clickable((By.ID, "password")))
         .send_keys(password))
        print("Ввод Password.")
        # нажатие на кнопку Login
        (WebDriverWait(self.driver_chrome, 30)
         .until(EC.element_to_be_clickable((By.ID, "login-button")))
         .click())
        print("Нажатие на кнопку Login.")