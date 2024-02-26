######### задание 4
# import time
# from selenium import webdriver
# from selenium.webdriver.support.select import Select
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
#
# driver = webdriver.Chrome("C:\chromedriver.exe")
# driver.maximize_window()
# driver.get("https://practice.automationtesting.in/")
# login = "awdw@gmail.com"
# password = "Gfhjkm904kqi864Ntcnjdsq"
# myacc = driver.find_element_by_id("menu-item-50")
# myacc.click()
# log_mail = driver.find_element_by_id("username")
# log_mail.send_keys(login)
# log_pass = driver.find_element_by_id("password")
# log_pass.send_keys(password)
# login_btn = driver.find_element_by_css_selector(".u-column1 p:nth-child(3) .button")
# login_btn.click()
# logout = driver.find_element_by_css_selector(".woocommerce li:nth-child(6)")
# logout_text = logout.text
# assert logout_text == "Logout"
# shop = driver.find_element_by_id("menu-item-40")
# shop.click()
# html_forms = driver.find_element_by_css_selector(".masonry-done > li:nth-child(3)")
# html_forms.click()
# h1 = driver.find_element_by_class_name("entry-title")
# h1_text = h1.text
# assert h1_text == "HTML5 Forms"

######## задание 5
# import time
# from selenium import webdriver
# from selenium.webdriver.support.select import Select
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
#
# driver = webdriver.Chrome("C:\chromedriver.exe")
# driver.maximize_window()
# driver.get("https://practice.automationtesting.in/")
# login = "awdw@gmail.com"
# password = "Gfhjkm904kqi864Ntcnjdsq"
# myacc = driver.find_element_by_id("menu-item-50")
# myacc.click()
# log_mail = driver.find_element_by_id("username")
# log_mail.send_keys(login)
# log_pass = driver.find_element_by_id("password")
# log_pass.send_keys(password)
# login_btn = driver.find_element_by_css_selector(".u-column1 p:nth-child(3) .button")
# login_btn.click()
# logout = driver.find_element_by_css_selector(".woocommerce li:nth-child(6)")
# logout_text = logout.text
# assert logout_text == "Logout"
# shop = driver.find_element_by_id("menu-item-40")
# shop.click()
# html = driver.find_element_by_link_text("HTML")
# html.click()
# items = driver.find_elements_by_css_selector(".masonry-done .product")
# assert len(items) == 3


######## задание 6
# import time
# from selenium import webdriver
# from selenium.webdriver.support.select import Select
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# driver = webdriver.Chrome("C:\chromedriver.exe")
# driver.maximize_window()
# driver.get("https://practice.automationtesting.in/")
# login = "awdw@gmail.com"
# password = "Gfhjkm904kqi864Ntcnjdsq"
# myacc = driver.find_element_by_id("menu-item-50")
# myacc.click()
# log_mail = driver.find_element_by_id("username")
# log_mail.send_keys(login)
# log_pass = driver.find_element_by_id("password")
# log_pass.send_keys(password)
# login_btn = driver.find_element_by_css_selector(".u-column1 p:nth-child(3) .button")
# login_btn.click()
# logout = driver.find_element_by_css_selector(".woocommerce li:nth-child(6)")
# logout_text = logout.text
# assert logout_text == "Logout"
# shop = driver.find_element_by_id("menu-item-40")
# shop.click()
# selector = driver.find_element_by_class_name("orderby")
# selector_check = selector.get_attribute("value")
# assert selector_check == "menu_order"
# select = Select(selector)
# select.select_by_value('price-desc')
# selector = driver.find_element_by_class_name("orderby")
# selector_check = selector.get_attribute("value")
# assert selector_check == "price-desc"

######## задание 7
# import time
# from selenium import webdriver
# from selenium.webdriver.support.select import Select
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
#
# driver = webdriver.Chrome("C:\chromedriver.exe")
# driver.maximize_window()
# driver.get("https://practice.automationtesting.in/")
# login = "awdw@gmail.com"
# password = "Gfhjkm904kqi864Ntcnjdsq"
# myacc = driver.find_element_by_id("menu-item-50")
# myacc.click()
# log_mail = driver.find_element_by_id("username")
# log_mail.send_keys(login)
# log_pass = driver.find_element_by_id("password")
# log_pass.send_keys(password)
# login_btn = driver.find_element_by_css_selector(".u-column1 p:nth-child(3) .button")
# login_btn.click()
# logout = driver.find_element_by_css_selector(".woocommerce li:nth-child(6)")
# logout_text = logout.text
# assert logout_text == "Logout"
# shop = driver.find_element_by_id("menu-item-40")
# shop.click()
# android = driver.find_element_by_css_selector(".post-169 h3")
# android.click()
# old_price = driver.find_element_by_css_selector(".price > del > span")
# old_price_text = old_price.text
# new_price = driver.find_element_by_css_selector(".price > ins > span")
# new_price_text = new_price.text
# assert old_price_text == "₹600.00"
# assert new_price_text == "₹450.00"
# book_cover = WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.CSS_SELECTOR,".images .attachment-shop_single")))
# book_cover.click()
# close = WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".pp_close")))
# close.click()


####### задание 8
# import time
# from selenium import webdriver
# from selenium.webdriver.support.select import Select
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
#
# driver = webdriver.Chrome("C:\chromedriver.exe")
# driver.maximize_window()
# driver.get("https://practice.automationtesting.in/")
# shop = driver.find_element_by_id("menu-item-40")
# shop.click()
# driver.execute_script('window.scrollBy(0, 600)')
# html5 = driver.find_element_by_css_selector(".post-182 .add_to_cart_button")
# html5.click()
# time.sleep(1)
# item_cart = driver.find_element_by_css_selector(".wpmenucart-contents .cartcontents")
# item_cart_text = item_cart.text
# assert item_cart_text == "1 item"
# price_cart = driver.find_element_by_css_selector(".wpmenucart-contents .amount")
# price_cart_text = price_cart.text
# assert price_cart_text == "₹180.00"
# cart = driver.find_element_by_class_name("added_to_cart")
# cart.click()
# Subtotal = WebDriverWait(driver,10).until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".cart-subtotal .woocommerce-Price-amount"),"₹180.00"))
# Total = WebDriverWait(driver,10).until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".order-total .woocommerce-Price-amount"), "₹183.60"))

###### задание 9
# import time
# from selenium import webdriver
# from selenium.webdriver.support.select import Select
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
#
# driver = webdriver.Chrome("C:\chromedriver.exe")
# driver.maximize_window()
# driver.get("https://practice.automationtesting.in/")
# shop = driver.find_element_by_id("menu-item-40")
# shop.click()
# driver.execute_script('window.scrollBy(0, 600)')
# html5 = driver.find_element_by_css_selector(".post-182 .add_to_cart_button")
# html5.click()
# time.sleep(1)
# JS = driver.find_element_by_css_selector(".post-180 .add_to_cart_button")
# JS.click()
# time.sleep(1)
# cart = driver.find_element_by_class_name("added_to_cart")
# cart.click()
# time.sleep(1)
# remove_first = driver.find_element_by_css_selector(".cart_item:nth-child(1) .remove")
# remove_first.click()
# time.sleep(2)
# undo = driver.find_element_by_link_text("Undo?")
# undo.click()
# quantity = driver.find_element_by_css_selector(".cart_item:nth-child(2) .quantity > input")
# quantity.clear()
# quantity.send_keys(3)
# update_cart = driver.find_element_by_css_selector(".actions .button:nth-child(2)")
# update_cart.click()
# time.sleep(1)
# quantity = driver.find_element_by_css_selector(".cart_item:nth-child(2) .quantity > input")
# quantity_check = quantity.get_attribute("value")
# assert quantity_check == "3"
# apply_coupon = driver.find_element_by_css_selector(".actions .coupon .button")
# apply_coupon.click()
# time.sleep(1)
# error = driver.find_element_by_class_name("woocommerce-error")
# error_text = error.text
# assert error_text == "Please enter a coupon code."


####### задание 10
import time
from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome("C:\chromedriver.exe")
driver.maximize_window()
driver.get("https://practice.automationtesting.in/")
shop = driver.find_element_by_id("menu-item-40")
shop.click()
driver.execute_script('window.scrollBy(0, 300)')
html5 = driver.find_element_by_css_selector(".post-182 .add_to_cart_button")
html5.click()
time.sleep(1)
cart = driver.find_element_by_class_name("added_to_cart")
cart.click()
time.sleep(1)
checkout_check = WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".wc-proceed-to-checkout .button")))
checkout = driver.find_element_by_css_selector(".wc-proceed-to-checkout .button")
checkout.click()
first_name_check = WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.ID, "billing_first_name")))
first_name = driver.find_element_by_id("billing_first_name")
first_name.send_keys("Test1")
last_name = driver.find_element_by_id("billing_last_name")
last_name.send_keys("Test2")
email = driver.find_element_by_id("billing_email")
email.send_keys("Test3@m.com")
phone = driver.find_element_by_id("billing_phone")
phone.send_keys("98544")
country = driver.find_element_by_id("select2-chosen-1")
country.click()
time.sleep(1)
country_search = driver.find_element_by_id("s2id_autogen1_search")
country_search.send_keys("Netherlands")
time.sleep(1)
country_select = driver.find_element_by_class_name("select2-match")
country_select.click()
driver.execute_script('window.scrollBy(0, 300)')
adress = driver.find_element_by_id("billing_address_1")
adress.send_keys("Test5")
postcode = driver.find_element_by_id("billing_postcode")
postcode.send_keys("test6")
town = driver.find_element_by_id("billing_city")
town.send_keys("test7")
driver.execute_script('window.scrollBy(0, 800)')
time.sleep(2)
payments = driver.find_element_by_id("payment_method_cheque")
payments.click()
order = driver.find_element_by_id("place_order")
order.click()
thanks = WebDriverWait(driver,10).until(EC.text_to_be_present_in_element((By.CLASS_NAME, "woocommerce-thankyou-order-received"), "Thank you. Your order has been received."))
method = WebDriverWait(driver,10).until(EC.text_to_be_present_in_element((By.CLASS_NAME, "method"),"Check Payments"))