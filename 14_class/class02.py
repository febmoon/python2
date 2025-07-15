import time

class Player: # class 명은 대문자로 시작해야 한다!
    def __init__(self, nickname, hp=100, gold=0, level=1): # 디폴트 값을 설정할 수 있다
        # 필수값과 기본값을 설정할 수 있다. nickname= 필수값, 나머지 - 기본값 정의
        # 주의))def __init__(self, hp=100, gold=0, level=1, nickname) # 이렇게는 못 쓴다!!
        self.nickname = nickname
        self.hp = hp
        self.gold = gold
        self.level = level
        print(f"닉네임:{self.nickname}\nHP:{self.hp}\nGOLD:{self.gold}\nLEVEL:{self.level}")

    def __del__(self): # 프로그램을 종료
        print("저장중...")
        print("저장되었습니다!!")

    def change_nickname(self, new_nickname):
        self.nickname = new_nickname
        # 현재 객체의  nickname 속성을 새로운 닉네임으로 변경
        print(f"{self.nickname}으로 닉변되었습니다")
player1 = Player("모험가")
player1.change_nickname("모험가2")
print(f"player의 현재 닉네임은{player1.nickname}")