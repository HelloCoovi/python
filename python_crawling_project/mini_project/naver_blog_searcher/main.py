# TODO: Goal🎯 : 네이버 블로그 검색툴 만들기(검색어를 받으면 블로그 게시물의 제목과 주소를 가져온다.)

# TODO:
# TODO: 검색어를 받는다.
# TODO: 검색어를 네이버 검색에 적용 및 불러오기
# TODO: 무한스크롤을 이해하고 각 블로그 게시물의 제목과 링크를 출력한다.

import requests
from bs4 import BeautifulSoup


def naver_blog_finder():
    search_word = input("네이버에서 찾기를 원하는 블로그 검색어를 입력하세요.\n ->")
    page_nums = 1
    count = 0

    while True:
        try:
            view_page_url = f"https://s.search.naver.com/p/review/search.naver?rev=44&where=view&api_type=11&start={page_nums}&query={search_word}&nso=&nqx_theme=%7B%22theme%22%3A%7B%22main%22%3A%7B%22name%22%3A%22food_ingredient%22%7D%7D%7D&main_q=&mode=normal&q_material=&ac=1&aq=0&spq=0&st_coll=&topic_r_cat=&nx_search_query=&nx_and_query=&nx_sub_query=&prank=61&sm=tab_hty.top&ssc=tab.view.view&ngn_country=KR&lgl_rcode=11200103&fgn_region=&fgn_city=&lgl_lat=37.448775&lgl_long=126.7319911&abt=&_callback=viewMoreContents "
            view_page = requests.get(view_page_url)
            # soup = BeautifulSoup(view_page.content, "html.parser")
            soup = BeautifulSoup(view_page.text.replace("\\", ""), "html.parser")
            for i in range(30):
                print(soup.select("a.api_txt_lines")[i].text)
                print(soup.select("a.api_txt_lines")[i]["href"])
                print("")
                count += 1
            page_nums += 30
        except:
            break

    print(f"네이버의 {search_word}관련 블로그 글이 끝났습니다.")
    print(f"전체 글 수는 {count}입니다")

naver_blog_finder()
