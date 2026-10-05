#Faça um sistema que aprova o emprestimo baseado em condições e regras de negocio
'''
Regras:
1- Para pedir o emprestimo você deve ter todos os dados a seguir (Nome Completo, Idade, CPF, renda)
2- renda minima de 1500 para revisão humana de 1500-5000 automatizada, abaixo de 1500 está bloqueado
3- 1 a 20 mil automatizado, de 20.001 até 50 mil revisão humana, acima de 50 mil bloqueado
4- somente acima de 18 anos
'''

#Variaveis
nome_completo = str(input("Digite seu nome completo: "))
idade = int(input("Digite sua idade: "))

while idade < 0:
    print("Idade incorreta.")
    idade = int(input("Digite sua idade: "))

cpf = str(input("Digite seu CPF: "))
renda = int(input("Digite sua renda: R$"))
pedido_emprestimo = int(input("Quanto deseja? R$"))

#Status
bloqueado = False
revisao_humana = False

#Regras de Negocio
# Regra 1: Validação de dados obrigatórios (Nome, CPF, Renda e Pedido não podem ser vazios/zerados)
if not nome_completo or not cpf or renda <= 0 or pedido_emprestimo <= 0:
    print("\nErro: Todos os dados (Nome, CPF, Renda e Valor do Pedido) são obrigatórios.")
    bloqueado = True
#Regra 2: Idade minima possivel para o emprestimo
if idade < 18:
    bloqueado = True

#Regra 3: Analisando Renda
if renda < 1500 and not bloqueado:
    bloqueado = True
elif renda >= 1500 and renda <= 5000 and not bloqueado:
    revisao_humana = True

#Regra 4: Analisando o pedido de emprestimo
if pedido_emprestimo > 20000 and pedido_emprestimo <= 50000 and not bloqueado:
    revisao_humana = True
elif pedido_emprestimo > 50000 and not bloqueado:
    bloqueado = True

#Saída
if bloqueado:
    print("Bloqueado")
elif revisao_humana:
    print("Revisão humana")
else:
    print("Automatizado")