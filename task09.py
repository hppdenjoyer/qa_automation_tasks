from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

try:
    # Открыть страницу https://suninjuly.github.io/selects1.html
    link = "https://suninjuly.github.io/selects1.html"
    browser = webdriver.Firefox()
    browser.get(link)

    # Посчитать сумму заданных чисел
    num_1 = browser.find_element(By.ID, "num1").text
    num_2 = browser.find_element(By.ID, "num2").text
    answer = int(num_1) + int(num_2)

    # Выбрать в выпадающем списке значение равное расчитанной сумме
    select = Select(browser.find_element(By.ID, "dropdown"))
    select.select_by_value(str(answer))

    # Нажать кнопку "Submit"
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit() 

