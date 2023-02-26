import requests
import json

category_name = 'technology'

api = f'https://inshorts.deta.dev/news?category={category_name}'

i = 0

while i >= 0:


    enter = input("Press enter for next news: ")
    response = requests.get(api).text
    jsondata = json.loads(response)
    date = jsondata['data'][i]['date']
    content = jsondata['data'][i]['content']
    msg = f"Date : {date}\nNews {i}: {content}"
    api_key = f"https://api.callmebot.com/whatsapp.php?phone=918882488170&text={msg}&apikey=3544314"
    requests.get(api_key)
    print("check your call me bot!")
    i = i + 1


