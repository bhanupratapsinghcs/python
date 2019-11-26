from selenium import webdriver
import time

username = "181500191"
password = "ELAW"

driver = webdriver.Chrome("C:/Users/Bhanu/Desktop/chromedriver_win32/chromedriver.exe")

driver.get("http://glauniversity.in:8083/StudentHome")
time.sleep(3)
driver.maximize_window()
time.sleep(2)
driver.find_element_by_id("cboxClose").click()

elem = driver.find_element_by_id("txt_user_name")
time.sleep(3)
elem.send_keys(username)

elem = driver.find_element_by_id("txt_password")
elem.send_keys(password)

driver.find_element_by_id("btn_login").click()
time.sleep(3)

elems = driver.find_elements_by_xpath('//*[@id="Ul1"]/li[10]/ul/li[2]/a')
sub = ""
for elem in elems:
    sub = elem.get_attribute("href")

driver.get(sub)
