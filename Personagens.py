import random
import time
from Weapons import *
from BarraVida import HealthBar


class Player:
    def __init__(self,
                name:str,
                health: int) -> None:
    
        self.name = name
        self.health = health #vida atual
        self.max_health = health #vida máxima
        self.agility =  0 #Atributo Rogue
        self.strength = 0 #Atributo Fighter
        self.intelligence = 0 #Atributo Mago
        self.wisdom = 0 #Atributo Bardo
        self.health_bar = HealthBar(self, color="green")

    def weapon_attack(self, target):
        
        if (self.weapon == battleaxe):
            dice_roll = random.randint(1,12)
            print(f"\nVocê ataca com {self.weapon.name}, causando {dice_roll + self.strength} de dano ao inimigo.")
            target.health = target.health - dice_roll - self.strength

        elif (self.weapon == small_axe):
            dice_roll = random.randint(1,4)
            print(f"\nVocê ataca com seu(a) {self.weapon.name}, causando {dice_roll + self.strength} de dano ao inimigo.")
            target.health = target.health - dice_roll - self.strength

        elif (self.weapon == javelin):
            dice_roll = random.randint(1,6)
            print(f"\nVocê ataca com seu(a) {self.weapon.name}, causando {dice_roll + self.strength} de dano ao inimigo.")            
            target.health = target.health - dice_roll - self.strength

        elif (self.weapon == longbow):
            dice_roll = random.randint(1,6)
            print(f"\nVocê ataca com seu(a) {self.weapon.name}, causando {dice_roll + self.agility} de dano ao inimigo.")            
            target.health = target.health - dice_roll - self.agility

        elif (self.weapon == dagger):
            dice_roll = random.randint(1,4)
            print(f"\nVocê ataca com seu(a) {self.weapon.name}, causando {dice_roll + self.agility} de dano ao inimigo.")            
            target.health = target.health - dice_roll - self.agility

        elif (self.weapon == longsword):
            dice_roll = random.randint(1,12)
            print(f"\nVocê ataca com seu(a) {self.weapon.name}, causando {dice_roll + self.agility} de dano ao inimigo.")            
            target.health = target.health - dice_roll - self.agility

        elif (self.weapon == arcane_spark):
            dice_roll = random.randint(1,4)
            print(f"\nVocê ataca com seu(a) {self.weapon.name}, causando {dice_roll + self.intelligence} de dano ao inimigo.")            
            target.health = target.health - dice_roll - self.intelligence

        elif (self.weapon == lightning_bolt):
            dice_roll = random.randint(1,6)
            print(f"\nVocê ataca com seu(a) {self.weapon.name}, causando {dice_roll + self.intelligence} de dano ao inimigo.")            
            target.health = target.health - dice_roll - self.intelligence

        elif (self.weapon == fireball):
            dice_roll = random.randint(1,12)
            print(f"\nVocê ataca com seu(a) {self.weapon.name}, causando {dice_roll + self.intelligence} de dano ao inimigo.")            
            target.health = target.health - dice_roll - self.intelligence

        elif (self.weapon == maracas):
            dice_roll = random.randint(1,4)
            print(f"\nVocê ataca com seu(a) {self.weapon.name}, causando {dice_roll + self.wisdom} de dano ao inimigo.")            
            target.health = target.health - dice_roll - self.wisdom

        elif (self.weapon == viola):
            dice_roll = random.randint(1,6)
            print(f"\nVocê ataca com seu(a) {self.weapon.name}, causando {dice_roll + self.wisdom} de dano ao inimigo.")            
            target.health = target.health - dice_roll - self.wisdom

        elif (self.weapon == drums):
            dice_roll = random.randint(1,12)
            print(f"\nVocê ataca com seu(a) {self.weapon.name}, causando {dice_roll + self.wisdom} de dano ao inimigo.")            
            target.health = target.health - dice_roll - self.wisdom

        elif (self.weapon == melee):
            target.health = target.health - 1 - self.strength

        if (target.health < 0):
            target.health = 0
            
        target.health_bar.update()

        
    def get_item(self):
        tabela_inwhile = random.randint(0,40)
        if(self.__class__ == Fighter):
            if (tabela_inwhile >=1 and tabela_inwhile <=10):
                print("Você vasculha a floresta e acha...")
                time.sleep(1)
                print('.')
                time.sleep(1)
                print('.')
                time.sleep(1)
                print('.')
                time.sleep(2)
                print('Um Talismã do marombeiro frango! Sua força aumenta em 3.')
                time.sleep(4)
                self.strength += 3 
        
            elif (tabela_inwhile >=11 and tabela_inwhile <=15):
                print("Você vasculha a floresta e acha...")
                time.sleep(1)
                print('.')
                time.sleep(1)
                print('.')
                time.sleep(1)
                print('.')
                time.sleep(2)
                print('Um Talismã do rato de academia! Sua força aumenta em 5.')
                time.sleep(4)
                self.strength += 5

            elif (tabela_inwhile >=16 and tabela_inwhile <=20):
                print("Você vasculha a floresta e acha...")
                time.sleep(1)
                print('.')
                time.sleep(1)
                print('.')
                time.sleep(1)
                print('.')
                time.sleep(2)
                print('Um Talismã do Mister Olympia! Sua força aumenta em 8.')
                time.sleep(4)
                self.strength += 8

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
                time.sleep(1)
                
        if(self.__class__ == Rogue):
            if (tabela_inwhile >=1 and tabela_inwhile <=10):
                print("Você vasculha a floresta e acha...")
                time.sleep(1)
                print('.')
                time.sleep(1)
                print('.')
                time.sleep(1)
                print('.')
                time.sleep(2)
                print('Um Talismã do red bull! Sua agilidade aumenta em 3.')
                time.sleep(4)
                self.agility += 3 
        
            elif (tabela_inwhile >=11 and tabela_inwhile <=15):
                print("Você vasculha a floresta e acha...")
                time.sleep(1)
                print('.')
                time.sleep(1)
                print('.')
                time.sleep(1)
                print('.')
                time.sleep(2)
                print('Um Talismã do gato laranja! Sua agilidade aumenta em 5.')
                time.sleep(4)
                self.agility += 5

            elif (tabela_inwhile >=16 and tabela_inwhile <=20):
                print("Você vasculha a floresta e acha...")
                time.sleep(1)
                print('.')
                time.sleep(1)
                print('.')
                time.sleep(1)
                print('.')
                time.sleep(2)
                print('Um Talismã do universitário fim de semestre! Sua agilidade aumenta em 8.')
                time.sleep(4)
                self.agility += 8

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
                time.sleep(1)

        if(self.__class__ == Wizard):
            if (tabela_inwhile >=1 and tabela_inwhile <=10):
                print("Você vasculha a floresta e acha...")
                time.sleep(1)
                print('.')
                time.sleep(1)
                print('.')
                time.sleep(1)
                print('.')
                time.sleep(2)
                print('Um Talismã do auto-didata! Sua inteligência aumenta em 3.')
                time.sleep(4)
                self.intelligence += 3 
        
            elif (tabela_inwhile >=11 and tabela_inwhile <=15):
                print("Você vasculha a floresta e acha...")
                time.sleep(1)
                print('.')
                time.sleep(1)
                print('.')
                time.sleep(1)
                print('.')
                time.sleep(2)
                print('Um Talismã do jogador de DoTa! Sua inteligência aumenta em 5.')
                time.sleep(4)
                self.intelligence += 5

            elif (tabela_inwhile >=16 and tabela_inwhile <=20):
                print("Você vasculha a floresta e acha...")
                time.sleep(1)
                print('.')
                time.sleep(1)
                print('.')
                time.sleep(1)
                print('.')
                time.sleep(2)
                print('Um Talismã do jogador de Valorant! Sua inteligência aumenta em 8.')
                time.sleep(4)
                self.intelligence += 8

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
                time.sleep(1)

        if(self.__class__ == Bard):
            if (tabela_inwhile >=1 and tabela_inwhile <=10):
                print("Você vasculha a floresta e acha...")
                time.sleep(1)
                print('.')
                time.sleep(1)
                print('.')
                time.sleep(1)
                print('.')
                time.sleep(2)
                print('Um Talismã do aprendiz! Sua sabedoria aumenta em 3.')
                time.sleep(4)
                self.wisdom += 3 
        
            elif (tabela_inwhile >=11 and tabela_inwhile <=15):
                print("Você vasculha a floresta e acha...")
                time.sleep(1)
                print('.')
                time.sleep(1)
                print('.')
                time.sleep(1)
                print('.')
                time.sleep(2)
                print('Um Talismã do multi-instrumentalista! Sua sabedoria aumenta em 5.')
                time.sleep(4)
                self.wisdom += 5

            elif (tabela_inwhile >=16 and tabela_inwhile <=20):
                print("Você vasculha a floresta e acha...")
                time.sleep(1)
                print('.')
                time.sleep(1)
                print('.')
                time.sleep(1)
                print('.')
                time.sleep(2)
                print('Um Talismã do virtuoso! Sua sabedoria aumenta em 8.')
                time.sleep(4)
                self.wisdom += 8

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
                time.sleep(1)
        
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

        if (self.__class__ == Wizard):
            initial_item_wizard = random.randint(1,3)      
            if (initial_item_wizard == 1):
                 self.weapon = arcane_spark
            elif (initial_item_wizard == 2):
                 self.weapon = lightning_bolt
            elif (initial_item_wizard == 3):
                self.weapon = fireball

        if (self.__class__ == Bard):
            initial_item_bard = random.randint(1,3)      
            if (initial_item_bard == 1):
                 self.weapon = maracas
            elif (initial_item_bard == 2):
                 self.weapon = viola
            elif (initial_item_bard == 3):
                self.weapon = drums


class Rogue(Player):
    def __init__(self,
                name:str,
                health:int):

        self.agility = 1
        self.strength = 0
        self.intelligence = 0
        self.wisdom = 0
        self.name = name
        self.weapon = melee
        self.health = health
        self.max_health = health
        self.health_bar = HealthBar(self, color="blue")

    def sneak_attack(self,target):
        sneak_attack = random.randint(4,9)
        if (self.weapon == longbow):
            dice_roll = random.randint(1,6)
            print(f"\nVocê ataca com seu(a) {self.weapon.name}, causando {dice_roll + self.agility + sneak_attack} de dano ao inimigo.")            
            target.health = target.health - dice_roll - self.agility - sneak_attack

        elif (self.weapon == dagger):
            dice_roll = random.randint(1,4)
            print(f"\nVocê ataca com seu(a) {self.weapon.name}, causando {dice_roll + self.agility + sneak_attack} de dano ao inimigo.")            
            target.health = target.health - dice_roll - self.agility - sneak_attack

        elif (self.weapon == longsword):
            dice_roll = random.randint(1,12)
            print(f"\nVocê ataca com seu(a) {self.weapon.name}, causando {dice_roll + self.agility + sneak_attack} de dano ao inimigo.")            
            target.health = target.health - dice_roll - self.agility - sneak_attack 

        elif (self.weapon == melee):
            print(f"\nVocê ataca com seu(a) {self.weapon.name}, causando {sneak_attack} de dano ao inimigo.")            
            target.health = target.health - sneak_attack 

        target.health_bar.update()

class Fighter(Player):
    def __init__(self,
                name:str,
                health:int):

        self.agility = 0
        self.strength = 1
        self.intelligence = 0
        self.wisdom = 0
        self.name = name
        self.health = health
        self.max_health = health
        self.weapon = melee
        self.health_bar = HealthBar(self, color="green")

class Wizard(Player):
    def __init__(self,
                name:str,
                health:int):

        self.agility = 0
        self.strength = 0
        self.intelligence = 1
        self.wisdom = 0
        self.name = name
        self.health = health
        self.max_health = health
        self.weapon = melee
        self.health_bar = HealthBar(self, color="yellow")

    def drain_health(self,target):
        if (self.health < 50):
            print(f"Você canaliza sua energia arcana, drenando 10 pontos de vida do inimigo e adicionando a sua.")
            target.health = target.health - 10
            self.health = self.health + 10

        if (self.health > 50):    
            self.health = 50

        self.health_bar.update()
        target.health_bar.update()

class Bard(Player):
    def __init__(self,
                name:str,
                health:int):

        self.agility = 0
        self.strength = 0
        self.intelligence = 0
        self.wisdom = 1
        self.name = name
        self.health = health
        self.max_health = health
        self.weapon = melee
        self.health_bar = HealthBar(self, color="red")

    def life_song(self):
        rest_song_roll = random.randint(8,16)
        rest_song_health = rest_song_roll + self.wisdom
        print(f"Você toca uma melodia para acalmar seu coração e focar sua mente. Você recupera {rest_song_health} de vida.")
        self.health = self.health + rest_song_health
        self.health_bar.update()