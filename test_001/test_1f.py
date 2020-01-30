import unittest
import time

from Tools.demo.ss1 import center
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import Select

driver = webdriver.Chrome(executable_path="C:\Program Files (x86)\chromedriver.exe")
driver.get("https://in.bookmyshow.com/bengaluru")
print(driver.title)
inputsearch=driver.find_element_by_xpath("//input[@name='inputSearchBox']")
inputsearch.click()
language=driver.find_element_by_xpath("//span[@data-filter-value='Telugu']")
language.click()
slnk=driver.find_element_by_xpath("//a[@data-id='ET00103955']")
slnk.click()
driver.close()