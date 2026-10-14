from central import cadastrar_solicitacao
from central import consultar_solicitacao
from central import estatistica_solicitacao
from central import carregar_solicitacoes

#FUNÇÃO PARA INICIAR SOLICITACOES:
carregar_solicitacoes()

#Variaveis
choose = -1

#Central
while choose != 0:
    print("--------------- CENTRAL ---------------")
    print("(1) Cadastrar Solicitação\n(2) Consultar solicitação\n(3) Estatísticas\n(0) Fechar")
    
    try:
        choose = int(input("Escolha uma das opções: "))

    except ValueError:
        print("Erro: Digite apenas números.")
        continue

    match choose:
        case 1:
            cadastrar_solicitacao()

        case 2:
            consultar_solicitacao()

        case 3:
            estatistica_solicitacao()

        case 0:
            print("Fechando Central..")

print("Central fechada.")