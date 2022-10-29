"""
크롤링 봇은 대부분 차단을 당한다. 로그인 프로그램을 속이자
1. send.Key를 사용할떄 복사+붙여넣기는 넣는다.
  이유는 모르지만 된다고 하더라
2. 실제 브라우저 처럼 꾸민다.
  자신의 pc에 있는 프로필 경로를 넣어준다.
  크롬창 주소창에 chrome://version 입력하고 '프로필 경로'에 있는 내용을 복사해서
  option.add_argument(f'user-data-dir = {요기}')에 입력해준다.
    2-1. 옵션이 잘 적용되었다면 크롬의 우측 상단에 프로필이 생긴다.

"""

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

import time
import pyperclip

## TODO, 1. selenium 기본설정하기

options = webdriver.ChromeOptions()
options.add_argument(r'user-data-dir = /Users/ro/Library/Application Support/Google/Chrome/Default')
options.add_experimental_option("detach", True)

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

## TODO, 2. 로그인페이지 접속 및 로그인
# 크롤링, 자동화가 비교적 쉬운 모바일 버전으로 진입하는 것을 추천

# driver.get("https://m.naver.com/")
driver.get("https://nid.naver.com/nidlogin.login?svctype=262144&url=http://m.naver.com/aside/")

user_id = "ID"
user_pw = "PW"

time.sleep(2)

el = driver.find_element(By.ID, "id")
pyperclip.copy(user_id)
el.click()
## 코드 복사 붙여넣기에 관하여
# 이상하게 코드가 오락가락한다.
# 첫번째 코드: el.send_keys(Keys.COMMAND, 'v')
#   심플하게 command + v 인데 종종 작동을 안한다. 공식문서와 자료를 참고해 수정한 코드는 다음으로
# 두번째 코드: ActionChains(driver).key_down(Keys.COMMAND).send_keys('v').key_up(Keys.COMMAND).perform()
#   좀 더 복잡하고 섬세한작업에 쓰인다고 공식문서에 기록되어있다.
#   from selenium.webdriver import ActionChains 와 같은 임포트 과정이 필요하며 첫번쨰 보다는 이 방법을 추천한다.
ActionChains(driver).key_down(Keys.COMMAND).send_keys('v').key_up(Keys.COMMAND).perform()
time.sleep(1)

el = driver.find_element(By.ID, "pw")
pyperclip.copy(user_pw)
el.click()
ActionChains(driver).key_down(Keys.COMMAND).send_keys('v').key_up(Keys.COMMAND).perform()

el.send_keys(Keys.ENTER)
time.sleep(1.5)

## TODO, 3. 메인페이지 접속후 적당히 순서를 보고 봇으로 의심하지 않게 하기위한 절차가 필요하다
# 메인페이지 -> 블로그 페이지 와 같은 순으로 일반적인 순서로 이동해서 사람 처럼 보이게 한다.
# 그냥 한번에 글 작성 링크로 이동할 수 있지만 차단이나 기타 조치를피하기 위한 방법이다.

driver.get("https://m.naver.com/")
time.sleep(1.5)
driver.get("https://m.blog.naver.com/FeedList.naver")
time.sleep(1.5)

driver.find_element(By.CLASS_NAME, "overflow_menu_btn__HngNp").click()
time.sleep(0.5)
driver.find_elements(By.CLASS_NAME, "profile_menu_item_link__G6b1_")[4].click()
time.sleep(1.5)

## TODO, 4. 제목과 본문을 찾아서 글자 집어넣기

blog_title = "테스트 제목입니다아ㅏ"
blog_text = """
블로그 봇 테스트 내용입니당.
에베베에에에렝네
본문 내용입니다~~~~~~
"""

# 원인은 모르겠으나 안먹힘
# 그냥 마음 편하게 어렵고 복잡하지만 잘되는거 쓰겠다.
# el = driver.find_elements(By.CLASS_NAME, "se_textarea")[0]
# el.send_keys(blog_title)
# el = driver.find_elements(By.CLASS_NAME, "se_textarea")[1]
# el.send_keys(blog_text)

el = driver.find_elements(By.CLASS_NAME, "se_textarea")[0]
pyperclip.copy(blog_title)
el.click()
ActionChains(driver).key_down(Keys.COMMAND).send_keys('v').key_up(Keys.COMMAND).perform()
time.sleep(0.5)

el = driver.find_elements(By.CLASS_NAME, "se_textarea")[1]
pyperclip.copy(blog_text)
el.click()
ActionChains(driver).key_down(Keys.COMMAND).send_keys('v').key_up(Keys.COMMAND).perform()
time.sleep(0.5)