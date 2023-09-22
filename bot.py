import sys
import urllib.request
import json

def validate_data(user, user_data):
    if len(user_data) == 0 :
        print("ERROR: " + user + " is not a valid user on lichess!")
        sys.exit()
    else :
        return user_data[0]

def get_user_data(user):
    request = urllib.request.urlopen("http://lichess.org/api/users/status?ids=" + user).read()
    request = request.decode('utf8').replace("'", '"')
    data = json.loads(request)

    return validate_data(user, data)

def check_if_online(user_data):
    if "online" in user_data.keys() and user_data["online"] == True:
        print(user_data["id"] + " is online!")
    else : 
        print("NOT online")

def main():
    user = input("Enter lichess username to track: ")
    user_data = get_user_data(user)
    check_if_online(user_data)

main()