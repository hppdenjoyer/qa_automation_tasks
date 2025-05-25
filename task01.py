from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

link = "http://suninjuly.github.io/simple_form_find_task.html"
driver.get(link)
button = driver.find_element(By.ID, "submit_button")
driver.click()

# закрываем браузер после всех манипуляций
driver.quit()
