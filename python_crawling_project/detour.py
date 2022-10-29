"""
일부 사이트는 bot을 차단하는데
유저의 정보를 받아서 사람같은 정보가 없다면 차단해버린다.
예. 아마존(amazon)
그것을 우회해서 사람처럼 보이기위한 위장법
TODO, 1. 정보확인
크롤링 하려는 페이지에 접속해서 검사 -> Network -> Name -> 가장 처음 요소 클릭 -> Headers -> Request Headers에
각종 정보들이 있는 것을 확인하고 User-Agent 를 찾는다.
  User-Agent는 현재 페이지의 접속한 유저의 정보를 저장한 것이며 이를 통해 진짜 인간인지 확인한다.
TODO, 2. 유저 데이터 입력
headers 딕셔너리를 만들고 User-Agent 정보 입력
requests.get에 있는 headers 파라미터에 방금 생성한 headers 입력
TODO, 3. 쿠키 입력
검사 -> Network -> Name -> 가장 처음 요소 클릭 -> Headers -> Request Headers -> Cookie 정보를 복사한뒤
딕셔너리 형태로 변환시켜준다(노가다 or 아래 코드들을 적절히 이용하여 수정)
str = str.replace(';', ',')
str = str.replace('=', ':')
str = str.replace(' ', '\n')
예시)
원본 -
Cookie: aws_lang=ko; aws-target-data=%7B%22support%22%3A%221%22%7D; AMCVS_7742037254C95E840A4C98A6%40AdobeOrg=1; aws-target-visitor-id=1666012413401-865114.32_0; AMCV_7742037254C95E840A4C98A6%40AdobeOrg=1585540135%7CMCIDTS%7C19283%7CMCMID%7C87915971882026749860939091058045536350%7CMCAAMLH-1666617213%7C11%7CMCAAMB-1666617213%7CRKhpRz8krg2tLO6pguXWp5olkAcUniQYPHaMWWgdJ3xzPWQmdj0y%7CMCOPTOUT-1666019613s%7CNONE%7CMCAID%7CNONE%7CvVersion%7C4.4.0; regStatus=pre-register; s_cc=true; aws-mkto-trk=id%3A112-TZM-766%26token%3A_mch-aws.amazon.com-1666012413410-24302; session-id=134-9461159-2694150; session-id-time=2082787201l; i18n-prefs=USD; sp-cdn="L5Z9:KR"; skin=noskin; ubid-main=132-3220547-7104858; session-token=yR+bzkhDGfOgGWmWmFptkwFDax9cbXVs86sziRIM7Nh/n9HS33IgpAmbO9RBgneuoVSI7TrPsCxlc01uRjxvprwjq5V5fDBXsZlBL+cPDXsDWRvTcOVmwj7uJItASTHtpcyAUxZHhsFry6321EDcvgiP5CrBm/W41nM9n1HooTU+8o8T1WdE1GlPmg4CoxTD0GOwSUv7KDldfFhiBs3iTfg9dpeJnQzWv54GnvmozwU=
수정후 -
cookie = {
    "aws_lang": "ko",
    "aws-target-data": "%7B%22support%22%3A%221%22%7D",
    "AMCVS_7742037254C95E840A4C98A6%40AdobeOrg": "1",
    "aws-target-visitor-id": "1666012413401-865114.32_0",
    "AMCV_7742037254C95E840A4C98A6%40AdobeOrg": "1585540135%7CMCIDTS%7C19283%7CMCMID%7C87915971882026749860939091058045536350%7CMCAAMLH-1666617213%7C11%7CMCAAMB-1666617213%7CRKhpRz8krg2tLO6pguXWp5olkAcUniQYPHaMWWgdJ3xzPWQmdj0y%7CMCOPTOUT-1666019613s%7CNONE%7CMCAID%7CNONE%7CvVersion%7C4.4.0",
    "regStatus": "pre-register",
    "s_cc": "true",
    "aws-mkto-trk": "id%3A112-TZM-766%26token%3A_mch-aws.amazon.com-1666012413410-24302",
    "session-id": "134-9461159-2694150",
    "session-id-time": "2082787201l",
    "i18n-prefs": "USD",
    "sp-cdn": "L5Z9:KR",
    "skin": "noskin",
    "ubid-main": "132-3220547-7104858",
    "session-token": "yR+bzkhDGfOgGWmWmFptkwFDax9cbXVs86sziRIM7Nh/n9HS33IgpAmbO9RBgneuoVSI7TrPsCxlc01uRjxvprwjq5V5fDBXsZlBL+cPDXsDWRvTcOVmwj7uJItASTHtpcyAUxZHhsFry6321EDcvgiP5CrBm/W41nM9n1HooTU+8o8T1WdE1GlPmg4CoxTD0GOwSUv7KDldfFhiBs3iTfg9dpeJnQzWv54GnvmozwU="
}
TODO, 4. 에러 대응하기
if문 혹은 try except로 대응
"""

import requests

headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36"
}

cookie = {
    "aws_lang": "ko",
    "aws-target-data": "%7B%22support%22%3A%221%22%7D",
    "AMCVS_7742037254C95E840A4C98A6%40AdobeOrg": "1",
    "aws-target-visitor-id": "1666012413401-865114.32_0",
    "AMCV_7742037254C95E840A4C98A6%40AdobeOrg": "1585540135%7CMCIDTS%7C19283%7CMCMID%7C87915971882026749860939091058045536350%7CMCAAMLH-1666617213%7C11%7CMCAAMB-1666617213%7CRKhpRz8krg2tLO6pguXWp5olkAcUniQYPHaMWWgdJ3xzPWQmdj0y%7CMCOPTOUT-1666019613s%7CNONE%7CMCAID%7CNONE%7CvVersion%7C4.4.0",
    "regStatus": "pre-register",
    "s_cc": "true",
    "aws-mkto-trk": "id%3A112-TZM-766%26token%3A_mch-aws.amazon.com-1666012413410-24302",
    "session-id": "134-9461159-2694150",
    "session-id-time": "2082787201l",
    "i18n-prefs": "USD",
    "sp-cdn": "L5Z9:KR",
    "skin": "noskin",
    "ubid-main": "132-3220547-7104858",
    "session-token": "yR+bzkhDGfOgGWmWmFptkwFDax9cbXVs86sziRIM7Nh/n9HS33IgpAmbO9RBgneuoVSI7TrPsCxlc01uRjxvprwjq5V5fDBXsZlBL+cPDXsDWRvTcOVmwj7uJItASTHtpcyAUxZHhsFry6321EDcvgiP5CrBm/W41nM9n1HooTU+8o8T1WdE1GlPmg4CoxTD0GOwSUv7KDldfFhiBs3iTfg9dpeJnQzWv54GnvmozwU="
}


page_url = "https://www.amazon.com/s?k=monitor&crid=SN9ZIZK2YZ71&sprefix=moni%2Caps%2C618&ref=nb_sb_ss_pltr-ranker-lnopsacceptance_2_4"
page = requests.get(page_url, headers=headers, cookies=cookie)

from bs4 import BeautifulSoup
soup = BeautifulSoup(page.content.decode('euc-kr', 'replace'), 'html.parser')




if page.status_code == 200:
    print(soup.select('.a-size-medium')[0])
else:
    print("에러다아아아ㅏ")