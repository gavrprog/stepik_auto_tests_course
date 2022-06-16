from selenium import webdriver
from selenium.webdriver.common.by import By
import time 

try:
    link = "http://suninjuly.github.io/registration2.html"
    browser = webdriver.Chrome()
    browser.get(link)

    input1 = browser.find_element(
        By.CSS_SELECTOR, "input.first:required").send_keys("Ivan")
    input2 = browser.find_element(
        By.CSS_SELECTOR, "input.second:required").send_keys("Petrov")
    input3 = browser.find_element(
        By.CSS_SELECTOR, "input.third:required").send_keys("Smolensk")
    button = browser.find_element(By.CSS_SELECTOR, "button.btn").click()

    time.sleep(2)
    welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
    welcome_text = welcome_text_elt.text

    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    
    time.sleep(2)
    browser.quit()
