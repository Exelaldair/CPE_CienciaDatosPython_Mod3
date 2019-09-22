'''
Programa : Ciencia de Datos con Pthon
Modulo 03 : Estadística y Visualización de Datos con Python
Sesion 01 : Analisis de Datos con Python - Web Scraping
Fecha : 22/09/2019
Version : 1
Author : Jaime Gomez
'''

import requests

URL = 'http://www.webscrapingfordatascience.com/basichttp/'
r = requests.get(URL)
print(r.text)
