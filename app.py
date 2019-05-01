import json
import urllib.request

with urllib.request.urlopen("http://data.nba.net/data/10s/prod/v1/2018/teams.json") as url:
    data = json.loads(url.read().decode())
    print(json.dumps(data, indent=4))

   

