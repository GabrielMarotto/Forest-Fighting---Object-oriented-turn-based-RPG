import random
import time
from Personagens import Player,Rogue, Fighter
from Weapons import javelin,small_axe, battleaxe, longbow, longsword, dagger, melee

# Menu principal pré-while, ainda vou fazer uns gráficos dentro do terminal mas por enquanto to deixando assim.

print("Bem-vindo ao Forest Fighting!")
escolha_p1 = input("\n Jogador 1, escolha seu personagem.\n\n[1]Ladino\n[2]Guerreiro\n\n----->")
escolha_p2 = input("\n Jogador 2, escolha seu personagem.\n\n[1]Ladino\n[2]Guerreiro\n\n----->")

escolha_p1 = escolha_p1.lower()
escolha_p2 = escolha_p2.lower()

if (escolha_p1 == "1" or escolha_p1 == "ladino"):
    Player1 = Rogue("Ladino",100)
elif (escolha_p1 == "2" or escolha_p1 == "guerreiro"):
    Player1 = Fighter("Guerreiro",100)

Player1.initial_item()
print(f"O {Player1.name} vasculha a floresta por uma arma, e acha...")
# #time.sleep(1)
# print('.')
# #time.sleep(1)
# print('.')
# #time.sleep(1)
# print('.')
# #time.sleep(2)
print(f'{Player1.weapon.name}!')
# time.sleep(0.5)

if (escolha_p2 == "1" or escolha_p2 == "ladino"):
    Player2 = Rogue("Ladino",100)
elif (escolha_p2 == "2" or escolha_p2 == "guerreiro"):
    Player2 = Fighter("Guerreiro",100)

Player2.initial_item()
print(f"O {Player2.name} vasculha a floresta por uma arma, e acha...")
# time.sleep(1)
# print('.')
# time.sleep(1)
# print('.')
# time.sleep(1)
# print('.')
# time.sleep(2)
print(f'{Player2.weapon.name}!')
# time.sleep(0.5)