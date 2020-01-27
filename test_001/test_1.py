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
dr = driver.find_element_by_xpath("//a[@class='dropdown-toggle']//i[@class='glyphicon glyphicon-user']")
dr.click()
fr = driver.find_element_by_xpath("//header[@class='main-header']//li[8]//a[1]")
fr.click()
cl = driver.find_element_by_xpath("//button[@class='btn btn-default']")
cl.click()
time.sleep(15)
g = driver.find_element_by_xpath("//span[@id='hm_lft_sdbar_span_Models']")
g.click()
time.sleep(5)
h = driver.find_element_by_xpath("//a[@id='hm_lp_vview']")
h.click()
time.sleep(10)

rows = len(driver.find_elements_by_xpath("//*[@id='center']/div/div[2]/div[2]/div/div/div"))
cols = len(driver.find_elements_by_xpath("//*[@id='center']/div/div[2]/div[2]/div/div/div[1]/div"))

print(rows)
print(cols)

for r in range(1,rows+1):
    for c in range(1,cols+1):
        value = driver.find_element_by_xpath("//*[@id='center']/div/div[2]/div[2]/div/div/div["+str(r)+"]/div["+str(c)+"]").text
        print(value,end='   ')
        print()
    print(    )



driver.close()
