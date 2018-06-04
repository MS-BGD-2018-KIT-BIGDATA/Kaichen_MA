#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 20 13:35:23 2017

@author: kaichenma
"""

import requests
from bs4 import BeautifulSoup
import json
import re
import pandas as pd


ibuprofene = requests.get("https://www.open-medicaments.fr/api/v1/medicaments?query=ibuprofene&api_key=ibuprofene").json()
print (ibuprofene)

for i in ibuprofene:
    url = "https://www.open-medicaments.fr/api/v1/medicaments/" + i['codeCIS']
    info = requests.get(url).json()
    print (info)
    print ("*****")
    code = info['codeCIS']
    dosage = info['denomination']
    
    price = info['presentations'][0]['prix']

    date = info['presentations'][0]['dateDeclarationCommercialisation']
    
    
    print (code, int(regex.findall(dosage)[0]), price, date)
    




