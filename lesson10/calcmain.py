from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


class CalcMain:
    def __init__(self, driver):
        """
        Эта функция открыввает браузер и переходит по ссылке
        :param driver:
        """
        self.driver = driver
        self.driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")

    def set_delay(self, delay):
        delay = self.driver.find_element(By.CSS_SELECTOR, '#delay')
        delay.clear()
        delay.send_keys("delay")

    def click_button(self, value):
        self.driver.find_element(By.XPATH, f"//span[text()='{value}']").click()

    def check_result(self, result):
        WebDriverWait(self.driver, 46).until(EC.text_to_be_present_in_element((By.CLASS_NAME, "screen"), str(result)))
        return self.driver.find_element(By.CSS_SELECTOR, ".screen").text




