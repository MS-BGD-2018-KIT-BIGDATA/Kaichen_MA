import pandas as pd
import requests
from bs4 import BeautifulSoup

url = 'http://alize2.finances.gouv.fr/communes/eneuro/detail.php?icom=056&dep=075&type=BPS&param=5&exercice='
years = ['2010','2011','2012','2013','2014','2015']

def getSoupFromUrl(url, method='get', data={}):
    if method == 'get':
        res = requests.get(url)
    elif method =="post":
        res = requests.post(url, data=data)
    else:
        return None

    if res.status_code == 200:
        soup = BeautifulSoup(res.text, 'html.parser');
        #print(soup)
        return soup
    else:
        return None

def soup_year(year):
    url_year = url + year
    classname = 'montantpetit G'
    soup = getSoupFromUrl(url_year)

    all_content = soup.find_all(class_= classname)

    A = [int(content.text.strip().replace(' ', '')) for content in all_content[0:3]]
    B = [int(content.text.strip().replace(' ', '')) for content in all_content[3:6]]
    C = [int(content.text.strip().replace(' ', '')) for content in all_content[9:12]]
    D = [int(content.text.strip().replace(' ', '')) for content in all_content[12:15]]



    df_year = pd.DataFrame(A)
    df_year.index = ["En milliers d'euros", "Euros par habitant", "Moyenne de la strate"]
    df_year.columns = ['A']

    df_year['B'] = B
    df_year['C'] = C
    df_year['D'] = D

    return df_year


def get_soup_all():
    columns = ['A', 'B', 'C', 'D']

    df_ = pd.DataFrame(index=years, columns=columns)

    for year in years:
        df_tmp = soup_year(year)
        print(df_tmp)

    return df_

print(get_soup_all())
