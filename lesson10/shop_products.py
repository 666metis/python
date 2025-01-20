from selenium.webdriver.common.by import By


class ShopProducts:
    def __init__(self, driver):
        self.driver = driver

    def add_product(self, value):
        self.driver.find_element(By.ID, value).click()