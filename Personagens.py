import random
from Weapons import Weapon,battleaxe,small_axe,javelin,longbow,longsword,dagger,melee
from BarraVida import HealthBar


class Player:
    def __init__(self,
                name:str,
                health: int) -> None:
    
        self.name = name
        self.health = health #vida atual
        self.max_health = health #vida atual
        self.agility = 0
        self.strength = 0
        self.health_bar = HealthBar(self, color="green")

    def weapon_attack(self, target):
        
        if (self.weapon == battleaxe):
            dice_roll = random.randint(1,12)
            target.health = target.health - dice_roll - self.strength

        elif (self.weapon == small_axe):
            dice_roll = random.randint(1,4)
            target.health = target.health - dice_roll - self.strength

        elif (self.weapon == javelin):
            dice_roll = random.randint(1,6)
            target.health = target.health - dice_roll - self.strength

        elif (self.weapon == longbow):
            dice_roll = random.randint(1,6)
            target.health = target.health - dice_roll - self.agility

        elif (self.weapon == dagger):
            dice_roll = random.randint(1,4)
            target.health = target.health - dice_roll - self.agility

        elif (self.weapon == longsword):
            dice_roll = random.randint(1,12)
            target.health = target.health - dice_roll - self.agility

        elif (self.weapon == melee):
            target.health = target.health - 1 - self.strength

        target.health_bar.update()
        
    
    def add_luck():
        pass

    def initial_item(self):
        if (self.__class__ == Rogue):
            initial_item_rogue = random.randint(1,3)
            if (initial_item_rogue == 1):
                 self.weapon = dagger
            elif (initial_item_rogue == 2):
                 self.weapon = longbow    
            elif (initial_item_rogue == 3):
                 self.weapon = longsword

        if (self.__class__ == Fighter):
            initial_item_figther = random.randint(1,3)      
            if (initial_item_figther == 1):
                 self.weapon = small_axe
            elif (initial_item_figther == 2):
                 self.weapon = javelin
            elif (initial_item_figther == 3):
                self.weapon = battleaxe


class Rogue(Player):
    def __init__(self,
                name:str,
                health:int):

        self.agility = 1
        self.strength = 0
        self.name = name
        self.weapon = melee
        self.health = health
        self.max_health = health
        self.health_bar = HealthBar(self, color="blue")

class Fighter(Player):
    def __init__(self,
                name:str,
                health:int):

        self.agility = 0
        self.strength = 1
        self.name = name
        self.health = health
        self.max_health = health
        self.weapon = melee
        self.health_bar = HealthBar(self, color="green")