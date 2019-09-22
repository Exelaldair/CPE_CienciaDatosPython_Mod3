'''
Programa : Ciencia de Datos con Pthon
Modulo 03 : Estadística y Visualización de Datos con Python
Sesion 01 : Analisis de Datos con Python - Web Scraping
Library : requests
Fecha : 22/09/2019
Version : 1
Author : Jaime Gomez
'''

import requests

URL = "https://www.google.com/search"

params = {"q": "TECSUP" }

r = requests.get(URL, params=params)

print(r.text)



