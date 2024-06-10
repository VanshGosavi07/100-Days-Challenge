# import smtplib
#
# my_email = 'kalpeshdesale570@gmail.com'
# password = 'nnez uooi cymz qsun'
#
# with smtplib.SMTP('smtp.gmail.com',587) as connection:
#     connection.starttls()  # for secure connection
#     connection.login(user=my_email, password=password)
#     connection.sendmail(from_addr=my_email,
#                         to_addrs='vanshgosavi7@gmail.com',
#                         msg='Subject:Hello\n\n without port This is the body of my email'
#                         )
import random

# from datetime import datetime
#
# now = datetime.now()
# print(now)
# print(now.year)
#
# new = datetime(day=25, year=2005, month=1, hour=8, minute=10,)
# print(new)


import pandas
import smtplib
from datetime import datetime

now = datetime.now()
day = now.day

with open('quotes.txt') as file:
    quote_li = file.readlines()
    quotes = random.choice(quote_li)

if day == 10:
    my_email = 'kalpeshdesale570@gmail.com'
    password = 'nnez uooi cymz qsun'

    with smtplib.SMTP('smtp.gmail.com', 587) as connection:
        connection.starttls()  # for secure connection
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email,
                            to_addrs='vanshgosavi7@gmail.com',
                            msg=f'Subject:Nice Quotes\n\n {quotes}'
                            )
