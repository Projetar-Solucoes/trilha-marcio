# BIBLIOTECAS USADAS

from Personagem import characters
from Personagem import cadastrar_personagem
from Personagem import consultar_personagem
from Personagem import alterar_personagem

from Relatorio import relatorio

from Inventario import mostrar_inventario
from Inventario import adicionar_item
from Inventario import remover_item
from Inventario import procurar_item
from Inventario import quantidade_itens

from Loja import mostrar_loja

from Combate import menu_combate

choose = -1


# PROCESSAMENTO

while choose != 0:

    print("--------- MENU ---------")
    print(" (1) Cadastrar Personagem\n (2) Consultar Personagem\n (3) Alterar Personagem\n (4) Ver Inventario" 
          + "\n (5) Adicionar Item\n (6) Remover Item\n (7) Procurar Item\n (8) Ver quantidade de itens\n (9) Ver Relatorio"
          + "\n (10) Loja\n (11) Combate\n (0) Sair")

    choose = int(input("Escolha: "))

    match choose:


        #PERSONAGEM

        case 1:
            cadastrar_personagem()

        case 2:
            consultar_personagem()

        case 3:
            alterar_personagem()

        #INVENTARIO
        case 4:
            mostrar_inventario()

        case 5:
            adicionar_item()

        case 6:
            remover_item()

        case 7:
            procurar_item()

        case 8:
            quantidade_itens()

        #RELATORIO

        case 9:
            relatorio(characters)


        # LOJA

        case 10:
            mostrar_loja()

        #COMBATE
        
        case 11:
            menu_combate()
        case 0:
            print("Saindo...")