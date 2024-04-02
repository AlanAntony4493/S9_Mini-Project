import time
from django.test import TestCase
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class FormTest(TestCase):

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

        # Login
        username = driver.find_element(By.ID, "username")
        username.send_keys("alanantony96696@gmail.com")
        password = driver.find_element(By.ID, "password")
        password.send_keys("@Lan4493")
        submit_button = driver.find_element(By.ID, "submit")
        submit_button.click()
        time.sleep(2)

        # Navigate to career guidance form
        self.live_server_url = 'http://127.0.0.1:8000/career_forum/'  # Adjust URL if needed
        driver.get(self.live_server_url)

        # Fill in the form fields
        title_input = driver.find_element(By.ID, "questionTitle")
        title_input.send_keys("Test Title")

        description_input = driver.find_element(By.ID, "questionDescription")
        description_input.send_keys("Steps Summarize your problem in a one-line title. Describe your problem in more detail. Include any additional details. Review your question and post it to the site.")

        additional_details_input = driver.find_element(By.ID, "additionalDetails")
        additional_details_input.send_keys("Test Additional Details")

        # Submit the form
        submit_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "sub")))
        submit_button.submit()

        time.sleep(3)

        print("Testing Success")

if __name__ == '__main__':
    import unittest
    unittest.main()
