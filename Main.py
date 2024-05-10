import os
import random
import time
from Personagens import Player,Rogue, Fighter, Wizard, Bard
from Weapons import *
from lib import *
from BarraVida import HealthBar

# Menu principal pré-while
start_graphic()

time.sleep(2)
print("\n\nVocê se encontra no meio da Floresta dos Elfos Selvagens, com um inimigo a sua frente.")
time.sleep(3)
print("A floresta contém tudo o que você precisa para a vitória...")
time.sleep(3)
print("se a sorte estiver do seu lado.")
time.sleep(3)

os.system("cls")


# Menu principal de escolhas do jogador
print(linha())
escolha_p1 = input("\nJogador 1, escolha seu personagem.\n\n[1]Ladino\n[2]Guerreiro\n[3]Mago\n[4]Bardo\n\n----->")
while escolha_p1 not in ["1", "2", "3", "4"]:
    cabecalho("Opção inválida, por favor escolha um número da lista!")
    time.sleep(1)
    escolha_p1 = input("\nJogador 1, escolha seu personagem.\n\n[1]Ladino\n[2]Guerreiro\n[3]Mago\n[4]Bardo\n\n----->")
nome_p1 = input("Jogador 1, qual seu nome? ")

time.sleep(1)
os.system("cls")
print(linha())

escolha_p2 = input("\nJogador 2, escolha seu personagem.\n\n[1]Ladino\n[2]Guerreiro\n[3]Mago\n[4]Bardo\n\n----->")
while escolha_p2 not in ["1", "2", "3", "4"]:
    cabecalho("Opção inválida, por favor escolha um número da lista!")
    time.sleep(1)
    escolha_p2 = input("\nJogador 2, escolha seu personagem.\n\n[1]Ladino\n[2]Guerreiro\n[3]Mago\n[4]Bardo\n\n----->")
nome_p2 = input("Jogador 2, qual seu nome? ")

os.system("cls")

escolha_p1 = escolha_p1.lower()
escolha_p2 = escolha_p2.lower()


#Criando os objetos de cada jogador e decidindo seu item inicial
#Player 1
if (escolha_p1 == "1" or escolha_p1 == "ladino"):
    Player1 = Rogue(nome_p1,50)
elif (escolha_p1 == "2" or escolha_p1 == "guerreiro"):
    Player1 = Fighter(nome_p1,70)
elif (escolha_p1 == "3" or escolha_p1 == "mago"):
    Player1 = Wizard(nome_p1,50)
elif (escolha_p1 == "4" or escolha_p1 == "bardo"):
    Player1 = Bard(nome_p1,50)

print(linha())
Player1.initial_item()
print(f"{nome_p1} vasculha a floresta por uma arma, e acha...")
time.sleep(1)
print('.')
time.sleep(1)
print('.')
time.sleep(1)
print('.')
time.sleep(2)
print(f'Um(a) {Player1.weapon.name}!')
time.sleep(2.5)

#Player2
if (escolha_p2 == "1" or escolha_p2 == "ladino"):
    Player2 = Rogue(nome_p2,50)
elif (escolha_p2 == "2" or escolha_p2 == "guerreiro"):
    Player2 = Fighter(nome_p2,70)
elif (escolha_p2 == "3" or escolha_p2 == "mago"):
    Player2 = Wizard(nome_p2,50)
elif (escolha_p2 == "4" or escolha_p2 == "bardo"):
    Player2 = Bard(nome_p2,50)

print(linha())
Player2.initial_item()
print(f"{nome_p2} vasculha a floresta por uma arma, e acha...")
time.sleep(1)
print('.')
time.sleep(1)
print('.')
time.sleep(1)
print('.')
time.sleep(2)
print(f'Um(a) {Player2.weapon.name}!')
time.sleep(2.5)

os.system("cls")
cabecalho("O CONFRONTO COMEÇA, ATÉ A MORTE!")
time.sleep(2.5)
cont_rogue_p1 = 0
cont_wizard_p1 = 0
cont_bard_p1 = 0

cont_rogue_p2 = 0
cont_wizard_p2 = 0
cont_bard_p2 = 0

#Aqui começa os turnos dos jogadores
while (Player1.health > 0 and Player2.health > 0):
    #TURNO DO JOGADOR 1
    #Menu do jogador
    os.system("cls")

    print(linha())
    print(f"JOGADOR 1 ({nome_p1})".center(58))
    print(linha())
    print(f"ARMA:{Player1.weapon.name} ({Player1.weapon.tier}) | ATRIBUTO PRINCIPAL:{Player1.strength if Player1.strength> Player1.agility else Player1.wisdom if Player1.wisdom > Player1.agility else Player1.intelligence if Player1.intelligence > Player1.agility else Player1.agility}".center(58))
    print(linha())
    Player1.health_bar.draw()
    print(linha())

    #Ações do jogador
    
    if (Player1.__class__ == Rogue and cont_rogue_p1 == 0):
        escolha = input("\n[1] Atacar\n[2]Vasculhar a floresta\n[3]Ataque furtivo (somente um uso)\n\n---->")
    
        while (escolha !="1" and escolha !="2" and escolha != "3"):
            cabecalho("Opção não disponível")
            time.sleep(1)        
            escolha = input("\n[1] Atacar\n[2]Vasculhar a floresta\n[3]Ataque furtivo (somente um uso)\n\n---->")


        if (escolha == "1"):
            Player1.weapon_attack(Player2)
            time.sleep(2)
            Player2.health_bar.draw()
            time.sleep(2)

        elif (escolha == "2"):
            Player1.get_item()

        elif (escolha == "3"):
            Player1.sneak_attack(Player2)
            time.sleep(2)
            Player2.health_bar.draw()
            time.sleep(2)
            cont_rogue_p1 +=1

    elif (Player1.__class__ == Wizard and cont_wizard_p1 == 0):
        escolha = input("\n[1] Atacar\n[2]Vasculhar a floresta\n[3]Drenar vida (somente um uso)\n\n---->")
        
        while (escolha !="1" and escolha !="2" and escolha != "3"):
            cabecalho("Opção não disponível")
            time.sleep(1)
            escolha = input("\n[1] Atacar\n[2]Vasculhar a floresta\n[3]Drenar vida (somente um uso)\n\n---->")
             
        if (escolha == "1"):
            Player1.weapon_attack(Player2)
            time.sleep(2)
            Player2.health_bar.draw()
            time.sleep(2)

        elif (escolha == "2"):
            Player1.get_item()

        elif (escolha == "3"):
            Player1.drain_health(Player2)
            time.sleep(2)
            Player1.health_bar.draw()
            time.sleep(2)
            Player2.health_bar.draw()
            time.sleep(2)
            cont_wizard_p1 +=1

    elif (Player1.__class__ == Bard and cont_bard_p1 == 0):
        escolha = input("\n[1] Atacar\n[2]Vasculhar a floresta\n[3]Cançao da vida (somente um uso)\n\n---->")

        while (escolha !="1" and escolha !="2" and escolha != "3"):
            cabecalho("Opção não disponível")
            time.sleep(1)
            escolha = input("\n[1] Atacar\n[2]Vasculhar a floresta\n[3]Cançao da vida (somente um uso)\n\n---->")
            
        if (escolha == "1"):
            Player1.weapon_attack(Player2)
            time.sleep(2)
            Player2.health_bar.draw()
            time.sleep(2)

        elif (escolha == "2"):
            Player1.get_item()

        elif (escolha == "3"):
            Player1.life_song()
            cont_bard_p1 +=1
            time.sleep(2)
            Player1.health_bar.draw()
            time.sleep(2)
    
    else:
        escolha = input("\n[1] Atacar\n[2]Vasculhar a floresta\n\n---->")
        while (escolha !="1" and escolha !="2"):
            cabecalho("Opção não disponível") 
            time.sleep(1)
            escolha = input("\n[1] Atacar\n[2]Vasculhar a floresta\n\n---->")
            
        if (escolha == "1"):
            Player1.weapon_attack(Player2)
            time.sleep(2)
            Player2.health_bar.draw()
            time.sleep(2)

        elif (escolha == "2"):
            Player1.get_item()

    #Condicional para parar o loop caso o jogador ganhe
    if (Player2.health <= 0):
        break
    
    #TURNO DO JOGADOR 2
    #Menu do jogador
    os.system("cls")

    print(linha())
    print(f"JOGADOR 2 ({nome_p2})".center(58))
    print(linha())
    print(f"ARMA:{Player2.weapon.name} ({Player2.weapon.tier}) | ATRIBUTO PRINCIPAL:{str(Player2.strength if Player2.strength> Player2.agility else Player2.wisdom if Player2.wisdom > Player2.agility else Player2.intelligence if Player2.intelligence > Player2.agility else Player2.agility)}".center(58))
    print(linha())
    Player2.health_bar.draw()
    print(linha())

    #Ações do jogador
    if (Player2.__class__ == Rogue and cont_rogue_p2 == 0):
        escolha = input("\n[1] Atacar\n[2]Vasculhar a floresta\n[3]Ataque furtivo (somente um uso)\n\n---->")

        while (escolha !="1" and escolha !="2" and escolha != "3"):
            cabecalho("Opção não disponível") 
            time.sleep(1)
            escolha = input("\n[1] Atacar\n[2]Vasculhar a floresta\n[3]Ataque furtivo (somente um uso)\n\n---->")
        
        if (escolha == "1"):
            Player2.weapon_attack(Player1)
            time.sleep(2)
            Player1.health_bar.draw()
            time.sleep(2)

        elif (escolha == "2"):
            Player2.get_item()

        elif (escolha == "3"):
            Player2.sneak_attack(Player1)
            time.sleep(2)
            Player1.health_bar.draw()
            time.sleep(2)
            cont_rogue_p2 +=1
    #TO DO, consertar as váriaveis do menu do Player 2 a partir daqui
    elif (Player2.__class__ == Wizard and cont_wizard_p2 == 0):
        escolha = input("\n[1] Atacar\n[2]Vasculhar a floresta\n[3]Drenar vida (somente um uso)\n\n---->")
    
        while (escolha !="1" and escolha !="2" and escolha != "3"):
            cabecalho("Opção não disponível") 
            time.sleep(1)     
            escolha = input("\n[1] Atacar\n[2]Vasculhar a floresta\n[3]Drenar vida (somente um uso)\n\n---->")
    
        if (escolha == "1"):
            Player2.weapon_attack(Player1)
            time.sleep(2)
            Player1.health_bar.draw()
            time.sleep(2)

        elif (escolha == "2"):
            Player2.get_item()

        elif (escolha == "3"):
            Player2.drain_health(Player1)
            time.sleep(2)
            Player2.health_bar.draw()
            time.sleep(2)
            Player1.health_bar.draw()
            time.sleep(2)
            cont_wizard_p2 +=1

    elif (Player2.__class__ == Bard and cont_bard_p2 == 0):
        escolha = input("\n[1] Atacar\n[2]Vasculhar a floresta\n[3]Cançao da vida (somente um uso)\n\n---->")

        while (escolha !="1" and escolha !="2" and escolha != "3"):
            cabecalho("Opção não disponível") 
            time.sleep(1)
            escolha = input("\n[1] Atacar\n[2]Vasculhar a floresta\n[3]Cançao da vida (somente um uso)\n\n---->")
            
        if (escolha == "1"):
            Player2.weapon_attack(Player1)
            time.sleep(2)
            Player1.health_bar.draw()
            time.sleep(2)

        elif (escolha == "2"):
            Player2.get_item()

        elif (escolha == "3"):
            Player2.life_song()
            cont_bard_p2 +=1
            time.sleep(2)
            Player2.health_bar.draw()
            time.sleep(2)
    else:  
        escolha = input("\n[1] Atacar\n[2]Vasculhar a floresta\n\n---->")

        while (escolha !="1" and escolha !="2"):
            cabecalho("Opção não disponível")
            time.sleep(1)
            escolha = input("\n[1] Atacar\n[2]Vasculhar a floresta\n\n---->")
  
        if (escolha == "1"):
            Player2.weapon_attack(Player1)
            time.sleep(2)
            Player1.health_bar.draw()
            time.sleep(2)

        elif (escolha == "2"):
            Player2.get_item()

    #Condicional para parar o loop caso o jogador ganhe
    if (Player1.health <= 0):
        break

#Terminado o loop while, tela de vencedor.
if (Player1.health > 0):
    time.sleep(1)
    print(linha())
    print(f"{nome_p2} cai diante de sua grandeza! {nome_p1},VOCÊ É O VENCEDOR!".center(58))
    print(linha())
    time.sleep(2)
    end_graphic()


elif (Player2.health > 0):
    time.sleep(1)
    print(linha())
    print(f"{nome_p1} cai diante de sua grandeza! {nome_p2},VOCÊ É O VENCEDOR!".center(58))
    print(linha())
    time.sleep(2)
    end_graphic()