#문자열의 인덱싱
# a = "Life is too short, You need Python"
# print(a[3])
# print(a[-1])
#
# b = a[0] + a[1] + a[2] + a[3]
# print(b)

#실습
#단어를 입력받고 변수에 선언한 다음 첫번째 글자와 마지막 글자를 출력하시오
# word = input("단어를 입력하세요 : ")
# print("첫번째 글자 -", word[0])
# print("마지막 글자 -", word[-1])

#슬라이싱
# print(a[0:4]) #Life
# print(a[5:7]) #끝 번호는 자기 자신을 포함하지 않는다.
# print(a[19:])
# print(a[:17])
# print(a[19:-7])
# print(a[::2])
# print(a[::-1]) #문자열 뒤집기

#실습
# date = "20250702Sunny"
# #년도 출력
# print("년도 :", date[:4])
# #월일 출력
# print("월일 :", date[4:8])
# #날씨 출력
# print("날씨 :", date[8:])

#각종 문자열 함수
a = "Life is too short, You need Python"
print(len(a)) #문자열의 길이
print(a.count("t")) #특정 문자가 몇개 있는지
print(a.index("t")) #특정 문자의 인덱스 찾기
print(a.index("t", 10, 18))
#특정문자, 시작인덱스, 끝인덱스로 구간을 설정
print(a.find("z"))

"""
index, find의 차이점
index는 해당 문자가 없으면 오류를 발생
find는 -1 반환
"""

print(",".join(a)) #문자 합치기 근데 이제 사이에 특정 문자 곁들여서
print(a.upper()) #모두 대문자로
print(a.lower()) #모두 소문자로
print(a[0].isupper()) #대문자 여부
print(a[2].islower()) #소문자 여부

b = "       hi         "
print(b.lstrip()) #왼쪽 공백제거
print(b.rstrip()) #오른쪽 공백제거
print(b.strip()) #양쪽 공백제거
print(a.replace("short", "long"))
print(a.replace(" ", ""))
print(a.split()) #아무것도 넣지 않으면 공백, 탭, 엔터 기준으로 나눔
c = "a:b:c:d"
print(c.split(":"))

#실습
#먼저 이메일을 입력받아서 변수에 저장, 해당 이메일에서 아이디만 추출해서 출력
email = input("이메일을 입력하세요: ")
print("이메일 아이디 :", email[:email.index("@")])
print("이메일 아이디 :", email.split("@")[0])





