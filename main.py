from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC

from login_page import LoginPage


class Test:
    def __init__(self, base_url):
        self.driver_chrome = None
        self.base_url = base_url
        self.options = self.configuration()
        self.service = ChromeService(ChromeDriverManager().install())

    def configuration(self):
        options = webdriver.ChromeOptions()
        options.add_experimental_option("detach", True)
        return options

    def open_browser(self):
        # открытие браузера с параметрами
        self.driver_chrome = webdriver.Chrome(
            options=self.options,
            service=self.service
        )
        # переход по url в браузере/развернуть на весь экран
        self.driver_chrome.get(base_url)
        self.driver_chrome.maximize_window()
        print("Браузер открыт.")

    def authorization(self):
        login = LoginPage(self.driver_chrome)
        login.authorization(user_name="standard_user", password="secret_sauce")

    def select_product(self):
        # название продукта
        value_product_name = (WebDriverWait(self.driver_chrome, 30)
                              .until(EC.element_to_be_clickable((By.ID, "item_4_title_link")))
                              .text)

        # добавление в корзину
        (WebDriverWait(self.driver_chrome, 30)
         .until(EC.element_to_be_clickable((By.ID, "add-to-cart-sauce-labs-backpack")))
         .click())
        print(f"Товар \"{value_product_name}\" добавлен в корзину.")

    def go_to_cart(self):
        # переход в корзину
        (WebDriverWait(self.driver_chrome, 30)
         .until(EC.element_to_be_clickable((By.ID, "shopping_cart_container")))
         .click())
        print("Переход в корзину.")

    def in_the_cart(self):
        # поиск элемента
        value_text_in_to_cart = (WebDriverWait(self.driver_chrome, 30)
                                 .until(EC.element_to_be_clickable((By.XPATH, "//span[@class='title']")))
                                 .text)
        assert value_text_in_to_cart == "Your Cart", "Ошибка: Текст должен совпадать."
        print(f"Текст \"{value_text_in_to_cart}\" присутствует на странице.")

    def exit_browser(self):
        # закрытие браузера
        self.driver_chrome.quit()
        print("Закрытие браузера.")


if __name__ == "__main__":
    base_url = 'https://www.saucedemo.com/'
    start_test = Test(base_url)
    start_test.open_browser()
    start_test.authorization()
    start_test.select_product()
    start_test.go_to_cart()
    start_test.in_the_cart()
    start_test.exit_browser()
