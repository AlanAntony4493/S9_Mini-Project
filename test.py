# from datetime import datetime
# from django.test import TestCase
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# import time
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC

# class Hosttest(TestCase):
#     def setUp(self):
#         self.driver = webdriver.Chrome()
#         self.driver.implicitly_wait(10)
#         self.live_server_url = 'http://127.0.0.1:8000/'

#     def tearDown(self):
#         self.driver.quit()

#     def test_02_registration_and_login(self):
#         driver = self.driver
#         driver.get(self.live_server_url)
#         driver.maximize_window()
#         time.sleep(1)

#         login_link = driver.find_element(By.CSS_SELECTOR, "#login")
#         login_link.click()
#         time.sleep(2)

#         username = driver.find_element(By.CSS_SELECTOR, "input#username")
#         username.send_keys("alanantony96696@gmail.com")
#         password = driver.find_element(By.CSS_SELECTOR, "input#password")
#         password.send_keys("@Lan4493")
#         time.sleep(1)

#         submit_button = driver.find_element(By.CSS_SELECTOR, "button#submit")
#         submit_button.click()
#         time.sleep(2)

#         # Navigate to the career forum page
#         driver.get("http://127.0.0.1:8000/career_forum")
#         time.sleep(2)

#         # Locate and fill out the form fields
#         title_field = driver.find_element(By.ID, "questionTitle")
#         title_field.send_keys("How are you doing hai")

#         description_field = driver.find_element(By.ID, "questionDescription")
#         description_field.send_keys("Steps Summarize your problem in a one-line title. Describe your problem in more detail.Include any additional details.Review your question and post it to the site. You’re ready to ask a career-related question, and this form will help guide you through the process.")
#         additional_details_field = driver.find_element(By.ID, "additionalDetails")
#         additional_details_field.send_keys("Additional details for the question ggg.")
#         time.sleep(1)

#         submit_button = driver.find_element(By.CSS_SELECTOR, "input#sub")
#         submit_button.click()
#         # time.sleep(2)

#         # submitc = driver.find_element(By.CSS_SELECTOR, "a#logout")
#         # submitc.click()
#         # time.sleep(2)

#         print("Test done successfully")

# if __name__ == '_main_':
#     import unittest
#     unittest.main()



from datetime import datetime
from django.test import TestCase
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class Hosttest(TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)
        self.live_server_url = 'http://127.0.0.1:8000/'

    def tearDown(self):
        self.driver.quit()

    def test_django_project_functionalities(self):
        driver = self.driver
        driver.get(self.live_server_url)
        driver.maximize_window()
        time.sleep(1)

        # Navigate to the user index page
        driver.get(self.live_server_url + '/index')
        time.sleep(2)

        # Click on the login link
        login_link = driver.find_element(By.CSS_SELECTOR, "#login")
        login_link.click()
        time.sleep(2)

        # Navigate to the login page
        login_page_url = driver.current_url

        # Enter credentials (email and password)
        username = driver.find_element(By.CSS_SELECTOR, "input#username")
        username.send_keys("SmymAdmin@2023")
        password = driver.find_element(By.CSS_SELECTOR, "input#password")
        password.send_keys("@lan4493")
        time.sleep(1)

        submit_button = driver.find_element(By.CSS_SELECTOR, "button#submit")
        submit_button.click()
        time.sleep(2)

        # Check if successfully redirected to the home page
        assert driver.current_url != login_page_url, "Login failed"

        # Click on the "Users" button
        users_button = driver.find_element(By.CSS_SELECTOR, "#users")
        users_button.click()
        time.sleep(2)

        # Click on the "Approval" button
        approval_button = driver.find_element(By.CSS_SELECTOR, "#activate")
        approval_button.click()
        time.sleep(2)

        # Click on the "Logout" button
        logout_button = driver.find_element(By.CSS_SELECTOR, "#logout-button")
        logout_button.click()
        time.sleep(2)

        # Check if successfully logged out
        assert "Login" in driver.page_source, "Logout failed"

if __name__ == '__main__':
    import unittest
    unittest.main()
