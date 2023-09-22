import urllib.request
import json

user = input("Enter lichess username to track: ")

contents = urllib.request.urlopen("http://lichess.org/api/users/status?ids=" + user).read()
contents = contents.decode('utf8').replace("'", '"')
data = json.loads(contents)

if "online" in data[0].keys() and data[0]["online"] == True:
    print(user + " is online!")
else : 
    print("not online")

