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
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

import pyperclip


options = webdriver.ChromeOptions()
options.add_argument(r'user-data-dir = /Users/ro/Library/Application Support/Google/Chrome/Default')
options.add_experimental_option("detach", True)

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
# driver.get("https://m.naver.com/")
driver.get("https://nid.naver.com/nidlogin.login?svctype=262144&url=http://m.naver.com/aside/")

driver.implicitly_wait(10)

pyperclip.copy("id")
el = driver.find_element(By.CSS_SELECTOR, "input#id")
el.send_keys(Keys.CONTROL, 'v')
el = driver.find_element(By.CSS_SELECTOR, "input#pw")
el.send_keys("jajaja")


