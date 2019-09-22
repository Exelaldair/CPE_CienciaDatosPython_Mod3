'''


'''

import requests

def search(keyword):
 url = 'https://www.google.com/search'
 params = {'q': keyword }
 r = requests.get(url, params=params)
 return r.text

print(search('TECSUP'))



