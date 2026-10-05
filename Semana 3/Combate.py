from Personagem import characters
from time import sleep 

#MENU COMBATE 
def menu_combate(): 

    #Variaveis 
    enemy = {} 
    character = {} 

    # ESCOLHER PERSONAGEM
    while True:

        try:

            name_character = str(input("Digite o nome do personagem: ")) 

            for personagem in characters:
                if name_character == personagem["NAME"]:
                    character = personagem
                    print("Personagem encontrado!")
                    sleep(1.5)
                    break

            if character == {}:
                print("Personagem não encontrado. ")
                print("Tente novamente.\n")
                continue

            break

        except Exception:

            print("Erro ao procurar personagem.")
            print("Tente novamente.\n")


    # ESCOLHER INIMIGO
    while True:

        print("Com qual inimigo deseja lutar?:\n (1) Lobo\n (2) Goblin\n (3) Dragão") 

        try:

            num_enemy = int(input("Digite o numero do Inimigo: ")) 

            if num_enemy == 1: 
                enemy = {"NAME": "Lobo", "HP": 50, "ATK": 12, "DEF": 5} 

            elif num_enemy == 2: 
                enemy = {"NAME": "Goblin", "HP": 70, "ATK": 15, "DEF": 8} 

            elif num_enemy == 3: 
                enemy = {"NAME": "Dragão", "HP": 200, "ATK": 30, "DEF": 20} 

            else:
                print("Inimigo não está entre as opções possíveis. ")
                print("Tente novamente.\n")
                continue

            break

        except ValueError:

            print("Digite apenas números!")
            print("Tente novamente.\n")

        except Exception:

            print("Erro inesperado.")
            print("Tente novamente.\n")


    combate(enemy, character)


def combate_ataque_enemy(character, enemy, defendeu):

    try:

        dano = 0

        if defendeu: 
            dano = enemy["ATK"] - character["DEF"] * 1.4

        else: 
            dano = enemy["ATK"] - character["DEF"]

        if(dano < 0): 
            dano = 0

        if character["HP"] - dano > 0: character["HP"] -= dano
        else: character["HP"] = 0

        print(f"Você tomou um ataque que tirou {dano:.0f} de HP.")
        sleep(1.5)

    except KeyError:

        print("Erro: dados do personagem ou inimigo estão incompletos.")
        sleep(1)

    except TypeError:

        print("Erro: dados possuem um tipo inválido.")
        sleep(1)

    except Exception:

        print("Erro inesperado durante o ataque.")
        sleep(1)


def combate_ataque_player(character, enemy):

    try:

        dano = 0
        dano = character["ATK"] - enemy["DEF"]

        if(dano < 0): 
            dano = 0

        enemy["HP"] -= dano

        print(f"Você atacou e tirou {dano:.0f} de HP.")
        sleep(1.5)

        if(enemy["HP"] > 0):
            combate_ataque_enemy(character, enemy, False)

    except KeyError:

        print("Erro: dados do personagem ou inimigo estão incompletos.")
        sleep(1)

    except TypeError:

        print("Erro: dados possuem um tipo inválido.")
        sleep(1)

    except Exception:

        print("Erro inesperado durante o ataque.")
        sleep(1)


def combate(enemy, character):

    print("---------------- COMBATE ----------------")

    while character["HP"] > 0 and enemy["HP"] > 0:

        try:

            print(f"{character['NAME']}\nHP: {character['HP']}\nATK: {character['ATK']}\nDEF: {character['DEF']}")

        except KeyError:

            print("Erro: dados do personagem estão incompletos.")
            return

        print("\n VS \n")

        try:

            print(f"{enemy['NAME']}\nHP: {enemy['HP']}\nATK: {enemy['ATK']}\nDEF: {enemy['DEF']}")

        except KeyError:

            print("Erro: dados do inimigo estão incompletos.")
            return

        # ESCOLHER AÇÃO
        while True:

            try:

                choose = int(input("O que deseja fazer?\n(1) Atacar\n(2) Defender\n(3) Fugir\nEscolha: "))

                match choose:

                    case 1:

                        combate_ataque_player(character, enemy)
                        break

                    case 2: 

                        combate_ataque_enemy(character, enemy, True)
                        break

                    case 3:

                        print(" VOCÊ FUGIU DA LUTA! ")
                        return

                    case _:

                        print("Escolha apenas 1, 2 ou 3!")
                        print("Tente novamente.\n")

            except ValueError:

                print("Digite apenas números!")
                print("Tente novamente.\n")

            except Exception:

                print("Erro inesperado!")
                print("Tente novamente.\n")


    print("\n ------------ FIM DA BATALHA ------------ \n")

    if enemy["HP"] > 0: 
        print("O Player perdeu. ")

    else: 
        print("O inimigo perdeu. ")