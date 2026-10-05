from time import sleep
for i in range(11):
    #Letra A

    #Variaveis e Verificações com While
    codigo = int(input("Codigo do Funcionario: "))
    num_job_time = int(input("Horas trabalhadas: "))
    turno_trabalho = str(input("Turno de trabalho:\n (M) Matutino\n (V) Vespertino\n (N) Noturno: \n")).upper()

    while turno_trabalho not in ["M", "V", "N"]:
        print("\nTurno incorreto.")
        turno_trabalho = str(input("\nTurno de trabalho:\n (M) Matutino\n (V) Vespertino\n (N) Noturno:\n")).upper()

    categoria = str(input("Você é\n (O) Operario\n (G) Gerente:\n")).upper()
    while categoria not in ["O", "G"]:
        print("\nCategoria incorreta.")
        categoria = str(input("\nVocê é\n (O) Operario\n (G) Gerente:\n")).upper()

    #letra B
    salario_minimo = 450.00
    money_job_time = 0
    if categoria == "G" and turno_trabalho == "N": 
        money_job_time = salario_minimo * 0.18
    elif categoria == "G" and turno_trabalho in ["M", "V"]:
        money_job_time = salario_minimo * 0.15
    elif categoria == "O" and turno_trabalho == "N":
        money_job_time = salario_minimo * 0.13
    elif categoria == "O" and turno_trabalho in ["M", "V"]:
        money_job_time = salario_minimo * 0.10

    #Letra C
    salario_inicial = money_job_time * num_job_time

    #Letra D
    auxilio_alimentacao = 0

    if salario_inicial <= 300:
        auxilio_alimentacao = salario_inicial * 0.2
    elif salario_inicial <= 600:
        auxilio_alimentacao = salario_inicial * 0.15
    elif salario_inicial > 600:
        auxilio_alimentacao = salario_inicial * 0.05

    #Letra E
        
    print("--------- FOLHA DE PAGAMENTO ---------")
    print(f"Codigo: {codigo}\nNumero de Horas trabalhadas é de {num_job_time}H recebendo R${money_job_time}\n" +
              f"Salário inicial: R${salario_inicial} com direito a auxílio alimentação de R${auxilio_alimentacao:.2f}\n" +
                f"Recebendo no total R${salario_inicial + auxilio_alimentacao:.2f}")
    sleep(2.2)