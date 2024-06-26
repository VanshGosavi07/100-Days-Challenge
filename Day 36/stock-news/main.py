import requests

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
stock_end_point = "https://www.alphavantage.co/query?"
stock_api_params = {
    "function": "TIME_SERIES_DAILY",
    "symbol": "IBM",
    "apikey": "HQ33EVHEOTJMP4WX"
}


def sms(messages):
    from twilio.rest import Client

    # Your Account SID and Auth Token from twilio.com/console
    account_sid = 'ACf7f0dacd871f0ef1cfb0f31d00e27ecb'
    auth_token = '053807720079e44e7133bd13545ea9e8'
    client = Client(account_sid, auth_token)

    # Phone numbers should be in string format and E.164 format
    from_number = '+15643332122'
    to_number = '+919359775740'
    message_body = messages

    message = client.messages.create(
        from_=from_number,
        body=message_body,
        to=to_number
    )

    print(message.sid)


response = requests.get(url=stock_end_point, params=stock_api_params)
response.raise_for_status()
data = response.json()['Time Series (Daily)']
data_value = [value for (key, value) in data.items()]
yesterday_closed_price = data_value[0]['4. close']
today_date = response.json()['Meta Data']['3. Last Refreshed']
print(yesterday_closed_price)

day_before_yesterday_price = data_value[1]['4. close']
print(day_before_yesterday_price)

difference = abs(float(yesterday_closed_price) - float(day_before_yesterday_price))

diff_percent = difference / float(yesterday_closed_price) * 100
print(diff_percent)

if diff_percent >= 5:
    news_end_point = "https://newsapi.org/v2/everything?"
    news_api_params = {
        "q": STOCK,
        "from": today_date,
        "sortBy": "publishedAt",
        "apikey": "465be5904a054965a01789ac85f63a4c"
    }
    response = requests.get(url=news_end_point, params=news_api_params)
    response.raise_for_status()
    news_data = response.json()["articles"][0]
    news_headline = news_data['title']
    news_brief = news_data['content']
    messages = f"\n\n\nTSLA: 🔺{diff_percent}%\n\nHeadline :{news_headline}\n\nBrief : {news_brief}\n"
    print(messages)
    sms(messages)
