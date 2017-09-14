# -*- coding: utf-8 -*-
"""
Created on Tue May 31 16:32:02 2016

@author: james.bradley
"""

import requests

from lxml import objectify


num_periods = "6"
state_id = "44"
division = "0"
parameter = "tavg"
num_months = "6"
year = "2016"

template_base = 'https://www.ncdc.noaa.gov/temp-and-precip/climatological'
template_base = template_base + '-rankings/download.xml?parameter='

template_add = '%s&state=%s&div=%s&month=%s&'
template_add = template_add +'periods[]=%s&year=%s'
insert_these = (parameter,state_id,division,num_months,num_periods,year)
template_add = template_add % insert_these

url = template_base + template_add

response = requests.get(url).content
root = objectify.fromstring(response)

my_wm_username = 'jemills'

print my_wm_username
print root["data"]["value"] #value
print root["data"]["twentiethCenturyMean"] #twentiethCenturyMean
print root["data"]["lowRank"] #lowRank 
print root["data"]["highRank"] #highRank
