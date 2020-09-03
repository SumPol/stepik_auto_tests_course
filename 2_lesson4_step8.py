from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try: 
    browser = webdriver.Chrome()

    browser.get("http://suninjuly.github.io/explicit_wait2.html")

    # Ищем кнопку "Забронировать"
    button1 = browser.find_element_by_id("book")

    # Ищем цену и ждем, когда она станет $100, в течении 12 секунд
    price = browser.find_element_by_id("price")
    price = WebDriverWait(browser, 12).until(EC.text_to_be_present_in_element((By.ID, "price"), "$100"))

    button1.click()

    # Решаем математическую задачу
    x_element = browser.find_element_by_id("input_value")
    x = x_element.text

    input1 = browser.find_element_by_id("answer")
    input1.send_keys(str(calc(x))) 

    # Отправляем форму
    button2 = browser.find_element_by_id("solve")
    button2.click()

    time.sleep(3)

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()