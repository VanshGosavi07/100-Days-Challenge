import smtplib

import requests
from bs4 import BeautifulSoup

header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 Edg/126.0.0.0",
    "Accept-Language": "en-US,en;q=0.9,de-DE;q=0.8,de;q=0.7",
}
response = requests.get(url="https://www.amazon.com/dp/B075CYMYK6?psc=1&ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6",
                        headers=header)
data = response.text

soup = BeautifulSoup(data, "html.parser")
price = soup.find(class_="a-offscreen").get_text()
price_without_currency = price.split("$")[1]
final_price = float(price_without_currency)

if final_price < 100:
    with smtplib.SMTP('smtp.gmail.com', 587) as connection:
        connection.starttls()  # for secure connection
        connection.login(user="kalpeshdesale570@gmail.com", password="nnez uooi cymz qsun")
        connection.sendmail(from_addr="kalpeshdesale570@gmail.com",
                            to_addrs='vanshgosavi7@gmail.com',
                            msg=f'Subject:Shopping Time \n\n current price is ${final_price}'
                            )
