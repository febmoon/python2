'''
try: 예외가 발생할 것 같은 코드블록
except : 예외 발생시 수행되는 코드블록
finally : 상관없이 실행 무조건
else : 정상적 실행
'''

# print(10/0)
# ZeroDivisionError: division by zero

try:
    print(10/0)
except:
    print("예외발생!!")

try:
    num = int(input("숫자를 입력해 주세요 :"))
    print(10/num)
except ValueError: #값데이터오류
    print("문자말고 숫자넣으시오")
    # hello 입력시
    # ValueError: invalid literal for int() with base 10: 'hello'
except ZeroDivisionError:
    print("0으로 나눌 수 없습니다")
