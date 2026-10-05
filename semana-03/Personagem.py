from time import sleep
#VARIAVEIS
characters = []

#Funções

#Cadastro de Personagens
def cadastrar_personagem():
    name = str(input("Digite o nome do Personagem:"))
    hp = int(input("Vida máxima do Personagem: "))
    atk = int(input("Força do Personagem: "))
    defense = int(input("Defesa do Personagem: "))
    level = int(input("Level do Personagem: "))
    exp = int(input("Experiência do Personagem: "))
    personagem = {"NAME": name, "HP": hp, "ATK": atk, "DEF": defense, "LEVEL": level, "EXP": exp}
    characters.append(personagem)
    print("ADICIONADO COM SUCESSO!")
    sleep(1.5)

#Consulta de Personagens
def consultar_personagem():
    search_character = False
    search_name = input("Digite o nome do Personagem que deseja procurar: ")

    for personagem in characters:
        if search_name == personagem["NAME"]:
            search_character = True

            print("Personagem encontrado!")

            print(f"Nome: {personagem['NAME']}\n"
                  f"Vida: {personagem['HP']}\n"
                  f"Ataque: {personagem['ATK']}\n"
                  f"Defesa: {personagem['DEF']}\n"
                  f"Level: {personagem['LEVEL']}\n"
                  f"Experiência(XP): {personagem['EXP']}")

            input("Enter para finalizar consulta: ")
            break

    if not search_character:
        print("Personagem não encontrado")

    sleep(1)


def alterar_personagem():

    if len(characters) == 0:
        print("Não há personagens cadastrados.")
        return

    search_character = input(
        "Digite o nome do personagem que você deseja alterar: "
    )

    personagem_encontrado = None

    for personagem in characters:
        if personagem["NAME"] == search_character:
            personagem_encontrado = personagem
            break

    if personagem_encontrado is None:
        print("Personagem não encontrado.")
        return

    print("Qual dado deseja alterar?")
    print("(1) Vida")
    print("(2) Nível")
    print("(3) Experiência")

    search_data = int(input("Digite: "))

    match search_data:

        case 1:
            personagem_encontrado["HP"] = int(
                input("Digite a nova vida: ")
            )
            print("Vida alterada.")

        case 2:
            personagem_encontrado["LEVEL"] = int(
                input("Digite o novo level: ")
            )
            print("Level alterado.")

        case 3:
            personagem_encontrado["EXP"] = int(
                input("Digite a nova experiência: ")
            )
            print("EXP alterado.")

        case _:
            print("Opção inválida.")

    sleep(1.5)