import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import os
login_email = os.getenv("STEPIK_LOGIN")
login_password = os.getenv("STEPIK_PASSWORD")


@pytest.fixture(scope="function")
def browser():
    """Фикстура для инициализации и закрытия браузера"""
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    browser.implicitly_wait(10)
    yield browser
    print("\nquit browser..")
    browser.quit()

def test_stepik_login(browser):
    """Тест авторизации на Stepik"""
    # Шаг 1: Открываем урок
    link = "https://stepik.org/lesson/236895/step/1"
    browser.get(link)

    # Шаг 2: Ищем кнопку "Войти" и кликаем на неё
    login_link = browser.find_element(By.CSS_SELECTOR, 'a[href="/lesson/236895/step/1?auth=login"]')
    login_link.click()

    # Шаг 3: Ждем появления формы авторизации и заполняем её
    email_field = browser.find_element(By.NAME, "login")
    password_field = browser.find_element(By.NAME, "password")
    email_field.send_keys(login_email)
    password_field.send_keys(login_password)

    # Шаг 4: Нажимаем кнопку "Войти" и проверяем, что модальное окно исчезло
    submit_button = browser.find_element(By.CSS_SELECTOR, "button[type='submit']")
    submit_button.click()
    WebDriverWait(browser, 15).until_not(
        EC.presence_of_element_located((By.CSS_SELECTOR, ".modal-dialog"))
    )
    