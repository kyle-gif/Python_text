import enum

class SKILL_CODE(enum.Enum):
    PrimaryAttack = 0
    Nasengan = 1
    Hasegi = 2
    SwordofLight_Supernova = 3


class SKILL:
    def __init__(self, skill_code: SKILL_CODE):
        self.code = skill_code

    def __str__(self):
        if self.code == SKILL_CODE.PrimaryAttack:
            return 'primary'
        elif self.code == SKILL_CODE.Nasengan:
            return 'Nasengan'
        elif self.code == SKILL_CODE.Hasegi:
            return 'Hasegi'
        elif self.code == SKILL_CODE.SwordofLight_Supernova:
            return 'SwordofLight_Supernova'