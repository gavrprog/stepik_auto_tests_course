from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math
from selenium.webdriver.support.ui import Select

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = "http://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)

    number1 = browser.find_element(By.ID, "num1").text
    number2 = browser.find_element(By.ID, "num2").text

    summa = int(number1) + int(number2)
    select = Select(browser.find_element(By.ID, "dropdown"))
    select.select_by_value(str(summa))

    browser.find_element(By.CSS_SELECTOR, "button.btn").click()


finally:
    
    time.sleep(5)
    browser.quit()
