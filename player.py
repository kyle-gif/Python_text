from skill import SKILL
import time

class Player():
    name = ""
    hp = 0
    current_hp = 0
    mp = 0
    current_mp = 0
    power = 0
    magic_power = 0

    def __init__(self, name, skill: SKILL):
        self.name = name
        self.hp = 100
        self.current_hp = 100
        self.mp = 100
        self.current_mp = 100
        self.power = 1.0  #power는 물리 공격에 대한 배수
        self.magic_power = 1.2  #마력은 마법공격에 대한 배수
        self.currentSkill = SKILL
        print(f"\n{self.name}이(가) 생성 되었습니다.")
        print(f"\nHP: {self.hp}\nMP: {self.mp}\n힘: {self.power}\n마력: {self.magic_power}")

    # 플레이어의 일반 공격
    def primary_attack(self, enemy):
        damage = 5 * self.power
        enemy.current_hp = enemy.current_hp - damage
        print(f"{self.name}의 공격! {enemy.name}에게 {damage}의 물리데미지를 입혔습니다.")
        time.sleep(0.5)
        if enemy.current_hp <= 0:
            print(f"{enemy.name}이(가) 쓰러졌습니다.")
            time.sleep(0.5)

    # 플레이어의 마법 공격
    def magic_attack(self, enemy):
        damage = 7 * self.magic_power
        enemy.current_hp = enemy.current_hp - damage
        self.current_mp = self.current_mp - 5
        print(f"{self.name}의 공격! {enemy.name}에게 {damage}의 마법데미지를 입혔습니다.")
        time.sleep(0.5)
        if enemy.current_hp <= 0:
            print(f"{enemy.name}이(가) 쓰러졌습니다.")
            time.sleep(0.5)

    def status(self):
        print(f"\n===나의 상태===\nHP: {self.current_hp} / {self.hp}\nMP: {self.current_mp} / {self.mp}")
        time.sleep(0.5)