from selenium.webdriver.common.by import By


class ShopMain:
    def __init__(self, driver):
        self.driver = driver
        self.driver.get("https://www.saucedemo.com/")

    def fill_parameter(self, parameter, value):
        self.driver.find_element(By.ID, parameter).send_keys(value)

    def click_button(self):
        self.driver.find_element(By.ID, "login-button").click()
