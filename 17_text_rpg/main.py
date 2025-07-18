import os
from package.models import Player
from package.utils import save_game, load_game


def main():
    print("턴제 RPG 게임")

    if os.path.exists("save.json"):
        choice = input("1. 기존 캐릭터 불러오기\n2. 새로 시작하기\n선택:")
        if choice =="1": # 플레이어 데이터 들고오기
            player = load_game() #load_game에 대한 반환값이 player 객체
            if not player:
                print("저장된 캐릭터가 없습니다.")
                nickname = input("닉네임을 입력해주세요:")
                player = Player(nickname)  # 닉네임 말고는 기본값 설정되어 있음

        elif choice =="2":
            nickname = input("닉네임을 입력해주세요:")
            player = Player(nickname) #닉네임 말고는 기본값 설정되어 있음
    else:
        nickname = input("닉네임을 입력해주세요:")
        player = Player(nickname)


    while True:
        print("닉네임:",player.nickname)
        print("\n[메뉴]")
        print("1. 배틀")
        print("2. 상점")
        print("3. 내 아이템 확인")
        print("4. 내 정보 확인")
        print("5. 게임 종료")
        choice = input("메뉴선택 : ")

        if choice == "1":
            print("\n[배틀]")
        elif choice == "2":
            print("\n[상점]")
        elif choice == "3":
            print("\n[내 아이템 확인]")
        elif choice == "4":
            print("\n[내 정보 확인]")
            print(f"닉네임:{player.nickname}\n레벨:{player.level}({player.exp}/{player.max_exp})\n공격력: {player.attack}\n치명타 확률:{player.cri_luk}%\nHP:{player.hp}\nMP:{player.mp},골드:{player.gold}")
        elif choice == "5":
            print("\n[게임 종료]")
            save_game(player)
            # 게임을 종료하기 전에 게임을 저장하는 함수 필요
            break
        else:
            print("잘못된 입력입니다.")


if __name__ == "__main__":
    main()
# 이 파이선 파일이 직접 실행되고 여기가 본체로 돌아가게 하기 위해


