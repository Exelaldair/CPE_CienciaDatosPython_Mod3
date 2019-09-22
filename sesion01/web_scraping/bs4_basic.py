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

URL = 'https://en.wikipedia.org/w/index.php?title=List_of_Game_of_Thrones_episodes&oldid=802553687'

r = requests.get(URL)
html_contents = r.text
html_soup = BeautifulSoup(html_contents, 'html.parser')

# Find the first h1 tag
first_h1 = html_soup.find('h1')
print(first_h1.name) # h1
print(first_h1.contents) # ['List of ', [...], ' episodes']
print(str(first_h1))