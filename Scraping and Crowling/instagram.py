import sys
sys.path.append("E:\\Data\\Programs\\python")
import config
from selenium.webdriver.support import ui
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time

username = config.user
password = config.pwrd

driver = webdriver.Chrome("C:/Users/Bhanu/Desktop/chromedriver_win32/chromedriver.exe")

driver.get("https://www.instagram.com/accounts/login/")
time.sleep(3)
# driver.maximize_window()
time.sleep(2)

elem = driver.find_element_by_xpath('/html/body/div[1]/section/main/div/article/div/div[1]/div/form/div[2]/div/label/input')
time.sleep(3)
elem.send_keys(username)

elem = driver.find_element_by_xpath("/html/body/div[1]/section/main/div/article/div/div[1]/div/form/div[3]/div/label/input")
elem.send_keys(password)

driver.find_element_by_xpath("/html/body/div[1]/section/main/div/article/div/div[1]/div/form/div[4]").click()
time.sleep(3)
ui.WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".aOOlW.HoLwm"))).click()
time.sleep(2)
driver.find_element_by_xpath("/html/body/div[1]/section/nav/div[2]/div/div/div[3]/div/div[5]/a/img").click()
time.sleep(2)
driver.find_elements_by_xpath("/html/body/div[1]/section/main/div/header/section/ul/li[2]/a").click()
time.sleep(2)
