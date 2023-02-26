import requests
import json

while True:

    api_url = "https://cat-fact.herokuapp.com/facts/random"

    response = requests.get(api_url).text

    facts = json.loads(response)

    random_facts = facts['text']

    msg = f'''
Here's your cat fact:

{random_facts}
    '''


    enter = input("Press enter to get facts: ")

    api_key = f"https://api.callmebot.com/whatsapp.php?phone=918882488170&text={msg}&apikey=3544314"

    requests.get(api_key)
    print("check your call me bot!")








# api_url = "https://cat-fact.herokuapp.com/facts"

# response = requests.get(api_url).text


# facts = json.loads(response)

# cat_facts = facts[0]['text']

# print(facts)

# print(cat_facts)
