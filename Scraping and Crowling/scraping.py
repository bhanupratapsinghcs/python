import requests
from bs4 import BeautifulSoup

rslt = requests.get("https://www.google.com/")
# ---------Resonse code---------
# print(rslt.status_code)
# print(rslt)

# ---------- content code---------
# print(rslt.headers)

src = rslt.content
# print(rslt.content)

# ------------ BeautifulSoup content

soup = BeautifulSoup(src, "lxml")

# --------- print the code in normal manner-----
# print(soup.prettify())

# ---------- first Occurrence of tab --------
# print(soup.p)
# print(soup.find("p"))

#  ---------------find all--------
lk = soup.find_all("a")
# print(lk)

for link in lk:
    if "About" in link.text:
        print(link)
        print(link.attrs['href'])
