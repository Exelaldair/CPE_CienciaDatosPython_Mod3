'''

library requests

'''


import requests

URL = 'http://www.webscrapingfordatascience.com/basichttp/'
r = requests.get(URL)
print(r.text)
