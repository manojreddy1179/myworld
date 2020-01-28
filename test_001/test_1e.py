import unittest
import time

from Tools.demo.ss1 import center
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import Select

driver = webdriver.Chrome(executable_path="C:\Program Files (x86)\chromedriver.exe")
driver.get("https://www.google.com")
print(driver.title)
searchb=driver.find_element_by_xpath("//*[@id='tsf']/div[2]/div[1]/div[1]/div/div[2]/input")
searchb.click()
searchb.send_keys("gmail login")
gsearch=driver.find_element_by_xpath("//*[@id='tsf']/div[2]/div[1]/div[3]/center/input[1]")
gsearch.click()
time.sleep(5)
gmail=driver.find_element_by_xpath("//*[@id='rso']/div[1]/div/div[2]/div/div/div[1]/a/h3")
gmail.click()
time.sleep(5)
mail=driver.find_element_by_xpath("//*[@id='identifierId']")
mail.click()
mail.send_keys("manojreddy1179@gmail.com")
next1=driver.find_element_by_xpath("//*[@id='identifierNext']/span/span")
next1.click()
time.sleep(3)
password=driver.find_element_by_xpath("//*[@id='password']/div[1]/div/div[1]/input")
password.click()
password.send_keys("8121041996")
next2=driver.find_element_by_xpath("//*[@id='passwordNext']/span/span")
next2.click()
time.sleep(3)
driver.close()