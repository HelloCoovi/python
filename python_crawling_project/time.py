import time

# 현재시간을 epoch 타임으로 출력
t = time.time()
print(t)

# epoch 타임을 년월일 시간으로 표현해준다.
t = time.ctime(t)
print(t)

# 시간을 각각의 요소로 출력가능
t = time.localtime()
# struct_time 객체로 변환되며 여기서 각각의 속성을 따로 호출 할수 있다.
print(t)
print(t.tm_hour)
print(t.tm_year)

# 시간 표시 형식을 지정해서 출력가능하다.
# 괄호안에 포맷팅 문법과 localtime를 집어넣어줘야한다.
# %Y: 년(소문자(y)사용시 뒤에 두자리로 나온다.)
# %m: 월, %d: 일
# %H: 시, %M: 분, %S: 초
t = time.strftime("%Y year %m month", t)
print(t)

# 조금 더 간편하게 출력하고 싶다면
import datetime
print(datetime.datetime(2022, 10, 1))
print(datetime.datetime(2022, 10, 1, 12, 10, 8))

