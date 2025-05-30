from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import unittest


class TestRegistration(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()

    def test_registration1(self):
        self.browser.get("http://suninjuly.github.io/registration1.html")
        self.browser.find_element(By.CSS_SELECTOR, ".first_block input.first").send_keys("Ivan")
        self.browser.find_element(By.CSS_SELECTOR, ".first_block input.second").send_keys("Petrov")
        self.browser.find_element(By.CSS_SELECTOR, ".first_block input.third").send_keys("test@gmail.com")
        self.browser.find_element(By.CSS_SELECTOR, "button.btn").click()
        welcome_text = self.browser.find_element(By.TAG_NAME, "h1").text
        self.assertEqual("Congratulations! You have successfully registered!", welcome_text)

    def test_registration2(self):
        self.browser.get("http://suninjuly.github.io/registration2.html")
        self.browser.find_element(By.CSS_SELECTOR, ".first_block input.first").send_keys("Ivan")
        self.browser.find_element(By.CSS_SELECTOR, ".first_block input.second").send_keys("Petrov")
        self.browser.find_element(By.CSS_SELECTOR, ".first_block input.third").send_keys("test@gmail.com")
        self.browser.find_element(By.CSS_SELECTOR, "button.btn").click()
        welcome_text = self.browser.find_element(By.TAG_NAME, "h1").text
        self.assertEqual("Congratulations! You have successfully registered!", welcome_text)

    def tearDown(self):
        time.sleep(10)
        self.browser.quit()


if __name__ == "__main__":
    unittest.main()
