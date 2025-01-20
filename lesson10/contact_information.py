from selenium.webdriver.common.by import By


class ContactInformation:
    def __init__(self, driver):
        self.driver = driver

    def contact_information(self, parameter, value):
        self.driver.find_element(By.ID, parameter).send_keys(value)

    def continue_button(self, value):
        self.driver.find_element(By.ID, value).click()