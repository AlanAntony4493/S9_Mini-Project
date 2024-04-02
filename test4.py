from django.test import TestCase
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
import time

class Hosttest(TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)
        self.live_server_url = 'http://127.0.0.1:8000/login'

    def tearDown(self):
        self.driver.quit()

    def test_django_project_functionalities(self):
        driver = self.driver
        driver.get(self.live_server_url)
        driver.maximize_window()
        time.sleep(1)

        username = driver.find_element(By.CSS_SELECTOR, "input#username")
        username.send_keys("alanantony96696@gmail.com")
        password = driver.find_element(By.CSS_SELECTOR, "input#password")
        password.send_keys("@Lan4493")
        time.sleep(3)
        submit_button = driver.find_element(By.CSS_SELECTOR, "button#submit")
        submit_button.click()
        time.sleep(2)

        # Find the element with ID "services"
        services_link = driver.find_element(By.LINK_TEXT, "Services")
        services_link.click()
        time.sleep(4)

        # Navigate to the parish directory page
        blood_donors_link = driver.find_element(By.CSS_SELECTOR, "#directory")
        blood_donors_link.click()
        time.sleep(2)

        select_element = driver.find_element(By.ID, "filter-prayer-group-select")
        select = Select(select_element)
        select.select_by_value("kana")
        # Logout from the session
        time.sleep(5)


        logout_button = driver.find_element(By.CSS_SELECTOR, "a#logout")
        logout_button.click()
        time.sleep(2)

        print("Testing Success")

if __name__ == '__main__':
    import unittest
    unittest.main()
