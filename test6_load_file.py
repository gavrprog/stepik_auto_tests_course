from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os

try:
    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)

    browser.find_element(By.NAME, "firstname").send_keys('Z')
    browser.find_element(By.NAME, "lastname").send_keys('z')
    browser.find_element(By.NAME, "email").send_keys('z')

    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, 'proba.txt')
    browser.find_element(By.ID, "file").send_keys(file_path)

    browser.find_element(By.CLASS_NAME, 'btn').click()
        

finally:
    
    time.sleep(5)
    browser.quit()
