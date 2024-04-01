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

        # Login
        username = driver.find_element(By.ID, "username")
        username.send_keys("accountant@gmail.com")
        password = driver.find_element(By.ID, "password")
        password.send_keys("@lan4493")
        submit_button = driver.find_element(By.ID, "submit")
        submit_button.click()
        # time.sleep(2)

        self.live_server_url = 'http://127.0.0.1:8000/accounts/'
        
        driver.get(self.live_server_url)
        # date = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "date")))
        # date.send_keys("21-03-2024")
        # time.sleep(5)
        # Wait for the date input element to be present
        date_input = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "date")))

        # Execute JavaScript to set the date value
        date = "2024-04-01"  # Make sure to adjust the format if needed
        driver.execute_script("arguments[0].value = arguments[1]", date_input, date)

        # Optionally, trigger any onchange events after setting the date
        driver.execute_script("validateTransactionDate()")
        time.sleep(2)

        category_dropdown = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "description")))
        Select(category_dropdown).select_by_value("Food")
        time.sleep(2)

        description = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "specifyTransaction")))
        description.send_keys("Groceries for the week")
        time.sleep(2)

        credit = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "credit")))
        credit.send_keys("50")
        time.sleep(2)

        # debit = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "debit")))
        # debit.send_keys("0")
        # time.sleep(2)

        bill_number = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "billNumber")))
        bill_number.send_keys("184")
        time.sleep(2)

        # Instead of clicking on a button with text, find the submit button by ID
        submit_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "transactionForm")))
        submit_button.submit()
        time.sleep(2)

        # # # Wait for the success message or page reload
        # # WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, "successMessage")))

        # # Wait for the button to be clickable
        # submit_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CLASS_NAME, "button1")))

        # # Click the button
        # submit_button.click()

        print("Testing Success")

if __name__ == '__main__':
    import unittest
    unittest.main()

