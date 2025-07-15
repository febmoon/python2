# Account 클래스  -> 계좌정보
# owner 그리고 balance=> 잔액은 생성될 때 0으로 초기화
# deposit 메서드를 추가하여 잔액을 증가시키고 증가된 잔액을 출력 - 양수로 입력받기
# withdraw 메서드를 추가하여 잔액을 감소시키고 감소된 잔액을 출력 - 잔액보다 작은 얌수로 입력받기
# 잔액이 부족하다면 출금을 할 수 없도록 출력
class Account:
    def __init__(self, owner, balance = 0):
        self.owner = owner
        self.balance  = balance
        print(f"{self.owner}의 계좌가 개설되었습니다. 잔액 :{self.balance}")

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"{amount}원 입금되었습니다. 현재 잔액 {self.balance}원")
        else :
            print("입금액은 0보다 커야 합니다. 현재 잔액 :{self.balance}")

    def withdraw(self, amount):
        if amount <=0:
            print("출금액은 0보다 커야 합니다.")
        elif amount <= self.balance:
            self.balance -= amount
            print(f"{amount}원 출금되었습니다. 현재 잔액 : {self.balance} 원")
        else:
            print(f"잔액이 부족합니다. 현재 잔액 :{self.balance}")

account1 = Account("sujin")

account1.deposit(40000)
account1.withdraw(5000)
