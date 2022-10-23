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


options = webdriver.ChromeOptions()
options.add_argument(r'user-data-dir = /Users/ro/Library/Application Support/Google/Chrome/Default')
options.add_experimental_option("detach", True)

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
# driver.get("https://m.naver.com/")
driver.get("https://nid.naver.com/nidlogin.login?svctype=262144&url=http://m.naver.com/aside/")

user_id = "your ID"
user_pw = "your PW"

time.sleep(2)

el = driver.find_element(By.ID, "id")
pyperclip.copy(user_id)
el.click()
## TODO. 코드 복사 붙여넣기에 관하여
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
time.sleep(1)

el.send_keys(Keys.ENTER)




