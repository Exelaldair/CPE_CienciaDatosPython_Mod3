'''
Programa : Ciencia de Datos con Pthon
Modulo 03 : Estadística y Visualización de Datos con Python
Sesion 01 : Analisis de Datos con Python - Web Scraping
Library : beautifulsoap4
Fecha : 22/09/2019
Version : 1
Author : Jaime Gomez
'''

import requests
from bs4 import BeautifulSoup

url = 'https://finance.yahoo.com/'

r = requests.get(url)
html_contents = r.text
html_soup = BeautifulSoup(html_contents, 'html.parser')

aref_nasdaq = html_soup.find('a', title="Nasdaq")
nasdaq = float(aref_nasdaq.find("span").contents[0].replace(',',''))
print(nasdaq)

aref_gold = html_soup.find('a', title="Gold")
gold = float(aref_gold.find("span").contents[0].replace(',',''))
print(gold)

aref_silver = html_soup.find('a', title="Silver")
silver = float(aref_silver.find("span").contents[0].replace(',',''))
print(silver)
