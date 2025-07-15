#반복문(while)
"""
while 조건:
    반복할 코드
    (조건을 변경하는 코드)
"""
from itertools import count

# num = 1
# while num <= 5:
#     print("숫자:", num)
#     num += 1

# num = 1
#
# while num <= 10:
#     print(num)
#
#     if num == 5: #num이 5가 되었을때 반복 종료
#         break #반복을 종료하는 코드
#
#     num += 1

# num = 0
# while num < 10:
#     num += 1
#
#     if num % 3 == 0: #3의 배수는 출력하지 않고 건너뜀
#         continue
#
#     print(num)

# dan = 1
# while dan <= 9:
#     n = 1
#     while n <= 9:
#         print(f"{dan} X {n} = {dan * n}")
#         n += 1
#     dan += 1

#실습문제
#1. 1부터 100까지 짝수만 출력하기
# num = 2
# while num <= 100:
#     print(num)
#     num += 2

# num = 1
# while num <= 100:
#     if num % 2 == 0:
#         print(num)
#     num += 1

#5의 배수 출력 50까지 (30에서 멈추기)
num = 5
while num <= 50:
    print(num)
    if num == 30:
        break
    num += 5







