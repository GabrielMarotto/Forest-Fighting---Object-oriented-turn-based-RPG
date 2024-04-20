import random
import time
from Personagens import Player,Rogue, Fighter
from Weapons import javelin,small_axe, battleaxe, longbow, longsword, dagger

# Importante adicionar os time.sleep e print('.') para demonstrar um jeito de adicionar tensão ao jogo. 

#===============================#
#Método dentro do while

def add_luck():
    sorte=0
    aleatorio = random.randint(0,100)
    sorte  = aleatorio + sorte
    if (sorte > 600000000):
        get_item()
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
        print('Um Talismã do Ladrão Trombadinha! Sua força agilidade aumenta em 1.')
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
        print('Um Talismã do Ladrão Profissional! Sua força agilidade aumenta em 2.')
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
        print('Um Talismã do Ladrão Especialista! Sua força agilidade aumenta em 3.')
        time.sleep(0.5)
        self.agility += 3
	

#===============================#
#Método fora do while

def initial_item(self):
    if (Player.agility > 0):
        initial_item_rogue = random.randint(1,3)
        if (initial_item_rogue == 1):
            Player.weapon == dagger
        elif (initial_item_rogue == 2):
            Player.weapon == longbow
        elif (initial_item_rogue == 3):
            Player.weapon == longsword
    elif (Player.strength > 0):
        initial_item_figther = random.randint(1,3)
        if (initial_item_figther == 1):
            Player.weapon == small_axe
        elif (initial_item_figther == 2):
            Player.weapon == javelin
        elif (initial_item_figther == 3):
            Player.weapon = battleaxe