from selenium.webdriver.common.by import By


class MainForm:
    def __init__(self, driver):
        self.driver = driver
        self.driver.get("https://bonigarcia.dev/selenium-webdriver-java/data-types.html")

    def fill_parameters(self, parameter, value):
        self.driver.find_element(By.NAME, parameter).send_keys(value)

    def click_submit(self):
        self.driver.find_element(By.TAG_NAME, "button").click()

    def return_result(self, parameter):
        return self.driver.find_element(By.ID, parameter).get_attribute("class")


