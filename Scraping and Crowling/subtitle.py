import requests
import os
from bs4 import BeautifulSoup

movies_name = input().split()
s = "-".join(movies_name)

result = requests.get("https://subscene.com/subtitles/" + s + "/english")

print("https://subscene.com/subtitles/" + s + "/english")
print((result.status_code))
if result.status_code == 200:
    src = result.content

    soup = BeautifulSoup(src, "lxml")

    tr_list = soup.find_all("tr")
    if tr_list[1].td['class'] == ['empty']:
        print('subtitles Not Found')
    else:
        link_to_d_p = tr_list[1].td.a['href']

        result2 = requests.get("https://subscene.com" + (str(link_to_d_p))).content

        soup2 = BeautifulSoup(result2, 'lxml')

        a_lst = soup2.find_all("a", {"class": "button positive"})

        #  ----  Download_link ----

        Download_link = a_lst[0].attrs['href']

        result23 = requests.get("https://subscene.com" + (str(Download_link))).content
        # print("https://subscene.com" + (str(Download_link)))

        # ----------downloaded file-----------

        with open(s + ".zip", "wb") as f:
            f.write(result23)
else:
	print('Page Not Found')