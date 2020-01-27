import unittest
import time

from Tools.demo.ss1 import center
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import Select

driver = webdriver.Chrome(executable_path="C:\Program Files (x86)\chromedriver.exe")

driver.get("https://www.makemytrip.com/bus-tickets/")
print(driver.title)
login=driver.find_element_by_xpath("//p[contains(text(),'Login or Create Account')]")
login.click()
email=driver.find_element_by_xpath("//input[@id='username']")
email.click()
email.send_keys("9581441090")
continue1=driver.find_element_by_xpath("//span[contains(text(),'Continue')]")
continue1.click()
time.sleep(3)
time.sleep(30)
login=driver.find_element_by_xpath("//span[contains(text(),'Login')]")
login.click()
time.sleep(5)
bangalore=driver.find_element_by_xpath("//input[@id='fromCity']")
bangalore.click()
time.sleep(3)
fromcity=driver.find_element_by_xpath("//input[@placeholder='From']")
fromcity.click()
fromcity.send_keys("Bangalore")
bglr=driver.find_element_by_xpath("//p[contains(text(),'Bangalore, India')]")
bglr.click()
search=driver.find_element_by_xpath("//a[contains(@class,'primaryBtn font24 latoBlack widgetSearchBtn')]")
search.click()
time.sleep(5)
driver.close()