# Download the helper library from https://www.twilio.com/docs/python/install

import os
from twilio.rest import Client

# Set environment variables for your credentials
# Read more at http://twil.io/secure

account_sid = "ACccbf646482d7d5dfb32a448be0fd4091"
auth_token = "33b6eaa04604a4e0a6ec119d902f9644"
client = Client(account_sid, auth_token)

name = input("Enter your name: ")

msg = f"Hello {name} your OTP is 9954"


message = client.messages.create(
  body=f"{msg}",
  from_="+12762658670",
  to="+918882488170"
)

print(message.sid)