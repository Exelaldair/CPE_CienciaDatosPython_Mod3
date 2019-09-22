'''


'''

import requests

URL = "https://www.google.com/search"

params = {"q": "TECSUP" }

r = requests.get(URL, params=params)

print(r.text)



