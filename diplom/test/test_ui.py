from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By


chrome = webdriver.Chrome()

chrome.get("https://www.kinopoisk.ru/")

add_button = chrome.find_element(By.XPATH, '//input[@placeholder="Фильмы, сериалы, персоны"]'). click()


add_button = chrome.find_element(By.XPATH, '//button[@aria-label = "Меню"]'). click()


add_button = chrome.find_element(By.XPATH, '//a[@href = "/promo"]'). click()


add_button = chrome.find_element(By.XPATH, '//a[@href = "/games"]'). click()


add_button = chrome.find_element(By.XPATH, '//a[@class = "styles_root__o_aAP styles_rootActive__xFaoQ"]'). click()

chrome.switch_to.alert.accept()
