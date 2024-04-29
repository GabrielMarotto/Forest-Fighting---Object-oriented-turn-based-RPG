import random
import time
from Personagens import Player,Rogue, Fighter
from Weapons import javelin,small_axe, battleaxe, longbow, longsword, dagger, melee
from lib import *
from BarraVida import HealthBar

# Menu principal pré-while, ainda vou fazer uns gráficos dentro do terminal mas por enquanto to deixando assim.

print(f"{"—"*42}\n"
      f"|                                        |\n"
      f"|                                        |\n"
      f"|                  FOREST                |\n"
      f"|                 FIGHTING               |\n"
      f"|                   v1.0                 |\n"
      f"|                                        |\n"
      f"|                                        |\n"
      f"{"—"*42}")
# time.sleep(2)
print("\n\nVocê se encontra no meio da Floresta dos Elfos Selvagens, com um inimigo a sua frente.")
# time.sleep(3)
print("A floresta contém tudo o que você precisa para a vitória...")
# time.sleep(3)
print("se a sorte estiver do seu lado.")
# time.sleep(2)


print("-"*42)
escolha_p1 = input("\n Jogador 1, escolha seu personagem.\n\n[1]Ladino\n[2]Guerreiro\n\n----->")
escolha_p2 = input("\n Jogador 2, escolha seu personagem.\n\n[1]Ladino\n[2]Guerreiro\n\n----->")

escolha_p1 = escolha_p1.lower()
escolha_p2 = escolha_p2.lower()
print("-"*42)

if (escolha_p1 == "1" or escolha_p1 == "ladino"):
    Player1 = Rogue("Jogador 1",100)
elif (escolha_p1 == "2" or escolha_p1 == "guerreiro"):
    Player1 = Fighter("Jogador 1",100)

Player1.initial_item()
print(f"O Jogador 1 vasculha a floresta por uma arma, e acha...")
# time.sleep(1)
# print('.')
# time.sleep(1)
# print('.')
# time.sleep(1)
# print('.')
# time.sleep(2)
print(f'Um(a) {Player1.weapon.name}!')
# time.sleep(0.5)

if (escolha_p2 == "1" or escolha_p2 == "ladino"):
    Player2 = Rogue("Jogador 2",100)
elif (escolha_p2 == "2" or escolha_p2 == "guerreiro"):
    Player2 = Fighter("Jogador 2",100)

Player2.initial_item()
print(f"O Jogador 2 vasculha a floresta por uma arma, e acha...")
# time.sleep(1)
# print('.')
# time.sleep(1)
# print('.')
# time.sleep(1)
# print('.')
# time.sleep(2)
print(f'Um(a) {Player2.weapon.name}!')
# time.sleep(2)

cabecalho("O CONFRONTO COMEÇA, ATÉ A MORTE!")

while (Player1.health > 0 and Player2.health > 0):
    cabecalho("JOGADOR 1")
    escolha = input("\n[1] Atacar\n[2]Vasculhar a floresta\n\n---->")
    
    if (escolha == "1"):
        Player1.weapon_attack(Player2)
        Player2.health_bar.draw()

    elif (escolha == "2"):
        Player1.add_luck()
    
    print("-"*42)
    cabecalho("JOGADOR 2")
    escolha = input("\n[1] Atacar\n[2]Vasculhar a floresta\n\n---->")

    if (escolha == "1"):
        Player2.weapon_attack(Player1)
        Player1.health_bar.draw()

    elif (escolha == "2"):
        Player2.add_luck()