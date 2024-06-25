import requests
from twilio.rest import Client

account_sid = 'ACf7f0dacd871f0ef1cfb0f31d00e27ecb'
auth_token = '053807720079e44e7133bd13545ea9e8'
api_key_weather_app = "bc1e38cde1d4b9f42d3220e44b7e19de"
end_point = "https://api.openweathermap.org/data/2.5/forecast?l"
latitude = 28.70405920
longitude = 77.10249020
weather_params = {
    "lat": latitude,
    "lon": longitude,
    "appid": api_key_weather_app,
}
response = requests.get(url=end_point, params=weather_params)
response.raise_for_status()
rain = False
for i in range(0, 12):
    data = response.json()['list'][i]['weather'][0]['id']
    if data < 700:
        rain = True
        break
if rain:
    client = Client(account_sid, auth_token)
    from_number = '+15643332122'
    to_number = '+919359775740'
    message_body = 'Bring Your Umbrella Today is rainy Day'
    message = client.messages.create(
        from_=from_number,
        body=message_body,
        to=to_number
    )

    print(message.status)
else:
    print('Its sunny Day')
