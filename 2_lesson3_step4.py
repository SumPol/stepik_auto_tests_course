from selenium import webdriver
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try: 
    link = "http://suninjuly.github.io/alert_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Нажать на кнопку
    button1 = browser.find_element_by_css_selector("button.btn")
    button1.click()

    # Нажать на Ок alert-а
    confirm = browser.switch_to.alert
    confirm.accept()

    # Код, который заполняет поле
    x_element = browser.find_element_by_id("input_value")
    x = x_element.text

    input1 = browser.find_element_by_id("answer")
    input1.send_keys(str(calc(x)))
    

    # Отправляем форму
    button2 = browser.find_element_by_css_selector("button.btn")
    button2.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(3)

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()