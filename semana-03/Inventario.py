from time import sleep


# VARIÁVEIS

types_itens = ["ARMA", "CONSUMÍVEL", "DEFESA", "QUEST"]

sword = ("ESPADA", types_itens[0])
potion = ("POÇÃO", types_itens[1])
shield = ("ESCUDO", types_itens[2])
maps = ("MAPA", types_itens[3])

inventory = [sword, potion, potion, potion, shield, maps]


# FUNÇÕES


# Mostrar inventário
def mostrar_inventario():

    indicie = 1

    for nome, tipo in inventory:
        print(f"{indicie} - {nome.capitalize()} || {tipo}")
        indicie += 1
        sleep(0.5)


# Adicionar item
def adicionar_item():

    name_item = input("Nome do item: ").upper()
    type_item = input("Tipo do item: ").upper()

    while type_item not in types_itens:
        type_item = input(
            "Tipo incorreto, digite o tipo novamente: "
        ).upper()

    new_item = (name_item, type_item)

    inventory.append(new_item)

    print(f"Item {name_item.capitalize()} adicionado ao inventário!")


# Remover item
def remover_item():

    name_item = input(
        "Digite o nome do item que deseja remover: "
    ).upper()

    indicie = -1
    remove = False

    for item in inventory:

        indicie += 1

        nome, tipo = item

        if nome == name_item:

            remove = True

            inventory.pop(indicie)

            break

    if not remove:
        print("Nenhum item com esse nome encontrado")
    else:
        print("Item removido!")

    sleep(1.5)


# Procurar item
def procurar_item():

    name_item = input(
        "Digite o nome do item que deseja buscar: "
    ).upper()

    search = False

    for nome, tipo in inventory:

        if nome == name_item:
            search = True
            break

    if search:
        print("Item no inventário!")
    else:
        print("Você não possui o item.")

    sleep(1.5)


# Ver quantidade de itens
def quantidade_itens():

    quant_itens = 0

    for item in inventory:
        quant_itens += 1

    print(f"Quantidade de itens: {quant_itens}")

    sleep(1.5)