from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


try:
    # Открыть страницу http://suninjuly.github.io/redirect_accept.html
    link = "http://suninjuly.github.io/redirect_accept.html"
    browser = webdriver.Firefox()
    browser.get(link)

    # Нажать на кнопку
    button = browser.find_element(By.CSS_SELECTOR, "button[type='submit']")
    button.click()

    # Переключиться на новую вкладку
    redirect_page = browser.window_handles[1]
    browser.switch_to.window(redirect_page)

    # Ждем 1 секунду
    time.sleep(2)
    
    # На новой странице решить капчу для роботов, чтобы получить число с ответом
    valuex = browser.find_element(By.ID, "input_value")
    y = calc(valuex.text)
    # Ввести ответ в текстовое поле.
    answer = browser.find_element(By.ID, "answer")
    answer.send_keys(y)
    # Нажать на кнопку Submit.
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

