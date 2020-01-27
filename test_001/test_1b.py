import unittest
import time

from Tools.demo.ss1 import center
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import Select

driver = webdriver.Chrome(executable_path="C:\Program Files (x86)\chromedriver.exe")
driver.get("https://rauat.modeloncloud.com/umg-admin/login")
print(driver.title)
login = driver.find_element_by_xpath("//input[@id='j_username']")
time.sleep(2)
login.send_keys("sysadmin")
p = driver.find_element_by_xpath("//input[@id='j_password']")
p.click()
time.sleep(2)
p.send_keys("Welcome1")
sub = driver.find_element_by_xpath("//p[@class='login button']//a//input")
sub.click()
time.sleep(15)


signout=driver.find_element_by_xpath("//a[@id='Logged_user_name']")
signout.click()
time.sleep(5)
sign=driver.find_element_by_xpath("//a[@id='logout']")
sign.click()
time.sleep(5)



driver.close()
