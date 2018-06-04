#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 18 18:55:23 2017

@author: kaichenma
"""

import requests
from bs4 import BeautifulSoup
import json
import re
#import json

region=["ile_de_france","aquitaine","provence_alpes_cote_d_azur"]
versions=r'life|intens|zen'

def getRegionUrl():
    for i in range(len(region)):
        region_=region[i]
        url='https://www.leboncoin.fr/voitures/offres/'+region_+'/?th=1&brd=Renault&mdl=Zoe'
        print(url)
    return url

def getSoupFromURL(url):
    res = requests.get(url)
    soup = BeautifulSoup(res.text, 'html.parser')
    #print(soup)
    return soup

def getCarUrl():
    soup = getSoupFromURL(url)
    if soup:
        carList=soup.find_all("a", class_="list_item clearfix trackable")
        #print(carUrl)
        url_content = ["http:" + carList['href'] for carList in carList]
        #print(url_content)
        return url_content
def getCarInfo():
    #url_car='https://www.leboncoin.fr/voitures/1320868333.htm?ca=12_s'
    #url_car = ...
    soup_car=getSoupFromURL(url_car)
    #print(soup_car)
    model=soup_car.find_all("span", class_="value")[3].text.strip()
    price=soup_car.find_all("span", class_="value")[0].text.strip()
    kilo=soup_car.find_all("span", class_="value")[5].text.strip()
    year=soup_car.find_all("span", class_="value")[4].text.strip()
    version=soup_car.find_all("p",class_="value")[0].text.strip().lower()
    version=re.search(versions,version)
    seller=soup_car.find_all("p", class_="title")[0].text.strip()
    print(model,price,kilo,year,version,seller)
    
    
getRegionUrl()      
getSoupFromURL(url)
url_content=getCarUrl()
#print(region)
#getCarInfo()
#list=[]
#print(len(url_content))

for i in range(len(region)):
    region_=region[i]
    url='https://www.leboncoin.fr/voitures/offres/'+region_+'/?th=1&brd=Renault&mdl=Zoe'
    #print(url)
    getRegionUrl()      
    getSoupFromURL(url)
    url_content=getCarUrl()
    for j in range(len(url_content)):
        url_car=url_content[j]
        getCarInfo()
#
#getCarInfo()

