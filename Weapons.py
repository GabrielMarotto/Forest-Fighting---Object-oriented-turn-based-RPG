import random

class Weapon:
    def __init__(self,
                 name:str,
                 damage_type:str) -> None:
        self.name = name





battleaxe = Weapon('Battleaxe','strength')
small_axe = Weapon('Small axe','strength')
javelin = Weapon('Javelin','strength')

longbow = Weapon('Longbow','agility') 
dagger = Weapon('Dagger','agility')
longsword = Weapon('Longsword','agility')

melee = Weapon('Melee','strength')