import sys
import urllib.request
import json
import time

from playsound import playsound


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
        print("\033[1;32m" + user_data["id"] + " is online!" + "\033[1;0m")
        playsound('assets/staffordgambittime.mp3')
    else : 
        print("\033[1;31m" + "NOT online" + "\033[1;0m" )

def main():
    user = input("Enter lichess username to track: ")

    while True:
        user_data = get_user_data(user)
        check_if_online(user_data)
        time.sleep(60)


main()