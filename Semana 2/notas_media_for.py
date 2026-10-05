#variavel
soma = 0

for i in range(1, 6):
    soma += int(input("Digite uma nota: "))
print(f"A média das notas é {soma/i}")