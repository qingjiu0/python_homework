import os
import time
from selenium import webdriver
driver = webdriver.Chrome (executable_path="./chromedriver")
#打开微约日历官网
driver.get("http://www.wedate.me/")
#点击官网首页的"体验网页版""
login = driver.find_element_by_css_selector("#home > div > div > div > div > div > div > div.hidden-xs.hidden-sm > div:nth-child(2) > a")
login.click()
#切换至手机登陆
phone = driver.find_element_by_css_selector("#logintab > li:nth-child(2) > a")
phone.click()
# 加个等待时间
time.sleep(2) 
phonenum = driver.find_element_by_css_selector("#mobile")
phonenum.click()
phonenum.send_keys("13120926100")
pwd = driver.find_element_by_id('pwd_old')
pwd.click()
pwd.send_keys("123456")
phonelogin = driver.find_element_by_id('login')
phonelogin.click()

time.sleep(3) 
#新建日程
new = driver.find_element_by_class_name("addicon")
new.click()
schtitle = driver.find_element_by_id("schtitle")
time.sleep(1) 
schtitle.click()
time.sleep(1) 
schtitle.send_keys("单天时间段")
time.sleep(1) 
btnSavesch = driver.find_element_by_id("btnSavesch")
btnSavesch.click()
time.sleep(2)

#新建待办
todo = driver.find_element_by_css_selector("#myTab > li:nth-child(2) > a")
todo.click()
time.sleep(2)