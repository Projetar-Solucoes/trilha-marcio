from time import sleep 
#Exercício e evidência Menu com cadastrar,
 #  listar, mostrar estatísticas e sair; 
 # o programa não pode encerrar diante das entradas inválidas previstas

#variaveis
in_menu = True
pessoas_cadastradas = []

#Processo
while in_menu:
    print("(1) CADASTRAR\n(2) LISTAR\n(3) MOSTRAR ESTATISTICAS\n(4) SAIR")

    #Variavel Temporaria
    opcao = int(input("Digite a opção que deseja: "))

    match opcao:
        #Cadastro
        case 1:
            print("------- CADASTRO --------")
            nome = str(input("Digite o nome que será cadastrado: ")).strip()
    
            pessoas_cadastradas.append(nome)
            print(f"{nome} cadastrado")
            sleep(1.5)

        case 2:
            if not pessoas_cadastradas:
                print("Ninguém cadastrado")
            else:
                print("-----PESSOAS CADASTRADAS ------")
                for pessoa in pessoas_cadastradas:
                    print(f"{pessoa} está cadastrada.")
            sleep(3)

        case 3:
            #Variaveis Temporarias
            print("------- ESTATISTICAS -------")
            cont_list = 0
            pessoas_repetidas = [] #Para que a mensagem não repita

            for pessoa in pessoas_cadastradas:
                cont_list += 1
                quant_repetidas = pessoas_cadastradas.count(pessoa)
                if(quant_repetidas > 1 and pessoa not in pessoas_repetidas): 
                    print(f"{pessoa} se repete {quant_repetidas}")
                    pessoas_repetidas.append(pessoa)

            print(f"{cont_list} estão cadastradas no sistema.")
            sleep(2)

        case 4:
            #Sim, eu poderia usar o break mas usar dessa forma sinto que seria algo feio visualmente
            in_menu = False
            
print("Você saiu do programa.")