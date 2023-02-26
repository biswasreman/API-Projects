import requests
import json

req = requests.get("http://api.open-notify.org/iss-now.json").text

obj = json.loads(req)

while True:

    enter = input("Please press enter to continue: ")

    msg = f"International Space Station Current Location:\n\nTimeStamp : {obj['timestamp']}\nLatitude : {obj['iss_position']['latitude']}\nLongitude :\
    {obj['iss_position']['longitude']}"

    api_key = f"https://api.callmebot.com/whatsapp.php?phone=918882488170&text={msg}&apikey=3544314"

    requests.get(api_key)
    print("check your call me bot!")
