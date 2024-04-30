import random
import time
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
            print(f"\nVocê brandeia seu(a) {self.weapon.name}, causando {target.health - dice_roll - self.strength} de dano ao inimigo.")
            target.health = target.health - dice_roll - self.strength

        elif (self.weapon == small_axe):
            dice_roll = random.randint(1,4)
            print(f"\nVocê brandeia seu(a) {self.weapon.name}, causando {target.health - dice_roll - self.strength} de dano ao inimigo.")
            target.health = target.health - dice_roll - self.strength

        elif (self.weapon == javelin):
            dice_roll = random.randint(1,6)
            print(f"\nVocê brandeia seu(a) {self.weapon.name}, causando {target.health - dice_roll - self.strength} de dano ao inimigo.")            
            target.health = target.health - dice_roll - self.strength

        elif (self.weapon == longbow):
            dice_roll = random.randint(1,6)
            print(f"\nVocê brandeia seu(a) {self.weapon.name}, causando {target.health - dice_roll - self.agility} de dano ao inimigo.")            
            target.health = target.health - dice_roll - self.agility

        elif (self.weapon == dagger):
            dice_roll = random.randint(1,4)
            print(f"\nVocê brandeia seu(a) {self.weapon.name}, causando {target.health - dice_roll - self.agility} de dano ao inimigo.")            
            target.health = target.health - dice_roll - self.agility

        elif (self.weapon == longsword):
            dice_roll = random.randint(1,12)
            print(f"\nVocê brandeia seu(a) {self.weapon.name}, causando {target.health - dice_roll - self.agility} de dano ao inimigo.")            
            target.health = target.health - dice_roll - self.agility

        elif (self.weapon == melee):
            target.health = target.health - 1 - self.strength

        target.health_bar.update()
        
    def get_item(self):
        tabela_inwhile = random.randint(0,75)
        if (tabela_inwhile >=1 and tabela_inwhile <=10):
            print("Você vasculha a floresta e acha...")
            time.sleep(1)
            print('.')
            time.sleep(1)
            print('.')
            time.sleep(1)
            print('.')
            time.sleep(2)
            print('Um Talismã do Luchador Novato! Sua força aumenta em 1.')
            time.sleep(0.5)
            self.strength += 1 
    
        elif (tabela_inwhile >=11 and tabela_inwhile <=15):
            print("Você vasculha a floresta e acha...")
            time.sleep(1)
            print('.')
            time.sleep(1)
            print('.')
            time.sleep(1)
            print('.')
            time.sleep(2)
            print('Um Talismã do Luchador Profissional! Sua força aumenta em 2.')
            time.sleep(0.5)
            self.strength += 2

        elif (tabela_inwhile >=16 and tabela_inwhile <=18):
            print("Você vasculha a floresta e acha...")
            time.sleep(1)
            print('.')
            time.sleep(1)
            print('.')
            time.sleep(1)
            print('.')
            time.sleep(2)
            print('Um Talismã do Luchador Supremo! Sua força aumenta em 3.')
            time.sleep(0.5)
            self.strength += 3

        elif (tabela_inwhile >=20 and tabela_inwhile <=30):
            print("Você vasculha a floresta e acha...")
            time.sleep(1)
            print('.')
            time.sleep(1)
            print('.')
            time.sleep(1)
            print('.')
            time.sleep(2)
            print('Um Talismã do Ladrão Trombadinha! Sua agilidade aumenta em 1.')
            time.sleep(0.5)
            self.agility += 1

        elif (tabela_inwhile >=31 and tabela_inwhile <=35):
            print("Você vasculha a floresta e acha...")
            time.sleep(1)
            print('.')
            time.sleep(1)
            print('.')
            time.sleep(1)
            print('.')
            time.sleep(2)
            print('Um Talismã do Ladrão Profissional! Sua agilidade aumenta em 2.')
            time.sleep(0.5)
            self.agility += 2

        elif (tabela_inwhile >=36 and tabela_inwhile <=38):
            print("Você vasculha a floresta e acha...")
            time.sleep(1)
            print('.')
            time.sleep(1)
            print('.')
            time.sleep(1)
            print('.')
            time.sleep(2)
            print('Um Talismã do Ladrão Especialista! Sua agilidade aumenta em 3.')
            time.sleep(0.5)
            self.agility += 3

        else:
            print("Você vasculha a floresta e acha...")
            time.sleep(1)
            print('.')
            time.sleep(1)
            print('.')
            time.sleep(1)
            print('.')
            time.sleep(2)
            print('Nada.')
            time.sleep(0.5)

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