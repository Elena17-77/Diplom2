from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
#from selenium.webdriver.chrome.service import Service
#from webdriver_manager.chrome import ChromeDriverManager

def test_kinopoisk():
  chrome = webdriver.Chrome()
  #service=Service(ChromeDriverManager().install())


  chrome.get("https://www.kinopoisk.ru/")
  #позитивные тесты
  input_field = chrome.find_element(By.CSS_SELECTOR, 'input[placeholder = "Фильмы, сериалы, персоны"]')
  input_field.send_keys('шрек')
  input_field.clear()

  chrome.find_element(By.CSS_SELECTOR, 'input[placeholder = "Фильмы, сериалы, персоны"]')
  input_field.send_keys('А')
  input_field.clear()

  chrome.find_element(By.CSS_SELECTOR, 'input[placeholder = "Фильмы, сериалы, персоны"]')
  input_field.send_keys('2')
  input_field.clear()

#негативные тесты
  chrome.find_element(By.CSS_SELECTOR, 'input[placeholder = "Фильмы, сериалы, персоны"]')
  input_field.send_keys(' ')
  input_field.clear()

  chrome.find_element(By.CSS_SELECTOR, 'input[placeholder = "Фильмы, сериалы, персоны"]')
  input_field.send_keys('-')
  input_field.clear()

  chrome.quit()