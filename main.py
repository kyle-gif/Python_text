import time
from skill import SKILL, SKILL_CODE
import game_class
import random
import sys


def player_turn(behv):
    if behv == 1:
        while True:
            try:
                print("\n===공격 방식 선택===\n1. 물리 공격\n2. 마법 공격")
                player_skill_input = int(input("\n공격할 방식의 번호를 입력해주세요: "))
                if player_skill_input not in [1, 2]:
                    print("공격방식을 다시 입력해주세요")
                    continue

                if player_skill_input == 2:
                    if p1.current_mp < 5:
                        print("스킬을 사용하는데 필요한 MP가 모자랍니다.")
                        continue
            except ValueError:
                print("공격방식을 숫자로 입력해주세요")
                continue
            break

        print("\n===공격 대상 선택===")
        for i, m in enumerate(monster_list):
            print(f"{i + 1}. {m.name} (HP: {m.current_hp} / {m.hp})")

        while True:
            try:
                player_target_input = int(input("\n공격할 대상의 번호를 입력해주세요: "))
                if player_target_input <= 0 or player_target_input > len(monster_list):
                    print("잘못된 대상을 선택하셨습니다. 다시 선택해주세요.")
                    continue
            except ValueError:
                print("대상 번호를 숫자로 입력해주세요.")
                continue
            break

        if player_skill_input == 1:
            p1.primary_attack(monster_list[player_target_input - 1])
        elif player_skill_input == 2:
            p1.magic_attack(monster_list[player_target_input - 1])

    elif behv == 2:
        runrate = random.randint(0,100)
        if runrate > 60:
            print("\n도망치는데 성공했다! 하남자ㅋㅋ")
            sys.exit()
        else:
            print("\n되겠냐고 ㅋㅋ")


def monster_turn():
    for monster in monster_list:
        monster.primary_attack(p1)


def monster_death():
    for m in monster_list[:]:
        if m.current_hp <= 0:
            monster_list.remove(m)


p1 = game_class.Player(input("당신의 이름은 무엇입니까?: "))
m1 = game_class.Monster("잡몹 1", random.randint(10, 50), 0.5+round(random.random(),1))
m2 = game_class.Monster("잡몹 2", random.randint(10, 50), 0.5+round(random.random(),1))
m3 = game_class.Monster("잡몹 3", random.randint(10, 50), 0.5+round(random.random(),1))

monster_list = [m1, m2, m3]

turn = 1

while True:
    input("\nENTER 키를 눌러 다음으로 진행하세요")
    print(f"\n====={turn}번째 턴====")
    time.sleep(0.3)
    p1.status()
    time.sleep(0.3)
    for m in monster_list:
        m.status()
        time.sleep(0.3)

    print("\n===플레이어 턴===")
    behv = int(input("\n할 행동을 정해주세요.\n1. 공격\n2. 도망치기\n"))
    player_turn(behv)
    monster_death()

    if not monster_list:
        print("\n====clear!====\n당신이 승리했습니다.")
        break

    print("\n===몬스터 턴===")
    time.sleep(0.3)
    monster_turn()

    if p1.current_hp <= 0:
        print("\n당신이 사망하였습니다.\n ====게임 오버====")
        break

    turn += 1
    print("\n====턴 종료====")
    time.sleep(0.3)