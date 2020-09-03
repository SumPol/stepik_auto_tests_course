from selenium import webdriver
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try: 
    link = "http://SunInJuly.github.io/execute_script.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Код, который считывает значение x
    x_element = browser.find_element_by_id("input_value")
    x = x_element.text

    # Код, который скроллит страницу вниз на 120 пикселей
    browser.execute_script("window.scrollBy(0, 120);")

    # Ввод ответа, рассчитанного по формуле, в поле
    input1 = browser.find_element_by_id("answer")
    input1.send_keys(str(calc(x)))
    
    # Код, который нажимает checkbox и radiobutton
    option1 = browser.find_element_by_css_selector("[for='robotCheckbox']")
    option1.click()

    option2 = browser.find_element_by_css_selector("[for='robotsRule']")
    option2.click()

    # Отправляем форму
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(3)

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()