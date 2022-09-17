
import requests
import json
res = requests.get('https://jsonplaceholder.typicode.com/posts')


results = json.loads(res.text)

for x in results:
    print(x['title'])





