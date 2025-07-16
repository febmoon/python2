class Mom:
    def swim(self):
        print("수영을 잘한다.")

class Dad:
    def run(self):
        print("달리기를 잘한다")

class Athlete(Mom, Dad):
    def __init__(self, name):
        self.name= name
        print(f"운동 선수 {self.name}이 생성되었습니다")
    def compete(self):
        print(f"{self.name}이 시합에 참가합니다.")

athlete1 = Athlete("철인")
athlete1.swim()
athlete1.run()
athlete1.compete()
#-------------------------------------------------------------------------------------------------------------
class Flyer():
    def fly(self):
        print("하늘을 날 수 있다.")
class Runner():
    def run(self):
        print("달릴 수 있다.")

class Pegasus(Flyer, Runner):
    def __init__(self,name):
        self.name = name
        print(f"페가수스 {self.name}이 생성되었습니다.")
    def introduce(self):
        print(f"내 이름은 {self.name}입니다.")
    def fly(self): # mehod overriding
        print(f"{self.name}이(가) 하늘을 날 수 있습니다.")
pegasus1 = Pegasus("수진")
pegasus1.fly()
pegasus1.run()
pegasus1.introduce()
#----------------------------------------------------------------------------------------------------------------
# 부모클래스 -> Camera, Message, Internet, Game
class Camera:
    def shoot(self):
        print("카메라로 사진을 촬영합니다.")
class Message:
    def send_message(self):
        print("메시지를 전송합니다.")
class Internet:
    def search_internet(self):
        print("인터넷 검색을 합니다.")
class Game:
    def play_game(self):
        print("게임을 플레이합니다.")

class Smartphone(Camera, Message, Internet, Game):
    def __init__(self, brand, model):
        self.brand= brand
        self.model= model
    def display_info(self):
        print(f"브랜드 : {self.brand}, 모델명 : {self.model}")
    def send_message(self): # method overriding
        print("카톡을 전송합니다")
    def shoot_search(self):
        super().shoot()
        super().search_internet()

smartphone1= Smartphone("apple", "iphone13")
smartphone1.shoot()
smartphone1.send_message()
smartphone1.search_internet()
smartphone1.play_game()
smartphone1.display_info()
smartphone1.shoot_search()
