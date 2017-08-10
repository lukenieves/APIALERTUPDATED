# /usr/bin/env python
# Download the twilio-python library from http://twilio.com/docs/libraries
from twilio.rest import Client

# Find these values at https://twilio.com/user/account
account_sid = "ACcb1c67b106ce5c18fbd51cbe9f7af2ba"
auth_token = "017f1c0c8f3e0a950f36704a6693f0d7"
client = Client(account_sid, auth_token)

message = client.api.account.messages.create(to="+19174020767",
                                             from_="+16464617136",
                                             body="This is a test")