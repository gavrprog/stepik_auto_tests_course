from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
    return math.log(abs(12 * math.sin(x)))

try:
    link = "http://suninjuly.github.io/redirect_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)

    browser.find_element(By.TAG_NAME, 'button').click()
    fenster = browser.window_handles[1]
    browser.switch_to.window(fenster)
    nummer = browser.find_element(By.ID, 'input_value').text
    answer = calc(int(nummer))
    browser.find_element(By.ID, 'answer').send_keys(str(answer))

    browser.find_element(By.CLASS_NAME, 'btn').click()

    answer = browser.switch_to.alert.text
    print(answer)
    browser.switch_to.alert.accept()

finally:
    
    time.sleep(5)
    browser.quit()
