from datetime import datetime
import json

solicitacoes = []

##JSON

#CARREGAR
def carregar_solicitacoes():
    global solicitacoes 

    try:
        arquivo = open("solicitacoes.json", "r", encoding="utf-8")
        solicitacoes = json.load(arquivo)
        arquivo.close()

    except FileNotFoundError:
        solicitacoes = []

    except json.JSONDecodeError:
        print("Erro: O arquivo JSON está corrompido.")
        solicitacoes = []

def salvar_solicitacoes():
    arquivo = open("solicitacoes.json", "w", encoding="utf-8")
    json.dump(solicitacoes, arquivo)
    arquivo.close()


#CADASTRAR
def cadastrar_solicitacao():
    cadastrando = True

    while cadastrando:
        #Variaveis Temporarias

        #NOME
        nome = input("Digite o nome de quem faz solicitação: ").strip()

        while nome == "":
            print("Erro: O nome não pode ficar vazio.")
            nome = input("Digite o nome de quem faz solicitação: ").strip()

        #CATEGORIA
        categorias_possiveis = ["SUPORTE","FINANCEIRO","RH","ESTRUTURA","OUTROS"]

        print(f"CATEGORIAS:\n{categorias_possiveis[0]} | {categorias_possiveis[1]}\n{categorias_possiveis[2]} | {categorias_possiveis[3]}\n{categorias_possiveis[4]}")

        categoria = input("Digite a categoria: ").strip().upper()

        while categoria not in categorias_possiveis:
            print("Categoria inválida.")
            categoria = input("Digite a categoria: ").strip().upper()

        #SETOR

        setores_possiveis = ["Armazem","Finanças", "Programação", "Admnistração", "RH"]
        setor = ""

        print("(1) Armazem\n(2) Finanças\n(3) Programação\n(4) Administração\n(5) RH")
        while setor not in setores_possiveis:
            try:
                pin_setor = int(input("Digite um numero: ")) - 1

                if pin_setor < 0: raise IndexError

                setor = setores_possiveis[pin_setor]
                print(f"Setor {setor} adicionado. ")

            except IndexError:
                print("Erro: Valor Indisponivel")

            except ValueError:
                print("Erro: Valor Incorreto, Apenas Numeros")
    
        #ASSUNTO

        assunto = input("Titulo da Solicitação: ").strip()

        while assunto == "":
            print("Erro: O título não pode ficar vazio.")
            assunto = input("Titulo da Solicitação: ").strip()

        #DESCRIÇÃO
        descricao = input("Explicação Detalhada: ").strip()

        while descricao == "":
            print("Erro: A descrição não pode ficar vazia.")
            descricao = input("Explicação Detalhada: ").strip()

        #PRIORIDADE
        prioridades_possiveis = ["BAIXO", "MÉDIO", "ALTO", "URGENTE"] # PRA VERIFICAR SE A CATEGORIA ESTÁ OK
        prioridade = ""

        match categoria:
            case "SUPORTE":
                prioridade = prioridades_possiveis[0]

            case "FINANCEIRO":
                prioridade = prioridades_possiveis[3]

            case "RH":
                prioridade = prioridades_possiveis[2]

            case "ESTRUTURA":
                prioridade = prioridades_possiveis[3]

            case "OUTROS":
                prioridade = prioridades_possiveis[1]

                prioridade 
        #Criando Protocolo(ano-numero-inicial)
        ano = datetime.now().year
        numero = f"{len(solicitacoes) + 1:04d}"
        iniciais = "".join(parte[0].upper() for parte in nome.split())
        protocolo = f"{ano}-{numero}-{iniciais}"

        #Saída
        print("--------- Solicitação --------")
        print("CADASTRADA!")

        solicitacao = {"PROTOCOLO": protocolo, "NOME": nome, "SETOR": setor, "CATEGORIA": categoria, "PRIORIDADE": prioridade, "ASSUNTO": assunto, "DESCRICAO": descricao}
        solicitacoes.append(solicitacao)
        salvar_solicitacoes()

        #Saindo da Central
        exit_central = str(input("Você deseja sair? S/N ")).upper()
        if(exit_central == "S"): cadastrando = False


#CONSULTAR

def consultar_solicitacao():
    if len(solicitacoes) > 0:
        for solicitacao in solicitacoes:
            print(f"{solicitacao["PROTOCOLO"]}\n")
            
        protocolo = str(input("Digite o protocolo que deseja acessar: ")).strip()
        for solicitacao in solicitacoes:
            if protocolo == solicitacao["PROTOCOLO"]:
                 print(f"PROTOCOLO: {solicitacao["PROTOCOLO"]} \n[{solicitacao["NOME"]} do Setor {solicitacao["SETOR"]}\nCategoria: {solicitacao["CATEGORIA"]}\nNível da Prioridade: {solicitacao["PRIORIDADE"]}\n Assunto: '\033[1m{solicitacao["ASSUNTO"]}\033[0m' \nDesc: {solicitacao["DESCRICAO"]}")
            
    else: print("Sem solicitações para consulta")

#ESTATISTICA
def estatistica_solicitacao():
    print("============ ESTATÍSTICA ============")
    print(f"{len(solicitacoes)} Solicitações")
    baixo = 0
    medio = 0
    alto = 0
    urgente = 0

    armazem = 0 
    financas = 0
    programacao = 0
    adm = 0
    rh = 0
    
    for solicitacao in solicitacoes:
        match solicitacao["PRIORIDADE"]:
            case "BAIXO":
                baixo += 1

            case "MÉDIO":
                medio += 1

            case "ALTO":
                alto += 1

            case "URGENTE":
                urgente += 1   

        match solicitacao["SETOR"]:
            case "Armazem":
                armazem += 1

            case "Finanças":
                financas += 1

            case "Programação":
                programacao += 1

            case "Admnistração":
                adm += 1

            case "RH":
                rh += 1 

    print(f"Solicitações por Prioridade:\nBaixo: {baixo}\nMédio: {medio}\nAlto: {alto}\nUrgente: {urgente}")
    print(f"Solicitações por Setor:\nArmazem: {armazem}\nFinanças: {financas}\nProgramação: {programacao}\nAdministração: {adm}\nRH: {rh}")
    