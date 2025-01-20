import allure
import pytest
from selenium import webdriver
from lesson7.calcmain import CalcMain


@pytest.fixture()
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()


@allure.suite("Заполнение и проверка кулькулятора")
@allure.title("Проверка кулькулятора")
@allure.description("Данный тест поможет проверить работоспособность кулькулятора")
def test_fill_calc(driver):
    with allure.step("Создать объект формы и заполнить ее"):
        calc = CalcMain(driver)
    calc.set_delay(45)

    calc.click_button("7")
    calc.click_button("+")
    calc.click_button("8")
    calc.click_button("=")

    with allure.step("Проверить, что фактический результат совпадает с ожидаемым"):
        assert calc.check_result(15) == "15"