import pandas as pd

df = pd.read_csv("https://raw.githubusercontent.com/Projetar-Solucoes/materiais-trilha/main/semana-04/solicitacoes_semana4.csv")

#colunas e linha
print(f"Colunas e Linhas: {df.shape}")

#Quantas linhas repetidas
print(f"Quantas linhas repetidas?: {df.duplicated().sum()}")

#Quantos valores vazios tem a coluna prioridade
print(f"Quantos valores vazios tem a coluna prioridade?: {df["prioridade"].isna().sum()}")

#Quantos valores diferentes aparecem na coluna (sem arrumar nada)
print(f"Quantos valores diferentes em categoria?: {df["categoria"].nunique()}")