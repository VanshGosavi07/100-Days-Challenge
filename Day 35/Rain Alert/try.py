from twilio.rest import Client

# Your Account SID and Auth Token from twilio.com/console
account_sid = 'ACf7f0dacd871f0ef1cfb0f31d00e27ecb'
auth_token = '053807720079e44e7133bd13545ea9e8'
client = Client(account_sid, auth_token)

# Phone numbers should be in string format and E.164 format
from_number = '+15643332122'
to_number = '+919359775740'
message_body = 'Bring Your Umbrella Today is rainy Day'

message = client.messages.create(
    from_=from_number,
    body=message_body,
    to=to_number
)

print(message.sid)
