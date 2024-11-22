from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LoginPage:
    def __init__(self, driver_chrome):
        self.driver_chrome = driver_chrome

    def authorization(self, user_name, password):
        # ввод Username
        input_user_name = WebDriverWait(self.driver_chrome, 30).until(EC.element_to_be_clickable((
            By.ID,
            "user-name"
        )))
        input_user_name.send_keys(user_name)
        print("Ввод Username.")

        # ввод Password
        input_password = WebDriverWait(self.driver_chrome, 30).until(EC.element_to_be_clickable((
            By.ID,
            "password"
        )))
        input_password.send_keys(password)
        print("Ввод Password.")

        # нажатие на кнопку Login
        click_login = WebDriverWait(self.driver_chrome, 30).until(EC.element_to_be_clickable((
            By.ID,
            "login-button"
        )))
        click_login.click()
        print("Нажатие на кнопку Login.")
