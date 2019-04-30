import json
import urllib


url = "http://data.nba.net/data/10s/prod/v1/2018/teams.json"
response = urllib.urlopen(url)
data = json.loads(response.read())


print(json.dumps(data, indent=4))
   

