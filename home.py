import time
from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome("C:\chromedriver.exe")
driver.maximize_window()
driver.get("https://practice.automationtesting.in/")
driver.execute_script('window.scrollBy(0, 600)')
ruby = driver.find_element_by_class_name("post-160")
ruby.click()
driver.execute_script('window.scrollBy(0, 600)')
review = driver.find_element_by_class_name("reviews_tab")
review.click()
star5 = driver.find_element_by_class_name("star-5")
star5.click()
comment = driver.find_element_by_id("comment")
comment.send_keys("Nice book!")
author = driver.find_element_by_id("author")
author.send_keys("tester")
email = driver.find_element_by_id("email")
email.send_keys("kjdn@mail.com")
submit = driver.find_element_by_class_name("submit")
submit.click()


