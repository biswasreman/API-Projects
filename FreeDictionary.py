import requests
import json


while True:
    try:

        word = input("Enter a word: ")
        api_key = "https://api.dictionaryapi.dev/api/v2/entries/en/" + word
        response = requests.get(api_key).text
        jsondata = json.loads(response)
        msg = jsondata[0]['meanings'][0]['definitions'][0]['definition']
        api_key = f"https://api.callmebot.com/whatsapp.php?phone=918882488170&text=your+given+word+is+{word.title()}+\n\n+{msg}&apikey=3544314"
        requests.get(api_key)
        print("check your call me bot!")

    except:

        print("Sorry, We don't have that word!")
