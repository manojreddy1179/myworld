from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import Select

driver=webdriver.Chrome(executable_path="C:\Program Files (x86)\chromedriver.exe")
a=driver
a.get("https://www.facebook.com")
print(a.title)
email=a.find_element_by_xpath("//input[@id='email']")
email.click()
email.send_keys("9581441090")
password=a.find_element_by_xpath("//input[@id='pass']")
password.click()
password.send_keys("9581441090")
login=a.find_element_by_xpath("//input[@id='u_0_b']")
login.click()
time.sleep(10)
a.close()