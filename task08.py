from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math


def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))


try:
    # Открыть страницу http://suninjuly.github.io/get_attribute.html
    link = "http://suninjuly.github.io/get_attribute.html"
    browser = webdriver.Firefox()
    browser.get(link)

    # Найти на ней элемент-картинку, который является изображением сундука с сокровищами.
    treasure_img = browser.find_element(By.ID, "treasure")

    # Взять у этого элемента значение атрибута valuex, которое является значением x для задачи.
    valuex = treasure_img.get_attribute("valuex")
    
    # Посчитать математическую функцию от x
    y = calc(valuex)

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

