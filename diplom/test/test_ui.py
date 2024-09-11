from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

chrome = webdriver.Chrome()

chrome.get("https://www.kinopoisk.ru/lists/categories/movies/8/")

add_button = chrome.find_element(By.XPATH, '//button[text()="Жанры"]'). click()
