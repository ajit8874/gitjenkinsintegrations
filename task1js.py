# from selenium import webdriver



import time

from selenium import webdriver
from selenium.webdriver.support.select import Select

from selenium.webdriver.common.action_chains import ActionChains

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

driver = webdriver.Chrome("/home/ajitsingh/Python/chromedriver_linux64/chromedriver")
driver.maximize_window()

driver.execute_script("window.open('https://qa-candidates.phenompeople.com/dashboard/candidates','_self')")

time.sleep(5)

element = "document.getElementById('username').value = 'teresa.vulluri@phenompeople.com'"
driver.execute_script(element)
print(element)

btn = "document.getElementsByClassName('btn-primary-signin')[0].click()"
driver.execute_script(btn)

time.sleep(5)
password = "document.getElementById('phenomPassword3').value= 'Devqa123!@#'"
driver.execute_script(password)
print(password)

sign_in_btn = "document.getElementsByClassName('btn-primary-sign-in')[0].click()"
driver.execute_script(sign_in_btn)

print("x")

time.sleep(10)
driver.find_element_by_xpath("//div[text()='Phenomenal']").click()

time.sleep(4)
setting_btn = "document.getElementsByClassName('pp-ds-only-icon-button pp-ds-only-icon-button__primary')[2].click()"
driver.execute_script(setting_btn)

time.sleep(10)
driver.find_element_by_xpath("//a[text()='Scheduling Preferences']").click()

time.sleep(10)
driver.find_element_by_class_name("checkbox-label-sched").click()

time.sleep(10)
driver.find_element_by_class_name("expand-hide-arrow").click()


time.sleep(10)
driver.find_element_by_xpath("//span[text()='12:00 AM']").click()


time.sleep(5)
driver.find_element_by_xpath("//div[text()='05:00 PM']").click()
time.sleep(5)
driver.find_element_by_xpath("//span[text()='01:00 AM']").click()

time.sleep(4)
add_btn = "document.getElementsByClassName('slot-icon ng-star-inserted')[0].click()"
driver.execute_script(add_btn)

driver.find_element_by_id('copySlots').click()

time.sleep(4)
drp_mon = "document.getElementsByClassName('form-check-label')[2].click()"
driver.execute_script(drp_mon)

time.sleep(4)
drp_tue = "document.getElementsByClassName('form-check-label')[3].click()"
driver.execute_script(drp_tue)

time.sleep(4)
drp_wed = "document.getElementsByClassName('form-check-label')[4].click()"
driver.execute_script(drp_wed)

time.sleep(4)
drp_thur = "document.getElementsByClassName('form-check-label')[5].click()"
driver.execute_script(drp_thur)

time.sleep(4)
drp_fri = "document.getElementsByClassName('form-check-label')[6].click()"
driver.execute_script(drp_fri)

time.sleep(4)
drp_sat = "document.getElementsByClassName('form-check-label')[7].click()"
driver.execute_script(drp_sat)

driver.find_element_by_xpath("//div[text()='Apply']").click()
