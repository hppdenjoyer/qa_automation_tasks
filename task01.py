from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

link = "http://suninjuly.github.io/simple_form_find_task.html"
driver.get(link)
button = driver.find_element(By.ID, "submit_button")
button.click()

# закрываем браузер после всех манипуляций
driver.quit()
