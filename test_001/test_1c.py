import unittest
import time

from Tools.demo.ss1 import center
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import Select

driver = webdriver.Chrome(executable_path="C:\Program Files (x86)\chromedriver.exe")

driver.get("https://www.flipkart.com/")
print(driver.title)
mobilenumber=driver.find_element_by_xpath("//input[@class='_2zrpKA _1dBPDZ']")
mobilenumber.click()
mobilenumber.send_keys("9581441090")
password=driver.find_element_by_xpath("//input[@class='_2zrpKA _3v41xv _1dBPDZ']")
password.click()
password.send_keys("Manoj@1996")
login=driver.find_element_by_xpath("//button[@class='_2AkmmA _1LctnI _7UHT_c']")
login.click()
time.sleep(5)
search=driver.find_element_by_xpath("//input[@placeholder='Search for products, brands and more']")
search.click()
search.send_keys("apple")
search1=driver.find_element_by_xpath("//body/div[@id='container']/div/div[@class='_3ybBIU']/div[@class='_1tz-RS']/div[@class='_3pNZKl']/div[@class='Y5-ZPI']/form[@class='_1WMLwI header-form-search']/div[@class='col-12-12 _2tVp4j']/button[@class='vh79eN']/*[1]")
search1.click()
time.sleep(5)
apple=driver.find_element_by_xpath("//div[contains(text(),'Apple iPhone 7 (Black, 32 GB)')]")
apple.click()
time.sleep(5)
manoj=driver.find_element_by_xpath("//body/div[@id='container']/div/div[@class='_3ybBIU']/div[@class='_1tz-RS']/div[@class='_3pNZKl']/div[3]/div[1]/*[1]")
manoj.click()
logout=driver.find_element_by_xpath("//body/div[@id='container']/div/div[@class='_3ybBIU']/div[@class='_1tz-RS']/div[@class='_3pNZKl']/div[3]/div[1]/div[1]/div[1]")
logout.click()
time.sleep(5)
search2=driver.find_element_by_xpath("//input[@placeholder='Search for products, brands and more']")
search2.click()
search2.send_keys("govindaa")
search3=driver.find_element_by_xpath("//body/div[@id='container']/div/div[@class='_3ybBIU']/div[@class='_1tz-RS']/div[@class='_3pNZKl']/div[@class='Y5-ZPI']/form[@class='_1WMLwI header-form-search']/div[@class='col-12-12 _2tVp4j']/button[@class='vh79eN']/*[1]")
search3.click()
logout1=driver.find_element_by_xpath("//body/div[@id='container']/div/div[@class='_3ybBIU']/div[@class='_1tz-RS']/div[@class='_3pNZKl']/div[3]/div[1]/*[1]")
logout1.click()


driver.close()