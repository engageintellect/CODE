import requests
import json
from pprint import *

URL = 'https://jsonplaceholder.typicode.com/comments'

response = requests.get(URL)

data = json.loads(response.text)

if not data:
    print('error')
else:
    print(data)
