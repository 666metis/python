import allure
import pytest
from selenium import webdriver
from lesson7.mainform import MainForm


@pytest.fixture()
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()


@allure.suite("Заполнение и отправка формы")
@allure.title("Тест отправки формы")
@allure.description(
    "Этот тест проряет заполняемость формы данными и проверяет заполненность каждого поля после отправки"
)
@allure.feature("Форма отправки")
def test_fill_form(driver):
    """
    Тест для проверки отправки формы и валидации данных
    :param driver:
    :return:
    """
    with allure.step("Создать объект формы и начать заполнение данных"):
        form = MainForm(driver)
    form.fill_parameters("first-name", "Иван")
    form.fill_parameters("last-name", "Петров")
    form.fill_parameters("address", "Ленина,55-3")
    form.fill_parameters("e-mail", "test@skypro.com")
    form.fill_parameters("phone", "+7985899998787")
    form.fill_parameters("city", "Москва")
    form.fill_parameters("country", "Россия")
    form.fill_parameters("job-position", "QA")
    form.fill_parameters("company", "SkyPro")

    with allure.step("Нажать на кнопку и проверить что поле зип-лок не заполнено и подсвечивается красным"):
        form.click_submit()
    assert "danger" in form.return_result("zip-code")


    with allure.step("проверить, что все поля успешно заполнены и подсвечиваются зеленым"):
        fields_to_check = ['first-name', 'last-name', 'address', 'e-mail', 'phone', 'city', 'country', 'job-position', 'company']

    for field_name in fields_to_check:
        assert "success" in form.return_result(field_name)

    driver.quit()