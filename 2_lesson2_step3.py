from selenium import webdriver
import time
from selenium.webdriver.support.ui import Select

def calc(x, y):
  return str(x + y)

try: 
    link = "http://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Код, который берет значения для расчета
    x = browser.find_element_by_id("num1")
    y = browser.find_element_by_id("num2")

    # Выбор значения суммы
    sum_field = Select(browser.find_element_by_tag_name("select"))
    sum_field.select_by_visible_text(calc(int(x.text), int(y.text)))

    # Пример подстановки значения в строку 
    #sum_nums = (calc(int(x.text), int(y.text)))
    #sum_field.select_by_visible_text('{}'.format(sum_nums))
    
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