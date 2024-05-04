import random

class Weapon:
    def __init__(self,
                 name:str,
                 damage_type:str,
                 tier:str) -> None:
        self.name = name
        self.tier = tier


#Objetos de armas já criados

#Fighter
small_axe = Weapon('Machado quebrado','strength','Tier 1')
javelin = Weapon('Lança','strength','Tier 2')
battleaxe = Weapon('Machado de batalha','strength',"Tier 3")

#Rogue
dagger = Weapon('Adaga Enferrujada','agility','Tier 1')
longbow = Weapon('Arco longo','agility','Tier 2') 
longsword = Weapon('Espada longa','agility','Tier 3')

#Wizard
arcane_spark = Weapon('Faísca arcana','intelligence','Tier 1')
lightning_bolt = Weapon('Raio de Eletricidade','intelligence','Tier 2')
fireball = Weapon('Bola de fogo', 'intelligence', 'Tier 3')

#Bard
maracas = Weapon('Maracas','wisdom','Tier 1')
viola = Weapon('Viola', 'wisdom', 'Tier 2')
drums = Weapon('Bateria','wisdom', 'Tier 3')

melee = Weapon('Punhos','strength', 'Tier 0')