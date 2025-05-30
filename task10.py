from selenium.webdriver.common.by import By
from selenium import webdriver
import time
import math


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


try:
    # Открыть страницу https://SunInJuly.github.io/execute_script.html.
    link = "http://suninjuly.github.io/execute_script.html"
    browser = webdriver.Firefox()
    browser.get(link)

    # Считать значение для переменной x.
    valuex = browser.find_element(By.ID, "input_value")
    
    # Посчитать математическую функцию от x.
    y = calc(valuex.text)
    
    # Проскроллить страницу вниз.
    browser.execute_script("window.scrollBy(0, 200);")

    # Ввести ответ в текстовое поле.
    answer = browser.find_element(By.ID, "answer")
    answer.send_keys(y)
    
    # Выбрать checkbox "I'm the robot".
    checkbox = browser.find_element(By.ID, "robotCheckbox")
    checkbox.click()

    # Переключить radiobutton "Robots rule!".
    radiobutton = browser.find_element(By.ID, "robotsRule")
    radiobutton.click()

    # Нажать на кнопку "Submit".
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

finally:
    # Ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # Закрываем браузер после всех манипуляций
    if 'browser' in locals():  # Проверяем, что browser был создан
        browser.quit()
