
import requests
from bs4 import BeautifulSoup
import json

url = 'https://lespoir.jimdo.com/2015/03/05/classement-des-plus-grandes-villes-de-france-source-insee/'


def getSoupFromURL(url):
    res = requests.get(url)
    soup = BeautifulSoup(res.text, 'html.parser')
    #print(soup)
    return soup

def getCity():
    soup = getSoupFromURL(url)
    if soup:
        cityContent = soup.find("table").find_all("tr")[1:]
    cities = list(map(lambda s: s.text.split()[1], cityContent))
    #print(cities)
    return cities
    
    


def distance():
    #origins = 'Paris'
    #destinations ='Rennes'
        
    url_city='https://maps.googleapis.com/maps/api/distancematrix/json?origins=' + origins + '&destinations=' + destinations + '&key=' + 'AIzaSyDAov8fvju9KiVUQE8dQ-vAcYAtLpnM9PI'
    res_city = requests.get(url_city)
    if res_city:
        distance_content = json.loads(res_city.text)
        distance = distance_content["rows"][0]["elements"][0]["distance"]["value"]
        #print(distance_content)
    else:
        print("Not found.")
    
        
    print (float(distance))

getSoupFromURL(url)
cities=getCity()
origins = cities
destinations = cities
for i in range(100):
    origins = cities[i]
    for j in range(100):
        destinations = cities[j]
        print(origins,destinations,":")
        distance()
  
#        
    