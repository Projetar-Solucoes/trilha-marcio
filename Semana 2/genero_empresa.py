#variaveis
in_analyse = True
homens = 0
mulheres = 0
homens_exp = 0
homens_idosos = 0
mulher_nova_exp = 0


idade_media_homens_exp = []
media_idade = 0

idade_mulher_exp = []
menor_idade = 1000
#processamento
while in_analyse:
    idade = int(input("Digite a idade: "))
    if(idade == 0): 
        in_analyse = False
        continue
    sexo = str(input("Você é do Gênero:\n(M) Masculino\n(F) Feminino")).upper()
    while sexo not in ["M", "F"]:
        print("\nGênero inexistente\n")
        sexo = str(input("\nVocê é do Gênero:\n(M) Masculino\n(F) Feminino\n")).upper()

    exp_servico = str(input("Você tem experiência em serviço?\n(S) Sim\n(N) Não")).upper()
    while exp_servico not in ["S", "N"]:
        print("\nExperiência escrita de forma incorreta.\n")
        exp_servico = str(input("Você tem experiência em serviço?\n(S) Sim\n(N) Não")).upper()

    #Verificações de sexo
    if sexo == "M": homens += 1
    else: mulheres += 1

    #Homens com experiência em serviço
    if sexo == "M" and exp_servico == "S":
        homens_exp += 1
        idade_media_homens_exp.append(idade)

    # Homens acima de 45
    if sexo == "M" and idade > 45:
        homens_idosos += 1

    #Mulheres com menos de 21 e com experiência de trabalho
    if sexo == "F" and idade < 21 and exp_servico == "S":
        mulher_nova_exp += 1

    #Menor idade mulher com experiência
    if sexo == "F" and exp_servico == "S":
        idade_mulher_exp.append(idade)

#saída
print(f"Há {mulheres} Mulheres")

#idade homem média homem com experiência em serviço
for idade in idade_media_homens_exp:
    media_idade += idade
if len(idade_media_homens_exp) > 0: print(f"A idade média de homens com experiência em serviço é de {media_idade/ len(idade_media_homens_exp)} Anos")
else: print("Não há homens com experiência")
#Porcentagem de Homens que já tem experiência em serviço
if(homens > 0):
    print(f"Há {homens} Homens")
    print(f"{(homens_exp / homens) * 100} tem experiência em serviço")

    #Porcentagem de homens com mais de 45 anos entre o total de homens
    print(f"{(homens_idosos / homens) * 100} Tem acima de 45 anos")
else:
    print("Não existem homens")

#Mulheres novas com experiência em serviço
print(f"{mulher_nova_exp} Mulheres novas tem experiência em serviço")

#A menor idade entre as mulheres com experiência
if idade_mulher_exp:
    for idade in idade_mulher_exp:
     if(idade < menor_idade): menor_idade = idade
    print(f"A menor idade entre as mulheres com experiência é de: {menor_idade}")
else:
    print("Não há mulheres com experiência. ")