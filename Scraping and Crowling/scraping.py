# import requests
# from bs4 import BeautifulSoup

# rslt = requests.get("https://www.google.com/")
# # ---------Resonse code---------
# # print(rslt.status_code)
# # print(rslt)

# # ---------- content code---------
# # print(rslt.headers)

# src = rslt.content
# # print(rslt.content)

# # ------------ BeautifulSoup content

# soup = BeautifulSoup(src, "lxml")

# # --------- print the code in normal manner-----
# # print(soup.prettify())

# # ---------- first Occurrence of tab --------
# # print(soup.p)
# # print(soup.find("p"))

# #  ---------------find all--------
# lk = soup.find_all("a")
# # print(lk)

# for link in lk:
#     if "About" in link.text:
#         print(link)
#         print(link.attrs['href'])

from selenium import webdriver
# # For using sleep function because selenium
# # works only when the all the elements of the
# # page is loaded.
# import time
# # webdriver path set
# browser = webdriver.Chrome("C:/Users/Bhanu/Desktop/chromedriver_win32/chromedriver.exe")

# # To maximize the browser window
# browser.maximize_window()

# # zomato link set
# browser.get('https://www.zomato.com')

# time.sleep(3)
# # Enter your user name and password here.
# username = "test"
# password = "test"


# # signin element clicked
# browser.find_element_by_xpath("//a[@id ='signin-link']").click()
# time.sleep(2)

# # Login clicked
# browser.find_element_by_xpath("//a[@id ='login-email']").click()

# # username send
# a = browser.find_element_by_xpath("//input[@id ='ld-email']")
# a.send_keys(username)

# # password send
# b = browser.find_element_by_xpath("//input[@id ='ld-password']")
# b.send_keys(password)

# # submit button clicked
# browser.find_element_by_xpath("//input[@id ='ld-submit-global']").click()

# print('Login Successful')
# # browser.close()

print(help(webdriver))
