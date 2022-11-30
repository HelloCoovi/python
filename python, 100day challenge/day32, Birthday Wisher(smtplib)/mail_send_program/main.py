import smtplib
from email.mime.text import MIMEText
import datetime as dt
import random

now = dt.datetime.now()
year = now.year
month = now.month
day_of_week = now.weekday()
print(now)
print(year)
print(month)
print(day_of_week)

data_of_birth = dt.datetime(year=1999, month=6, day=27, hour=3)
print(data_of_birth)



# 매주 월요일에 명언하나를 메일로 쏜다.
with open("quotes.txt", "r") as file:
    quotes_lsit = file.readlines()
    # for i in range(len(quotes_lsit)):
    #     quotes_lsit[i] = quotes_lsit[i].strip().replace(" - ", "\n   - ")
    quotes = random.choice(quotes_lsit).strip().replace(" - ", "\n   - ")

if now.weekday() == 4:
    my_id = "jangg0627"
    my_emali = "jangg0627@naver.com"
    password = "5P6MLUCGZSVW"

    recipient_email = 'coovistudy2@gmail.com'
    mail_title = "월요일입니다!"
    to_send_text = quotes


    smtp = smtplib.SMTP("smtp.naver.com")
    smtp.starttls()
    smtp.login(user=my_id, password=password)
    # smtp.sendmail(from_addr=my_emali, to_addrs="coovistudy2@gmail.com", msg="Hello!")

    msg = MIMEText(to_send_text)
    msg['From'] = my_emali
    msg['Subject'] = mail_title
    msg['To'] = recipient_email
    smtp.sendmail(my_emali, recipient_email, msg.as_string())

    smtp.quit()
