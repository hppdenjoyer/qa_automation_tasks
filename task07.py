from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math


def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))


try:
    # Открыть страницу https://suninjuly.github.io/math.html.
    link = "https://suninjuly.github.io/math.html"
    browser = webdriver.Firefox()
    browser.get(link)
    
    # Считать значение для переменной x.
    x_element = browser.find_element(By.ID, "input_value")
    
    # Посчитать математическую функцию от x
    x = x_element.text
    y = calc(x)

    # Ввести ответ в текстовое поле.
    answer = browser.find_element(By.ID, "answer")
    answer.send_keys(y)

    # Отметить checkbox "I'm the robot".
    checkbox = browser.find_element(By.ID, "robotCheckbox")
    checkbox.click()

    # Выбрать radiobutton "Robots rule!".
    radiobutton = browser.find_element(By.ID, "robotsRule")
    radiobutton.click()

    # Нажать на кнопку Submit.
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

