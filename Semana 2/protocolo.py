'''
Normalize os textos:
remova espaços no início e no final; - feito
transforme vários espaços consecutivos em um único espaço; - feito
formate o nome com iniciais maiúsculas; - feito
transforme o e-mail em minúsculas; - feito
formate o assunto;
mantenha corretamente caracteres acentuados.
'''

from datetime import datetime
import re

#Pegando o tempo em real time
ano = datetime.now().year

#Pegando
numero = int(input("Digite o número: "))
nome = str(input("Digite seu nome completo: "))
email = str(input("Digite seu email: "))
assunto = str(input("Digite o assunto: "))
descricao = str(input("Descreva a situação: "))

#Iniciando tratamento (re.sub(padrão (nessa ocasião pega espaços extras), substituição, texto))
nome = re.sub(r"\s+", " ", nome).strip()
assunto = re.sub(r"\s+", " ", assunto).strip()
descricao = re.sub(r"\s+", " ", descricao)

#Transformando
nome = nome.title()
email = email.lower()
assunto = assunto.capitalize()
descricao = descricao.capitalize()

#Coisa nova aprendida:
iniciais = "".join(parte[0].upper() for parte in nome.split()) #Inicio um for que pega partes do texto que o split separou através dos espaços e pego a primeira letra e coloco em maiusculo. Em seguida junto tudo com join

#Saída
print("--- ATENDIMENTO REGISTRADO ---")
print(f"PROTOCOLO: {ano}-{numero:04d}-{iniciais}") #:04d serve para adicionar 4 digitos extras
print(f"Nome: {nome}")
print(f"E-mail: {email}")
print(f"Assunto: {assunto}")
print(f"Descrição: {descricao}")

#Regex, List comprehetion e ver os videos