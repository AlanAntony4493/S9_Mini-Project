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
        self.live_server_url = 'http://127.0.0.1:8000/register'

    def tearDown(self):
        self.driver.quit()

    def test_django_project_functionalities(self):
        driver = self.driver
        driver.get(self.live_server_url)
        driver.maximize_window()
        time.sleep(1)

        # Fill out the registration form
        fname = driver.find_element(By.ID, "fname")
        fname.send_keys("John")
        mname = driver.find_element(By.ID, "Mname")
        mname.send_keys("Middle")
        lname = driver.find_element(By.ID, "lname")
        lname.send_keys("Doe")
        # lname = driver.find_element(By.ID, "lname")
        # lname.send_keys("Doe")
        house_name = driver.find_element(By.ID, "Hname")
        house_name.send_keys("Main Street")

        # Select the prayer group (e.g., 'Gethsemane')
        prayer_group_dropdown = Select(driver.find_element(By.ID, "prayer-group"))
        prayer_group_dropdown.select_by_value("Gethsemane")

        dob = driver.find_element(By.ID, "dob")
        dob.send_keys("21-10-2001")

        # Select the gender (e.g., 'Male')
        gender_dropdown = Select(driver.find_element(By.ID, "gender"))
        gender_dropdown.select_by_value("male")

        email = driver.find_element(By.ID, "email")
        email.send_keys("john123@example.com")

        password = driver.find_element(By.ID, "password")
        password.send_keys("@jhon1234")

        confirm_password = driver.find_element(By.ID, "cpassw")
        confirm_password.send_keys("@jhon1234")

        phone = driver.find_element(By.ID, "mob")
        phone.send_keys("8746353727")

        submit_button = driver.find_element(By.XPATH, "//button[contains(text(), 'Sign Up')]")
        submit_button.click()
        time.sleep(2)

        
        print("Testing Success")

if __name__ == '__main__':
    import unittest
    unittest.main()
