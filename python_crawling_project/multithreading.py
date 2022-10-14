"""
멀티스레딩(프로세싱 아님)으로 많은 코드를 동시에 빠르게 처리하는 방법을 서술함
len이 11인 url에서 반복문과 스레딩방식의 시간을 비교(time.time())
"""

import requests
import json
import time

url = [
    "https://tb.coinone.co.kr/api/v1/chart/olhc/?site=coinoneeth&type=1h&last_time=1609524000000",
    "https://tb.coinone.co.kr/api/v1/chart/olhc/?site=coinoneeth&type=1h&last_time=1608811200000",
    "https://tb.coinone.co.kr/api/v1/chart/olhc/?site=coinoneeth&type=1h&last_time=1608098400000",
    "https://tb.coinone.co.kr/api/v1/chart/olhc/?site=coinoneeth&type=1h&last_time=1606672800000",
    "https://tb.coinone.co.kr/api/v1/chart/olhc/?site=coinoneeth&type=1h&last_time=1605960000000",
    "https://tb.coinone.co.kr/api/v1/chart/olhc/?site=coinoneeth&type=1h&last_time=1605242700000",
    "https://tb.coinone.co.kr/api/v1/chart/olhc/?site=coinoneeth&type=1h&last_time=1604534400000",
    "https://tb.coinone.co.kr/api/v1/chart/olhc/?site=coinoneeth&type=1h&last_time=1603821600000",
    "https://tb.coinone.co.kr/api/v1/chart/olhc/?site=coinoneeth&type=1h&last_time=1603108800000",
    "https://tb.coinone.co.kr/api/v1/chart/olhc/?site=coinoneeth&type=1h&last_time=1602396000000",
]


def func(url):
    data = requests.get(url)
    dic = json.loads(data.content)
    return dic['data'][0]['Close']


# TODO, 1. 반복문을 활용한 크롤링
start = time.time()

price = []

for i in url:
    price.append(func(i))
print(price)

end = time.time()

print(f"반복문을 사용해 걸린시간: {end - start}")

# TODO, 2. 멀티스레딩을 활용한 크롤링
# 그냥 multiprocessing을 입력하면 멀티 프로세싱
# 아래와 같이 .dummy를 입력하면 멀티 쓰레딩
from multiprocessing.dummy import Pool as ThreadPool

start = time.time()

pool = ThreadPool(4)
price = pool.map(func, url)
pool.close()
pool.join()

print(price)

end = time.time()

print(f"멀티스레딩을 사용해 걸린시간: {end - start}")

"""
아래는 출력문을 가져온 것이며 반복문이 약 3배의 시간이 소요되는것을 확인할수있다.
['657500', '635500', '643300', '562900', '511700', '452900', '457800', '430300', '422600', '406300']
반복문을 사용해 걸린시간: 0.8329200744628906
['657500', '635500', '643300', '562900', '511700', '452900', '457800', '430300', '422600', '406300']
멀티스레딩을 사용해 걸린시간: 0.27434706687927246
"""