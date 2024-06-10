##################### Extra Hard Starting Project ######################

# 1. Update the birthdays.csv
import pandas
from datetime import datetime
import random
import smtplib

data = pandas.read_csv('birthdays.csv').to_dict(orient='records')


# 2. Check if today matches a birthday in the birthdays.csv

def check_date(user_date):
    obj = datetime.now()
    current_date = datetime(year=obj.year, month=obj.month, day=obj.day)
    if user_date == current_date:
        return True
    else:
        return False


# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

def pick_letter(names):
    n = random.randint(1, 3)
    letter_file = open(f"./letter_templates/letter_{n}.txt").read()
    x = letter_file.replace('[NAME]', names.strip())
    return x


# 4. Send the letter generated in step 3 to that person's email address.

def send_mail(messages, email_id):
    my_email = 'kalpeshdesale570@gmail.com'
    password = 'nnez uooi cymz qsun'

    with smtplib.SMTP('smtp.gmail.com', 587) as connection:
        connection.starttls()  # for secure connection
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email,
                            to_addrs=email_id,
                            msg=f'Subject:Birthday Wishes \n\n {messages}'
                            )


for i in range(0, len(data)):
    year = data[i]['year']
    month = data[i]['month']
    day = data[i]['day']
    name = data[i]['name']
    email = data[i]['email']
    user_date = datetime(day=day, year=year, month=month)
    if check_date(user_date):
        message = pick_letter(name)
        send_mail(message, email)
