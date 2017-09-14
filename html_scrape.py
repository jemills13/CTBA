# -*- coding: utf-8 -*-
"""
Created on Wed Jun 21 11:02:01 2017

@author: jemills
"""

import requests
from bs4 import BeautifulSoup as bsoup
    
my_wm_username = 'jemills'
search_url = 'http://publicinterestlegal.org/county-list/'
response = requests.get(search_url, headers={
            "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36"}).content

parsed_html = bsoup(response, "lxml")

targets = parsed_html.find_all('section', attrs={'id' : 'content'})

for row in targets:
   tr = row.find_all('tr')
   new_list1 = []
   body = row.find_all("strong")
   for z in body:
       new_list1.append(z.text)
          

#print(new_list1)

my_result_list = []
new_list = []
count = 0

for i in new_list1:
    new_list.append(i)
    count += 1
    if count == 3:
        count = 0
        my_result_list.append(new_list)
        new_list = []

print my_wm_username
print len(my_result_list)
print my_result_list
