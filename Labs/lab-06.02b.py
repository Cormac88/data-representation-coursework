import requests
import urllib.parse
from config import apiKey
import json

url = 'https://api.github.com/repos/your-username/aprivateone'

filename = "repos-private.json"

response = requests.get(url, auth=('token', apiKey))

repoJSON = response.json()

with open(filename, 'w') as fp:
    json.dump(repoJSON, fp, indent=4)
