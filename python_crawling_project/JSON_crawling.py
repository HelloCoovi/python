import requests
from bs4 import BeautifulSoup
import json
import time

url = "https://tb.coinone.co.kr/api/v1/chart/olhc/?site=coinone&type=1h"

page = requests.get(url)
# print(page.content)

dic = json.loads(page.content)


# json 내부에 DT라는 키값이 있는데 이것은 시간을 나타낸 것이며
# 이러한 형식은 epoch 시간이라하며 자세한것은 time 라이브러리 참고
print(dic["data"][0]["DT"])

for data in dic["data"]:
    t = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(data["DT"] / 1000))
    print(t)
    print(f"종가: {data['Close']}")

# 과거데이터를 수집하고싶다면 차트를 움직이면서 과거 데이터가 불러오는 요청(URL)의 규칙을 파악해서
# 데이터를 수집해보자