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
#默认月视图点击+新建日程
addicon = driver.find_element_by_class_name("addicon")
addicon.click()
schtitle = driver.find_element_by_id("schtitle")
time.sleep(1) 
schtitle.click()
time.sleep(1) 
schtitle.send_keys("月_单天时间")
time.sleep(1) 
btnSavesch = driver.find_element_by_id("btnSavesch")
btnSavesch.click()
time.sleep(2)

#切换周视图
button_周 = driver.find_element_by_css_selector("#mycalendar > div.fc-toolbar > div.fc-left > button.fc-agendaWeek-button.fc-button.fc-state-default.fc-corner-left.fc-corner-right")
button_周.click()
time.sleep(2)
#周视图点击+新建日程
addicon = driver.find_element_by_class_name("addicon")
addicon.click()
schtitle = driver.find_element_by_id("schtitle")
time.sleep(1) 
schtitle.click()
time.sleep(1) 
schtitle.send_keys("周_单天时间")
time.sleep(1) 
btnSavesch = driver.find_element_by_id("btnSavesch")
btnSavesch.click()
time.sleep(2)


#切换列表视图
button_列表 = driver.find_element_by_css_selector("#mycalendar > div.fc-toolbar > div.fc-left > button.fc-listMonth-button.fc-button.fc-state-default.fc-corner-left.fc-corner-right")
button_列表.click()
time.sleep(2)
#列表视图点击+新建日程
addicon = driver.find_element_by_class_name("addicon")
addicon.click()
schtitle = driver.find_element_by_id("schtitle")
time.sleep(1) 
schtitle.click()
time.sleep(1) 
schtitle.send_keys("列表_单天时间")
time.sleep(1) 
btnSavesch = driver.find_element_by_id("btnSavesch")
btnSavesch.click()
time.sleep(2)

#新建待办
todo = driver.find_element_by_css_selector("#myTab > li:nth-child(2) > a")
todo.click()
time.sleep(2)
addtodo = driver.find_element_by_id("addtodo")
addtodo.click()
time.sleep(1) 
todotitle = driver.find_element_by_id("todotitle")
todotitle.click()
time.sleep(1)
todotitle.send_keys("新建待办00234")
time.sleep(1)
savetodo = driver.find_element_by_id("savetodo")
savetodo.click()
time.sleep(2)



