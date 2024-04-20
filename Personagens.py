import random
from Weapons import Weapon,battleaxe,small_axe,javelin,longbow,longsword,dagger,melee

# NOTAS
# sistema para player com maior agilidade ir primeiro

class Player:
    def __init__(self,
                name:str,
                weapon,
                health: int) -> None:
    
        self.name = name
        self.health = health
        self.weapon = weapon
        self.agility = 0 # Depois cada classe de personagem vai ganhar uma agilidade e força diferentes. Daí cada arma vai usar agilidade ou força pra dar dano.
        self.strength = 0

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

        
    
    def add_luck():
        pass

    def roll_initiative(self): 
        initiative = random.randint(1,10) + self.agility


class Rogue(Player):
    def __init__(self,
                name:str,
                weapon,
                health:int):

        self.agility = 1
        self.strength = 0
        self.name = name
        self.health = health
        self.weapon = weapon

class Fighter(Player):
    def __init__(self,
                name:str,
                weapon,
                health:int):

        self.agility = 0
        self.strength = 1
        self.name = name
        self.health = health
        self.weapon = weapon
        