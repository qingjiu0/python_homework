import os
from selenium import webdriver
driver = webdriver.Chrome (executable_path="./chromedriver")
driver.get("http://www.wedate.me/")
login = driver.find_element_by_css_selector("#home > div > div > div > div > div > div > div.hidden-xs.hidden-sm > div:nth-child(2) > a")
login.click()
phonelogin = driver.find_element_by_css_selector("#logintab > li:nth-child(2) > a")
phonelogin.click()
text = driver.find_element_by_css_selector("#mobile")
text.click()
