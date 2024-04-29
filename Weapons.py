import random

class Weapon:
    def __init__(self,
                 name:str,
                 damage_type:str) -> None:
        self.name = name





battleaxe = Weapon('Machado de batalha','strength')
small_axe = Weapon('Machado pequeno','strength')
javelin = Weapon('Lança','strength')

longbow = Weapon('Arco longo','agility') 
dagger = Weapon('Adaga','agility')
longsword = Weapon('Espada longa','agility')

melee = Weapon('Punhos','strength')