import urllib.request
import json

contents = urllib.request.urlopen("http://lichess.org/api/users/status?ids=capibarazul").read()
contents = contents.decode('utf8').replace("'", '"')
data = json.loads(contents)

if "online" in data[0].keys() and data[0]["online"] == True:
    print("oaaees is online!")
else : 
    print("not online")

