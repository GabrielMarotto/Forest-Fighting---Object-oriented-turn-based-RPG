import random
from Personagens import Player,Rogue,Fighter
from Weapons import Weapon,battleaxe,small_axe,javelin,longbow,longsword,dagger,melee

p1=Rogue('Player 1',longbow,100)
p2=Fighter('Player 2',longbow,100)

while (p1.health > 0 and p2.health > 0):
    p1.weapon_attack(p2)
    print(f"{p1.name} atacou {p2.name} com {p1.weapon.name}, {p2.name} agora tem {p2.health} de vida.")
    p2.weapon_attack(p1)
    print(f"{p2.name} atacou {p1.name} com {p2.weapon.name}, {p1.name} agora tem {p1.health} de vida.")

