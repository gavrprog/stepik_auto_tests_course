from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import math
import time

def calc(x):
    return math.log(abs(12 * math.sin(x)))

try:
    link = "http://suninjuly.github.io/explicit_wait2.html"
    browser = webdriver.Chrome()
    browser.get(link)

    button = WebDriverWait(browser, 13).until(
        EC.text_to_be_present_in_element((By.ID, "price"), '$100')
    )
    browser.find_element(By.ID, 'book').click()

    nummer = browser.find_element(By.ID, 'input_value').text
    answer=calc(int(nummer))
    browser.find_element(By.ID, 'answer').send_keys(str(answer))

    browser.find_element(By.ID, 'solve').click()

    answer=browser.switch_to.alert.text
    print(answer)
    browser.switch_to.alert.accept()
finally:
    
    time.sleep(5)
    browser.quit()
