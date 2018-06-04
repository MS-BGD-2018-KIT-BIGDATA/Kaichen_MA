import requests
from bs4 import BeautifulSoup


url_acer = 'https://www.cdiscount.com/informatique/ordinateurs-pc-portables/acer-pc-portable-aspire-e5-774g-57p5-17-3-hd-ra/f-10709-aspiree5774g58j0.html?idOffre=154236317#mpos=6|cd'
url_dell = 'https://www.cdiscount.com/informatique/ordinateurs-pc-portables/dell-netbook-latitude-7350-m-5y71-13-3-core-m/f-10709-dell7350m5y71.html#mpos=1|cd'
def getSoupFromURL(url):
    res = requests.get(url)
    soup = BeautifulSoup(res.text, 'html.parser')
    print(soup)
    return soup

def getProductPrice(soup):
    PriceIni = soup.find_all(class_="fpStriked")[-1].text.strip(' €*').replace(',','.')
    PriceReal = soup.find_all(class_="fpPrice price")[-1].text.replace('€','.')
    #print (PrinceIni)
    Percent_re = (float(PriceIni) - float(PriceReal)) / float(PriceReal)*100
    return PriceIni, PriceReal, Percent_re


soup = getSoupFromURL(url_acer)
PriceIni, PriceReal, Percent_re = getProductPrice(soup)
print ("The initial price of Acer is:", PriceIni, "€")
print ("Its new price is:", PriceReal, "€")
print ("Its rebate is: %.2f" % Percent_re + "%")

soup = getSoupFromURL(url_dell)
PriceIni, PriceReal, Percent_re = getProductPrice(soup)
print ("\n\nThe initial price of Dell is:", PriceIni, "€")
print ("Its new price is:", PriceReal, "€")
print ("Its rebate is: %.2f" % Percent_re + "%")
