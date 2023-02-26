import requests
import json

api_key = 'https://api.nasa.gov/planetary/apod?api_key=YspFPkpXyMYywZ2fmswRlWtFSRKeo01cQTjurnLS'


response = requests.get(api_key).text

jsondata = json.loads(response)

msg = f'''

Astronomy Picture of the Day! (APOD)

Copyright : {jsondata['copyright']}
Date : {jsondata['date']}

Case : {jsondata['explanation']}

Image Title : {jsondata['title']}
HD Url : {jsondata['hdurl']}

Service Version : {jsondata['service_version']}
Source Code Copyright : Reman Biswas 2023

'''

print(msg)
