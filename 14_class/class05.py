# Account 클래스  -> 계좌정보
# owner 그리고 balance=> 잔액은 생성될 때 0으로 초기화
# deposit 메서드를 추가하여 잔액을 증가시키고 증가된 잔액을 출력 - 양수로 입력받기
# withdraw 메서드를 추가하여 잔액을 감소시키고 감소된 잔액을 출력 - 잔액보다 작은 얌수로 입력받기
# 잔액이 부족하다면 출금을 할 수 없도록 출력
class Account:
    def __init__(self, owner, balance = 0):
        self.owner = owner
        self.balance  = balance
    def deposit(self, a):
        if a > 0:
            self.balance += a
            print(f"입금 후 잔액은 {self.balance}입니다")
        else :
            print("0원 이상 입금하시오.")
    def withdraw(self, b):
        if b <= self.balance:
            self.balance -= b
            print(f"출금 후 잔액은 {self.balance}입니다")
        else:
            print("잔액을 초과하는 금액은 출금할 수 없습니다")
account1 = Account("sujin")

account1.deposit(40000)
account1.withdraw(50000)
