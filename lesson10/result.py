from selenium.webdriver.common.by import By


class Result:
    def __init__(self,driver):
        self.driver = driver

    def return_result(self):
        total_price = self.driver.find_element(By.CLASS_NAME, 'summary_total_label')
        total = total_price.text.strip().replace("Total: $", "")
        return total
