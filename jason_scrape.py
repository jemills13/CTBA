# -*- coding: utf-8 -*-
"""
Created on Thu Sep 01 07:57:10 2016

@author: james.bradley
"""

import requests

shots_made = 0
shots_missed = 0
shots_attempted = 0
jump_shots = 0

search_url = 'http://buckets.peterbeshai.com/api/?player=201939&season=2015'
              
response = requests.get(search_url, headers={
            "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36"})

for shot in response.json():
    if shot["ACTION_TYPE"] == "Jump Shot":
        jump_shots += 1
        if shot["EVENT_TYPE"] == "Made Shot":
            shots_made += 1
        elif shot["EVENT_TYPE"] == "Missed Shot":
            shots_missed += 1

shots_made = float(shots_made)
shots_attempted = float(shots_attempted)

wm_username = "jemills"
print(wm_username)
print(jump_shots)
print int(shots_made)
print round(shots_made/jump_shots * 100,2)
"""
– Your W&M username (this doesn’t come from the web page)
– Number of shots categorized as “Jump Shot”
– The number of those jump shots that Stephen Curry made, which were classified as a
“Made Shot”
– The percentage of the attempted “Jump Shots” which were classified as “Made Shot”
"""
    

#http://buckets.peterbeshai.com/api/?player=201935&season=2015
#give counts for both, and ask for percentage
#if percentage is 0.000, you need to float at least one of the twos

