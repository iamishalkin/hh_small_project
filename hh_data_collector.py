# -*- coding: utf-8 -*-
"""
Created on Fri Sep 28 16:40:47 2018

@author: ivan.mishalkin
"""

#https://github.com/hhru/api/blob/master/docs/vacancies.md
import requests
import json
import pandas as pd

baseURL = 'https://api.hh.ru/'
headers = {'User-Agent': 'HH-User-Agent'}

vacancyURL = baseURL + 'vacancies'

vacancyURL_with_params = (vacancyURL + '?' 
                                     + 'per_page=100' #results per page
                                     + '&area=1' #Msk
                                     + '&area=2' #SPB
                                     + '&vacancy_type=open' #fresh vacancies
                                     + '&text=python' #search for python in vacancies
                                     + '&vacancy_search_field=description' #in descriptions
                                     + '&industry=7' #IT
)


def get_vacancies_url_list(url, headers={'User-Agent': 'HH-User-Agent'}):
    req = requests.get(url, headers=headers)
    if req.status_code != 200:
        raise()





dicts = requests.get('https://api.hh.ru/dictionaries', headers=headers)
dicts = json.loads(dicts.content)

req = requests.get(vacancyURL_with_params, headers=headers)

df = req.content
data = json.loads(req.content)
data2 = json.loads(data['items'])

df = pd.DataFrame(data['items'])

req.status_code ==200