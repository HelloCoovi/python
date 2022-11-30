import requests
from datetime import datetime
import time
import smtplib
from email.mime.text import MIMEText

MY_LAT = 37.448192
MY_LNG = 126.736830

def iss_overhead():
    iss_response = requests.get(url="http://api.open-notify.org/iss-now.json")
    iss_response.raise_for_status()
    iss_data = iss_response.json()

    longitude = float(iss_data["iss_position"]["longitude"])
    latitude = float(iss_data["iss_position"]["latitude"])

    iss_position = (longitude, latitude)

    if abs(MY_LAT - iss_position[1]) <= 5 and abs(MY_LNG - iss_position[0]) <= 5:
        return True
    else:
        return False

def is_night():
    parameter = {
        "lat": MY_LAT,
        "lng": MY_LNG,
        "formatted": 0
    }

    sun_response = requests.get("https://api.sunrise-sunset.org/json", params=parameter)
    sun_response.raise_for_status()
    sun_data = sun_response.json()

    sunrise = sun_data["results"]["sunrise"]
    sunset = sun_data["results"]["sunset"]
    sunrise_hour = int(sunrise.split("T")[1].split(":")[0])
    sunset_hour = int(sunset.split("T")[1].split(":")[0])
    now = datetime.now()
    now_hour = now.hour

    if now_hour <= sunrise_hour or now_hour >= sunset_hour:
        return True
    else:
        return False

def send_mail():
    my_id = "jangg0627"
    my_emali = "jangg0627@naver.com"
    password = "YOUR PASSWORD"

    recipient_email = "jangg0627@naver.com"
    mail_title = "하늘을 보세요!"
    to_send_text = "머리 위러 ssi 위성이 지나가요!"

    smtp = smtplib.SMTP("smtp.naver.com")
    smtp.starttls()
    smtp.login(user=my_id, password=password)

    msg = MIMEText(to_send_text)
    msg['From'] = my_emali
    msg['Subject'] = mail_title
    msg['To'] = recipient_email
    smtp.sendmail(my_emali, recipient_email, msg.as_string())

    smtp.quit()

while True:
    time.sleep(60)
    if iss_overhead() and is_night():
        send_mail()

# 60초마다 반복적으로 확인

# 위성 위치 파악
    # 위성이 내 머리위에서 부터 경도 위도가 -5 +5 안에 들어와 있다면?
    # 지금이 밤이라면?(now > sunset)
    # 머리윙 위성이 있다고 메일

