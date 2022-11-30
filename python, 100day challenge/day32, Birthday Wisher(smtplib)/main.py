##################### Extra Hard Starting Project ######################

# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.

import pandas as pd
import smtplib
from email.mime.text import MIMEText
import datetime as dt
import random
import os

now = dt.datetime.now()
month = now.month
day = now.day

birthday_csv = pd.read_csv('birthdays.csv')
birthday_dict = birthday_csv.to_dict(orient='records')

for info in birthday_dict:
    if info['month'] == month and info['day'] == day:
        birthday_person = info
        send_mail = True
        break


letter = random.choice(os.listdir("letter_templates"))

with open(f"letter_templates/{letter}", "r") as file:
    letter_txt = file.read().replace("[NAME]", birthday_person['name'])


if send_mail:
    my_id = "jangg0627"
    my_emali = "jangg0627@naver.com"
    password = "YOUR PASSWORD"

    recipient_email = birthday_person['email']
    mail_title = "생일축하해요!"
    to_send_text = letter_txt

    smtp = smtplib.SMTP("smtp.naver.com")
    smtp.starttls()
    smtp.login(user=my_id, password=password)

    msg = MIMEText(to_send_text)
    msg['From'] = my_emali
    msg['Subject'] = mail_title
    msg['To'] = recipient_email
    smtp.sendmail(my_emali, recipient_email, msg.as_string())

    smtp.quit()
