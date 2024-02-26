import time
from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome("C:\chromedriver.exe")
driver.maximize_window()
driver.get("https://practice.automationtesting.in/")
login = "awdw@gmail.com"
password = "Gfhjkm904kqi864Ntcnjdsq"
myacc = driver.find_element_by_id("menu-item-50")
myacc.click()

#### задание 2
# reg_mail = driver.find_element_by_id("reg_email")
# reg_mail.send_keys(login)
# reg_pass = driver.find_element_by_id("reg_password")
# reg_pass.send_keys(password)
# reg = driver.find_element_by_css_selector(".u-column2 p:nth-child(4)")
# reg.click()

#### задание 3
log_mail = driver.find_element_by_id("username")
log_mail.send_keys(login)
log_pass = driver.find_element_by_id("password")
log_pass.send_keys(password)
login_btn = driver.find_element_by_css_selector(".u-column1 p:nth-child(3) .button")
login_btn.click()
logout = driver.find_element_by_css_selector(".woocommerce li:nth-child(6)")
logout_text = logout.text
assert logout_text == "Logout"

