'''
try: 예외가 발생할 것 같은 코드블록
except : 예외 발생시 수행되는 코드블록
finally : 상관없이 실행 무조건
else : 정상적 실행
'''

# print(10/0)
# ZeroDivisionError: division by zero

# try:
#     print(10/0)
# except:
#     print("예외발생!!")
#
# try:
#     num = int(input("숫자를 입력해 주세요 :"))
#     print(10/num)
# except ValueError: #값데이터오류
#     print("문자말고 숫자넣으시오")
#     # hello 입력시
#     # ValueError: invalid literal for int() with base 10: 'hello'
# except ZeroDivisionError:
#     print("0으로 나눌 수 없습니다")
#----------------------------------------------------------------
# IndexError, ValueError\
# try:
#     my_list = [1,2,3]
#     index = int(input("리스트에서 가져올 인덱스 :"))
#     print(my_list[index])
# except ValueError:
#     print("숫자만 입력해라")
# except IndexError:
#     print("그런 인덱스는 없습니다")

# 파일입출력예외처리 : FileNotFoundError

# file = None # 이걸 넣어줘야  네임에러가 안뜬다. NameError: name 'file' is not defined.
# try:
#     file = open("hi.txt", "r", encoding = "utf-8")
#     content = file.read() # 파일의 내용을 읽어온다.
#     print(content)
# except FileNotFoundError:
#     print("그런 파일은 없습니다")
# finally:
#     if file is not None and not file.closed:
#         file.close()
#         print("정상적으로 파일이 닫혔습니다.")
#     elif file is None:
#         print("애초에 파일이 열리지 않았습니다")


# 리스트 요소 5개 선언하고 index 로 찾는 로직
# indexError, ValueError 예외처리
# 정상적이면 해당 리스트 값 출력 else
# 마지막은 항상 끝!! 출려 finally

# list1 =[2,4,6,7,8]
# try:
#     index = int(input("인덱스 입력하시오:"))
#     result = list1[index]
# except IndexError as message:
#     print("해당 인덱스는 없습니다")
#     print(message) #list index out of range
# except ValueError as message:
#     print("숫자 입력해야 합니다")
#     print(message) #list index out of range
# else:
#     print(f"해당 인덱스값 :{result}") # invalid literal for int() with base 10
# finally:
#     print("끝!!")
#
# # raise 키워드 : 강제로/일부러!! 예외 발생시키기
# # 특정 조건에서 개발자가 직접 예외를 발생시키는 데 사용

# try:
#     age = int(input("나이 입력하시오:"))
#     if age >0 or age >150:
#         raise Exception("0이상 150이하 숫자만 입력하시오") # raise 뒤 Exception 안에 넣는 내용은 사용자에게 줄 에러메시지
# except Exception as e: # Exception : 대부분 예외클래스의 슈퍼클래스이 -> 하위 클래스예외도 다 잡아낸다. Value Error를 따로 안 잡아줘도 된다!
#     print(e)
# else:
#     print(f"입력된 나이 :{age}")
# finally:
#     print("끝")
#________________________________________________________________
# 사용자정의 예외클래스
''' 커스텀예외클래스
class 예외클래스명(Exception):
    def__init__(self):
        super().__init__("에러메시지")
'''

# class AgeException(Exception):
#     def __init__(self):
#         super().__init__("0이상 150 이하 숫자만 입력하시오.")
# try:
#     age = int(input("나이 입력하시오:"))
#     if age <0 or age >150:
#         raise AgeException()
# except AgeException as e:
#     print(e)
# else:
#     print(f"입력된 나이 : {age}")
# finally:
#     print("끝")

# 출금을 할 떄 잔액이 부족하면 발생되는 예외
# FundsError -> 잔액이 부족합니다. 현재잔액 *** 원, 출금 시도 금액  ***원
# account 클래스 만들고 메소드 withdraw 출금
# 출금할 때 잔액이 부족하면 FundsError 발생
# class FundsError(Exception):
#     def __init__(self, balance, amount): # 생성자에서 현재 잔액과 출금 시도 금액을 받습니다.
#         super().__init__(f"잔액이 부족합니다. 현재 잔액 {balance}원, 출금 시도 금액 {amount}원")
#
# class BankAccount:
#     def __init__(self, balance =0):
#         self.balance =balance
#     def withdraw(self, amount):
#         try:
#             if amount > self.balance:
#                 raise FundsError(self.balance, amount)
#         except FundsError as e:
#             print(e)
#         else: #정상상황이라면
#             self.balance -= amount
#             print(f"정상적으로 출금되었습니다. 남은 잔액 : {self.balance}")
#
# account1 = BankAccount(100000)
# account1.withdraw(50000)
# account1.withdraw(70000)
#------------------------------------------------
# 딕셔너리 요소 찾기
# 딕셔너리 키를 입력받음 (숫자로)
# result 변수에 해당 키의 값을 넣음
# 예외처리
# #-> 해당 키가 존재하지 않을 때 "KeyError"처리 :"해당 키는 존재하지 않습니다." 출력
# 숫자가 아닌 문자를 입력했을 때 " ValueError" 처리 : 숫자를 입력해 주세요." 출력
# 정상적으로 실행된다면 해당 키의 값을 넣어둔 result 출력
# 마지막은 항상 " 완료!!"를 출력



try:
    key = int(input("딕셔너리 키 숫자로 입력하시오.")) #ValueError가 발생할 수 있는 코드 - int 형변환할때 발생하는 에러임을 기억하자!
    dictionary = {1 : "APPLE", 2: "BANANA"} #얘는 에러가 발생하는 코드가 아니니까 밖에 있어도 상관없다
    result = dictionary[key] # KeyError가 발생할 수 있는 코드
except KeyError:
    print("해당 키는 존재하지 않습니다.")
except ValueError:
    print("숫자를 입력해 주세요.")
else:
    print(result)
finally:
    print("완료")
