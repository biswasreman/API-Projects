import json
import requests

app_id = "356f288a"
app_key = "5e0a0a6f47ea6a6c04cfa0b76335073d"
endpoint = "entries"
language_code = "en-us"

print("Welcome to Oxford Dictionary by Reman...")

while True:
    put = input("Enter a word: ")
    url = "https://od-api.oxforddictionaries.com/api/v2/" +endpoint + "/" + language_code + "/" + put.lower()
    response = requests.get(url, headers={"app_id": app_id, "app_key": app_key}).text
    meaning = json.loads(response)
    define = meaning.get('results')[0].get('lexicalEntries')[0].get('entries')[0].get('senses')[0].get("definitions")[0]


    msg = f'''
Your given word is: {put.capitalize()}

{define}
    '''

    api_key = f"https://api.callmebot.com/whatsapp.php?phone=918882488170&text={msg}&apikey=3544314"
    requests.get(api_key)
    print("check your call me bot!")




# print("code {}\n".format(r.status_code))
# print("text \n" + r.text)
# print("json \n" + json.dumps(r.json()))
