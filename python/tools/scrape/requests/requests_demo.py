import requests

page = requests.get('https://python.org')

content = page.content

print(content)
