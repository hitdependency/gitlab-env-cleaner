import json
import requests

headers = {'PRIVATE-TOKEN': ${token}}
url = 'https://gitlab.btc-s.ru/api/v4/projects/19/environments'

r = requests.get(url, headers=headers).json()

for env in r:
    url_del = 'https://gitlab.btc-s.ru/api/v4/projects/19/environments/%d/stop' % env["id"]
    requests.post(url_del, headers)
    print("deleted" env["id"])
