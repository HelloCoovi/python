"""
무한스크롤에서 정보 찾기
1. 개발자 도구에서 Network로 들어가서
2. 스크롤을 내리면서 새로운 정보가 들어오는것을 확인하고
3. 원하는 요소(텍스트)를 Network -> Search에 있는 검색창에 해당 내용을 검색
   예시) 네이버 블로그 글 제목 '구글 드라이브 계정 추가하는 방법'을 뽑아내고 싶다면
     '추가하는 방법' 같이 짧은 단어를 검색해서 원하는 내용을 특정한다.
4. 검색결과를 클릭하면 Network -> All -> Response 창이 새로 생길텐데
5. Network -> All -> Headers에 있는 Request URL에 있는 내용을 복사한다.
   -> Request URL은 안에 있는 요청을 받으면 해당 데이터를 리턴시킨다는 뜻이다.
6. requests.get() 안에 집어넣으면 해당 정보를 수신한다.
7. 스크롤을 계속 해서 내리면서 정보를 크롤링 하기 위해서는 Request URL의 규칙을 파악하는게 중요하다
   예시) 거의 모든것이 동일하지만 두번째 줄 start=31, start=121 이 가장 수상해 보인다.
        헷갈린다면 해당 찾아낸 주소를 주소창에 입력해서 맞는지 검증해보자(html이 출력됨)
     1번 링크:
       https://s.search.naver.com/p/review/search.naver?
       rev=44&where=view&api_type=11&start=31&
       query=%EA%B5%AC%EA%B8%80&nso=&nqx_theme=%7B%22theme%22%3A%7B%22main%22%3A%7B%22
       name%22%3A%22site%22%2C%22score%22%3A%220.735203%22%7D%7D%7D&main_q=&mode
       =normal&q_material=&ac=1&aq=0&spq=0&st_coll=&topic_r_cat=&
       nx_search_query=&nx_and_query=&nx_sub_query=&prank=31&sm=tab_jum&
       ssc=tab.view.view&ngn_country=KR&lgl_rcode=11200103&fgn_region=&fgn_city=
       &lgl_lat=37.448775&lgl_long=126.7319911&abt=&_callback=viewMoreContents
------
     2번 링크:
       https://s.search.naver.com/p/review/search.naver?
       rev=44&where=view&api_type=11&start=121&
       query=%EA%B5%AC%EA%B8%80&nso=&nqx_theme=%7B%22theme%22%3A%7B%22main%22%3A%7B%22
       name%22%3A%22site%22%2C%22score%22%3A%220.735203%22%7D%7D%7D&main_q=&mode
       =normal&q_material=&ac=1&aq=0&spq=0&st_coll=&topic_r_cat=&
       nx_search_query=&nx_and_query=&nx_sub_query=&prank=121&sm=tab_jum&
       ssc=tab.view.view&ngn_country=KR&lgl_rcode=11200103&fgn_region=&fgn_city=
       &lgl_lat=37.448775&lgl_long=126.7319911&abt=&_callback=viewMoreContents

"""

import requests
from bs4 import BeautifulSoup

url = "https://s.search.naver.com/p/review/search.naver?rev=44&where=view&api_type=11&start=1&query=%EA%B5%AC%EA%B8" \
      "%80&nso=&nqx_theme=%7B%22theme%22%3A%7B%22main%22%3A%7B%22name%22%3A%22site%22%2C%22score%22%3A%220.735203%22" \
      "%7D%7D%7D&main_q=&mode=normal&q_material=&ac=1&aq=0&spq=0&st_coll=&topic_r_cat=&nx_search_query=&nx_and_query" \
      "=&nx_sub_query=&prank=31&sm=tab_jum&ssc=tab.view.view&ngn_country=KR&lgl_rcode=11200103&fgn_region=&fgn_city" \
      "=&lgl_lat=37.448775&lgl_long=126.7319911&abt=&_callback=viewMoreContents "

page = requests.get(url)

# 백슬래쉬(\)는 파이썬에서 인식을 못하기때문에 replace() 함수로 백슬래쉬를 지운다.
soup = BeautifulSoup(page.text.replace("\\", ""), "html.parser")
# print(soup)
page_list = soup.select("a.api_txt_lines")
print(page_list[0].text)
print(page_list[0]["href"])