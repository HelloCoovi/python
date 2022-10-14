import requests
from bs4 import BeautifulSoup


def stock_price_crawler(code):
    page = requests.get(f"https://finance.naver.com/item/sise.naver?code={code}")
    soup = BeautifulSoup(page.content.decode('euc-kr', 'replace'), 'html.parser')
    stock_name = soup.select("#middle > div.h_company > div.wrap_company > h2 > a")[0].text
    price = soup.select("#_nowVal")[0].text
    return f"{stock_name}: {price}\n"


page_url = "005930"
print(stock_price_crawler(page_url))

# 삼성전자, 엘지생활건강, 카카오, sk하이닉스
codes = ["005930", "051900", "035720", "000660"]

w_file = open("stock_data.txt", "w")
for code in codes:
    w_file.write(stock_price_crawler(code))
w_file.close()