# -*- coding: utf-8 -*-
"""
Created on Fri Sep 28 16:40:47 2018

@author: ivan.mishalkin
"""

import requests
import json

baseURL = 'https://api.hh.ru/'
headers = {'User-Agent': 'HH-User-Agent'}

vacancyURL = baseURL + 'vacancies'

vacancyURL_with_params = vacancyURL + '?' + \
                                      'area=1' + \ #Moscow
                                      'area=2' + \ #SPB
                                      'vacancy_type=open' #+\ #fresh vacancies
                                      

dicts = requests.get('https://api.hh.ru/dictionaries', headers=headers)
dicts = json.loads(dicts.content)

req = requests.get(vacancyURL, headers=headers)


