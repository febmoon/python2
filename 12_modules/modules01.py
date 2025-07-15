import math
#math - 수학관련 모듈

#ceil - 올림
#print(math.ceil(3.14))

#floor - 내림
#print(math.floor(3.14))

#copysign - 두 번째 인자의 부호만 취해 첫 번째 인자에 적용
#print(math.copysign(3.14, -1))

#fabs - 절댓값을 반환하는 메소드
#print(math.fabs(-3.14))

#factorial - 팩토리얼 구하는 메소드
# print(math.factorial(7))
# print(math.factorial(5))
# print(math.factorial(12))

#gcd - 두 수의 최대공약수
# print(math.gcd(6, 8))
# print(math.gcd(12, 18))
# print(math.gcd(9, 27))

#modf - 정수 부분과 소수 부분을 분리해서 리턴
# print(math.modf(3.14))

#trunc - 내림
# print(math.floor(-3.14)) #무조건 아래로 내림
# print(math.trunc(-3.14)) #0으로 향해서 내림

#log(a, b) - b를 밑으로 하는 log a에 대한 로그 값
# print(math.log(10, 10))

#원주율
# print(math.pi)

#사용자로부터 양수인 소수를 입력받기
#입력받은 숫자 올림하기
#입력받은 숫자 절댓값 출력하기
#입력받은 숫자 소수와 정수 분리해서 출력하기

# user_num_str = input("양수인 소수를 입력하세요:")
# user_num = float(user_num_str)
# print(math.ceil(user_num))
# print(math.fabs(user_num))
# print(math.modf(user_num))

# import random
#
# print(random.random())
#
# print(random.randint(1, 100))
# print(random.randrange(0, 100, 2))
#
# #shuffle
# abc = ["a", "b", "c", "d", "e"]
# random.shuffle(abc)
# print(abc)
#
# #choice
# abc = ["a", "b", "c", "d", "e"]
# print(random.choice(abc))

#점심 메뉴 후보 리스트를 만들고, 이 중에서 무작위로 하나의 메뉴를
#선택하여 출력하시오
# import time
# dinner_menu_list = ["제육덮밥", "돈까스", "냉모밀", "냉면", "칼국수"]
# choice_menu = random.choice(dinner_menu_list)
# print("오늘의 점심 메뉴는.........")
# time.sleep(4)
# print(f"오늘의 저녁 메뉴는 {choice_menu}입니다.")


#datetime
#날짜와 시간을 다루는 기능을 제공합니다. 현재 시각, 특정 날짜 계산
#,날짜 형식 지정 등에 사용됩니다.

from datetime import datetime, timedelta

#현재 날짜 및 시간
# now = datetime.now() #현재 시스템의 날짜와 시간을 now 변수에 저장
# print(now)
#
# one_week_later = now + timedelta(days=7)#현재 날짜에 7일 더한 거
# print(one_week_later)
#
# #현재 날짜와 시간을 2025.07.10 14:37:33 형식 지정
# print(f"현재 시간: {now.strftime("%Y.%m.%d %H:%M:%S")}")
#

#현재 시간에서 5일뒤 시간을
#2025년 7월 10일 14시 40분 22초 형식으로 출력
# now = datetime.now()
# day = now + timedelta(days=5)
# print(day.strftime("%Y년 %m월 %d일 %H시 %M분 %S초"))

# import os #운영체제와 상호작용할 수 있는 기능
# print(os.getcwd()) #현재 작업 디렉토리(current working directory)의 경로를 출력
# print(os.listdir()) #현재 작업 디렉토리 내의 모든 파일과 폴더 목록을 출력
#
# if not os.path.exists("example"):
#     os.mkdir("example")

#정규 표현식 re
import re

pattern = r"\d{3}-\d{4}-\d{4}" #전화번호 정규 표현식 패턴
phone_number = "010-1234-5678"

if re.match(pattern, phone_number):
    print("올바른 전화번호")
else:
    print("틀린 전화번호")

#이메일 정규표현식 가져와서 위 처럼 예시를 넣고
#맞으면 올바른 이메일 틀리면 틀린 이메일
pattern = r"[a-zA-Z0-9._+-]+@[a-zA-Z0-9]+\.[a-zA-Z]{2,4}"
email = "dongyoon7212@naver.com"
if re.match(pattern, email):
    print("올바른 이메일")
else:
    print("틀린 이메일")




