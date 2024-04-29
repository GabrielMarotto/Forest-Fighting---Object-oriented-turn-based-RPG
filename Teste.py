import random
from Personagens import Player,Rogue,Fighter
from Weapons import Weapon,battleaxe,small_axe,javelin,longbow,longsword,dagger,melee
from BarraVida import HealthBar

p1=Rogue('Player 1',100)
p2=Fighter('Player 2',100)

while (p1.health > 0 and p2.health > 0):
    p1.weapon_attack(p2)
    p2.weapon_attack(p1)
    
    p1.health_bar.draw()
    p2.health_bar.draw()
