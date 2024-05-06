import random
from Personagens import *
from Weapons import Weapon,battleaxe,small_axe,javelin,longbow,longsword,dagger,melee
from BarraVida import HealthBar

p1=Rogue('Player 1',50)
p2=Wizard('Player 2',50)

while (p1.health > 0 and p2.health > 0):
    p1.sneak_attack(p2)
    p2.drain_health(p1)
    
    p1.health_bar.draw()
    p2.health_bar.draw()
