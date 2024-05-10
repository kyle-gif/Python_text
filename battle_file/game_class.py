import enum
import time
import os
import platform
import sys
from skill import SKILL
import enum


class PlayerStat(enum.Enum):
    hp = 1000
    mp = 100
    power = 10
    magic_power = 12


class Player:
    def __init__(self, name, playerstat=PlayerStat):
        self.name = name
        self.hp = playerstat.hp.value
        self.current_hp = self.hp
        self.mp = playerstat.mp.value
        self.current_mp = self.mp
        self.power = playerstat.power.value
        self.magic_power = playerstat.magic_power.value
        print(f"\n{self.name}이(가) 생성 되었습니다.")
        print(f"\nHP: {self.hp}\nMP: {self.mp}\n힘: {self.power}\n마력: {self.magic_power}")

    def primary_attack(self, enemy):
        damage = 50 * self.power
        enemy.current_hp -= damage
        print(f"{self.name}의 공격! {enemy.name}에게 {damage}의 물리 데미지를 입혔습니다.")
        time.sleep(0.5)
        if enemy.current_hp <= 0:
            print(f"{enemy.name}이(가) 쓰러졌습니다.")
            time.sleep(0.5)

    def magic_attack(self, enemy):
        damage = 70 * self.magic_power
        enemy.current_hp -= damage
        self.current_mp -= 5
        print(f"{self.name}의 공격! {enemy.name}에게 {damage}의 마법 데미지를 입혔습니다.")
        time.sleep(0.5)
        if enemy.current_hp <= 0:
            print(f"{enemy.name}이(가) 쓰러졌습니다.")
            time.sleep(0.5)

    def status(self):
        print(f"\n===나의 상태===\nHP: {self.current_hp} / {self.hp}\nMP: {self.current_mp} / {self.mp}")
        time.sleep(0.5)


class Monster:
    def __init__(self, name, hp, power):
        self.name = name
        self.hp = hp
        self.current_hp = hp
        self.power = power

    def primary_attack(self, enemy):
        damage = 15 * self.power
        enemy.current_hp -= damage
        print(f"{self.name}의 공격! {enemy.name}에게 {damage}의 물리 데미지를 입혔습니다.")
        time.sleep(0.5)
        if enemy.current_hp <= 0:
            print(f"{enemy.name}이(가) 쓰러졌습니다.")
            time.sleep(0.5)

    def status(self):
        print(f"\n==={self.name}의 상태===\nHP: {self.current_hp} / {self.hp}")
        time.sleep(0.5)
