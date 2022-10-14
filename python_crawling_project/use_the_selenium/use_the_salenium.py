""""
1. selenium 설치하기(pip install selenium)
  - driver를 관리하는 패키지 설치하기(pip install webdriver-manager)
2. TODO. import에 있는 모듈 임포트
3.

문제해결
주요 문제들은 샐레니움이 4버전이 업데이트 되면서 생긴 문제들이다.(selenium버전: 4.5.0)
 - ChromeDriverManager와 Service 모듈로 chromedriver 관련 설정을 안해도 된다.
 - find_element 문법 변경(By import)
 - 모달창 처리하기(아주 그지같았음)(WebDriverWait, expected_conditions, element_to_be_clickable)
 - urllib 오류(맥에서 파일 다운로드시 생기는 오류(ssl.SSLCertVerificationError:))
   (응용프로그램 -> Python 3.8 -> lnstall Cretificates.commend 더블클릭)
"""

## TODO. import
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
# 사진 다운로드용
import urllib.request

# # 인코딩을 위해 임포트했으나 잘 안해도 잘 돌아가서 pass
# from urllib import parse

## TODO. 페이지를 불러오고 driver를 관리해주는 코드들
options = webdriver.ChromeOptions()
# 이것은 코드 실행이 끝난후 페이지를 닫지않고 유지하는 코드이며 필요없다면 주석처리
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
driver.get("https://www.instagram.com/")

## TODO. 각종 요소들 불러와보기(By.~~~ 문법이 중요)
# el = driver.find_element(By.CLASS_NAME, "KPnG0").text
# el = driver.find_element(By.CSS_SELECTOR, ".b_nGN").text

## TODO. 인풋데이터에 정보 집어넣기(로그인 자동화)
driver.implicitly_wait(10)
# el = driver.find_element(By.CSS_SELECTOR, "input[name='username']")
# el.send_keys("아이디")
# el.send_keys(Keys.ENTER)
# el = driver.find_element(By.CSS_SELECTOR, "input[name='password']")
# el.send_keys("비밀번호")
# el.send_keys(Keys.ENTER)

# el = driver.find_element(By.CSS_SELECTOR, "button.y3zKF").click()
driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[5]/button').click()

user_id = driver.find_element(By.XPATH, '//*[@id="email"]')
user_id.send_keys("01088035510")
user_password = driver.find_element(By.XPATH, '//*[@id="pass"]')
user_password.click()
user_password.send_keys("@jaja2578")
user_password.send_keys(Keys.ENTER)

## 모달창 처리하는 코드
# 로그인 후 대기시간이 생각보다 오래걸려서 40까지 연장
WebDriverWait(driver, 40).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'button._a9--._a9_1'))).click()

## TODO. 태그 내용을 받고 사진 다운로드
# my_tag = parse.quote("노션")
my_tag = "제주"
driver.get(f"https://www.instagram.com/explore/tags/{my_tag}/")
driver.implicitly_wait(10)
driver.find_element(By.CSS_SELECTOR, '._aagw').click()

for i in range(10):
    # 이미지 저장코드
    image_url = driver.find_element(By.CSS_SELECTOR, '._aagu._aato img.x5yr21d').get_attribute('src')
    urllib.request.urlretrieve(image_url, f'test{i+1}.jpg')

    # 다음버튼 누르기
    driver.implicitly_wait(10)
    # driver.find_elements(By.CSS_SELECTOR, 'button._abl-')[2].click()
    # # 만약 버튼이 안눌린다면?(JS 문법임)
    next_image = driver.find_element(By.CSS_SELECTOR, 'div._aaqg._aaqh button._abl-')
    driver.execute_script('arguments[0].click();', next_image)

    # 윤태 요즘 새로 배우는거에요!!!!
    # 하나는 네이버에서 자동으로 검색 해주는 프로그램
    # 하나는 인스타그램에서 사진 자동으로 받아주는 프로그램!!!

