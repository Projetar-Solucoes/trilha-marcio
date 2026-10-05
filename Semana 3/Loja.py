from Inventario import inventory
from Personagem import characters

#Variaveis
itens_loja = {
("ESPADA", "ARMA"): 100,
("POÇÃO", "CONSUMÍVEL"): 25,
("ESCUDO", "DEFESA"): 80,
("MAPA", "QUEST"): 50,
("PÊSSEGO", "CONSUMÍVEL"): 12,
("ERVA", "CONSUMÍVEL"): 13
}

#Mostra a Loja e determina o personagem que irá fazer a compra
def mostrar_loja():
    character = None
    if len(characters) > 0:
        search = True

        #Pegando o Personagem
        while search: 
            found_character = str(input("Digite o nome do Personagem que irá efetuar a compra. "))
        
            for personagem in characters:
                if found_character == personagem["NAME"]:
                    print(f"Personagem encontrado: Entrando como {personagem["NAME"]}")
                    character = personagem
                    search = False
                    break
    else: 
        print("Não há personagem para fazer a compra")
        return

    #Menu
    print("----------- LOJA -----------")
    choose = -1

    while choose != 0:
        indicie = 1
        for item, preco in itens_loja.items():
            nome, tipo = item
            print(f"({indicie}): {nome}: {tipo} custa {preco} XP. \n")
            indicie += 1

        choose = int(input("Escolha o produto que deseja comprar(0 para voltar): "))
        if choose > 0: comprar_loja(choose, character)

def comprar_loja(choose, character):
    indicie = 1
    for item, preco in itens_loja.items():
        if indicie == choose:
            if character["EXP"] >= preco:
                inventory.append(item)
                character["EXP"] -= preco
                print("COMPRA EFETUADA")
                break
            else:
                print("XP INSUFICIENTE")
                break
        indicie += 1

        
