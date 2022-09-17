# Fetch API

import requests
import json
res = requests.get('https://jsonplaceholder.typicode.com/posts')


results = json.loads(res.text)
for i in results:
    print(f"ID: {i['userId']} Title: {i['title']}")


