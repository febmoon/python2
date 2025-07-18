import json
import os

from .models import Player

def load_game():
    if os.path.exists("./save.json"):
        with open("./save.json","r",encoding = "utf-8") as file:
            data = json.load(file)
            player = Player.from_dict(data)
            return player # 데이터가 객체형태가 아니다 -> 메서드를 실행시킬 수 없다. 메서드는 객체통해서 수행할 수 있으므로
def save_game(player):
    with open("./save.json","w", encoding="utf-8") as file: #package 바깥에 생성될 것이다
        json.dump(player.to_dict(), file, indent =4, ensure_ascii = False) # indent 가독성 좋게 들임, ensure_ascii 깨지지 말라고
