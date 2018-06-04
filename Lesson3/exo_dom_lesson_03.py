import requests
from bs4 import BeautifulSoup
import pandas as pd
import json
import getpass
from requests.auth import HTTPBasicAuth
import functools

url = 'https://gist.github.com/paulmillr/2657075'

def getID():
    ID = input ("Entre your ID: ")
    ID = str (ID)
    password = getpass.getpass("Entre your password: ")
    return ID, password

def getSoupFromURL(url):
    res = requests.get(url)
    soup = BeautifulSoup(res.text, 'html.parser')
    return soup
    

def getStarName():
    soup = getSoupFromURL(url)
    if soup:
        starName = soup.find("table").find("tbody").find_all("tr")
    
    stars = []
    for line in starName:
        stars.append(line.find("a").text.strip())
    return stars
    
        
def getStarState(stars):
    
    res = requests.get('https://api.github.com/users/' + 'star' + '/repos', auth = HTTPBasicAuth('ID', 'password'))
    starContent = json.loads(res.text)
    reposNbr = len(starContent)
    starNbr = 0
    starNbr = sum([i['stargazers_count'] for i in starContent])
    starNote = round(float(starNbr) / float(reposNbr), 2)
    return starNote





ID, password = getID()
#print (ID, password)
soup = getSoupFromURL(url)
stars = getStarName()
print (stars)
for star in stars:
    starNote = getStarState(stars)
    print (star, ":", starNote)
