from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import math
import time


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

try:
    # Открыть страницу http://suninjuly.github.io/explicit_wait2.html
    browser = webdriver.Chrome()

    browser.get("http://suninjuly.github.io/explicit_wait2.html")

    # Дождаться, когда цена дома уменьшится до $100 (ожидание нужно установить не меньше 12 секунд)
    price = WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "100")
    )
    
    # Нажать на кнопку "Book"
    button = browser.find_element(By.ID, "book")
    button.click()

    # Проскроллить страницу вниз.
    browser.execute_script("window.scrollBy(0, 200);")

    # Решить уже известную нам математическую задачу (используйте ранее написанный код) и отправить решение
    valuex = browser.find_element(By.ID, "input_value")
    y = calc(valuex.text)

    # Ввести ответ в текстовое поле.
    answer = browser.find_element(By.ID, "answer")
    answer.send_keys(y)

    # Нажать на кнопку Submit.
    button = browser.find_element(By.ID, "solve")
    button.click()

finally:
    time.sleep(10)
    browser.quit()

