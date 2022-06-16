from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math
from selenium.webdriver.support.ui import Select

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = "http://SunInJuly.github.io/execute_script.html"
    browser = webdriver.Chrome()
    browser.get(link)

    number = browser.find_element(By.ID, "input_value").text

    summa = str(calc(number))
    browser.find_element(By.ID, 'answer').send_keys(summa)

    browser.find_element(By.ID, 'robotCheckbox').click()
    radio_bt = browser.find_element(By.ID, 'robotsRule')
    browser.execute_script(
      'return arguments[0].scrollIntoView(true);', radio_bt)
    radio_bt.click()
    
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    #browser.execute_script(
      # "return arguments[0].scrollIntoView(true);", button)
    button.click()


finally:
    
    time.sleep(1)
    browser.quit()
