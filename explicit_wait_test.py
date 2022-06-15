from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import math

browser = webdriver.Chrome()
browser.maximize_window()

link = 'http://suninjuly.github.io/explicit_wait2.html'
browser.get(link)
wait = WebDriverWait(browser, 15)
price = wait.until(
    EC.text_to_be_present_in_element((By.CSS_SELECTOR, '#price'), '$100')
)
btn = browser.find_element(By.CSS_SELECTOR, '#book').click()
def calc(get_x):
    return str(math.log(abs(12*math.sin(get_x))))
x = browser.find_element(By.CSS_SELECTOR, '#input_value')
get_x = int(x.text)
result = calc(get_x)
print(result)
answer = browser.find_element(By.CSS_SELECTOR, '#answer').send_keys(result)
submit = browser.find_element(By.CSS_SELECTOR, '#solve').click()
