"""
크롤링하기
1. requests, bs4 임포트
2. 원하는 페이지 불러오기(requests)
3. find_all 혹은 select를 활용해서 가져온다.
"""
import requests
from bs4 import BeautifulSoup

# 이 링크에서
page_url = "https://finance.naver.com/item/sise.naver?code=005930"
# 페이지를 가져오고
page = requests.get(page_url)
# 페이지의 html을 뽑아(?)낸뒤(원래라면 decode는 필요없지만 한글이 깨져보인다면 넣어야한다.)
# soup = BeautifulSoup(page.content, 'html.parser')
soup = BeautifulSoup(page.content.decode('euc-kr', 'replace'), 'html.parser')
# 원하는 곳에 있는 정보를 프린트
print(soup.select("#_nowVal")[0].text)


# print(soup.find_all("strong", id="_nowVal")[0].text)
# class는 유니크 하지 않으므로 직접확인하고 인덱스를 지정해주자
# print(soup.find_all("span", class_="tah")[0].text)
# print(soup.find_all("em", class_="no_down")[0])

"""select 활용하기
태그 클래스 혹은 id 띄여쓰기는 해당 태그 내부를 의미한다.
간단하게 하려면 원하는 요소를 우클릭하고 Copy -> Copy selector 를 누르면
바로 selector 문법으로 복사된다.

selector 문법에서
id는 앞이 # 으로 시작되고
class는 앞이 . 으로 시작된다 
"""

# 태그:em, id:_market_sum 을 찾아라
# print(soup.select("em#_market_sum")[0].text)
#  id:tab_con1 안에 태그:h3 를 찾아라
# print(soup.select("#tab_con1 h3")[0].text)
#
# 이미지 찾기
# 이미지 클릭 -> copy select -> 셀렉트 문법으로 호출 -> src호출
# img_url = soup.select("#img_chart_area")[0]["src"]
# print(img_url)