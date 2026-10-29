import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("semana-05/Atividade 1/eleicao_ficticia.csv")

# ATIVIDADE 1
print("-------------------- ATIVIDADE 1 --------------------")

#Dimensão da base
print("--- DIMENSÂO DA BASE: ---\n")
print(f"Linhas e colunas: {df.shape}")
print(f"Quantidade de linhas: {df.shape[0]}")
print(f"QUantidade de colunas: {df.shape[1]}")

#Tipos das colunas
print("\n TIPOS DAS COLUNAS\n")
print(df.info())

# Primeiras cinco linhas
print("\nPRIMEIRAS CINCO LINHAS\n")
print(df.head())

# Quantas seções e quantos bairros existem?
print("\nQUANTIDADE DE SEÇÕES E BAIRROS\n")
print(f"Quantidade de seções: {df['secao'].nunique()}")
print(f"Quantidade de bairros: {df['bairro'].nunique()}")

#Explicação - Seção funciona como identificador: A serie Coluna tem números, mas esses números não são a quantidade e sim pra diferenciar uma seção eleitoral de outra.
print("--------------------------------------------")




#ATIVIDADE 2
print("-------------------- ATIVIDADE 2 --------------------")

#Valores ausentes por coluna
print("\nVALOR AUSENTES POR COLUNA\n")
print(df.isna().sum())

# Linhas duplicadas
print("\nQUANTIDADE DE LINHAS DUPLICADAS\n")
print(df.duplicated().sum())

#Verificar se a seção é única
print("\nA COLUNA SECAO É UNICA?\n")
print(df["secao"].is_unique)

#Identificar todas as linhas com seções repetidas ( Daqui pra frente tive uma ajuda grande de algumas IAs, e aprendi outros métodos tbm)
secao_repetida = df["secao"].duplicated(keep=False) 

#Identificar as colunas que representam contagem (Fora seção)
colunas_contagem = [coluna for coluna in df.select_dtypes(include="number").columns if coluna != "secao"]

#Verificar contagens negativas ou não inteiras
contagem_invalida = pd.Series(False, index= df.index)

for coluna in colunas_contagem:
    valores = df[coluna]

    contagem_invalida |= ((valores < 0) | (valores % 1 != 0) & valores.notna()) # DUVIDA, COMO O PYTHON PERCORRE OS VALORES?

# Verificar se as abstenções superam os eleitores aptos
abstencoes_invalidas = (df["abstencoes"] > df["eleitores_aptos"])

# Juntar todas as regras em um único filtro
problemas = (df.isna().any(axis = 1) | df.duplicated(keep = False) | secao_repetida | contagem_invalida | abstencoes_invalidas)

# Mostrar somente os registros com problemas

print("\nREGISTROS QUE VIOLAM AS REGRAS\n")
print(df.loc[problemas])
print("--------------------------------------------")




#ATIVIDADE 3
print("-------------------- ATIVIDADE 3 --------------------")
# Calcular o comparecimento
df["comparecimento"] = df["eleitores_aptos"] - df["abstencoes"]

# Calcular os votos válidos
df["votos_validos"] = (df["votos_ana"] +df["votos_bruno"] +df["votos_carla"])

# Conferir se os números fecham em cada seção
df["conferencia"] = (df["comparecimento"] == df["votos_validos"] + df["votos_brancos"] + df["votos_nulos"])

print("\nCONFERÊNCIA POR SEÇÃO")
print(df[["secao","comparecimento","votos_validos","votos_brancos","votos_nulos","conferencia"]])

# Mostrar o resultado explícito da conferência
print("\nRESULTADO DA CONFERÊNCIA")
print("Todas as seções estão corretas?", df["conferencia"].all())

# Calcular os totais
print("\nTOTAIS DA ELEIÇÃO")
print("Total de eleitores aptos:", df["eleitores_aptos"].sum())
print("Total de abstenções:", df["abstencoes"].sum())
print("Total de comparecimento:", df["comparecimento"].sum())
print("Total de votos válidos:", df["votos_validos"].sum())

print("--------------------------------------------")




# ATIVIDADE 4
print("-------------------- ATIVIDADE 4 --------------------")

# Verificar se os eleitores aptos são maiores que zero
denominador_valido = df["eleitores_aptos"] > 0

# Calcular a taxa de abstenção
df["taxa_abstencao"] = (100 * df["abstencoes"] / df["eleitores_aptos"]).where(denominador_valido)

# Calcular a taxa de comparecimento
df["taxa_comparecimento"] = (100 * df["comparecimento"] / df["eleitores_aptos"]).where(denominador_valido)

# Calcular o percentual de votos brancos e nulos sobre o comparecimento
denominador_comparecimento = df["comparecimento"] > 0

df["taxa_brancos_nulos"] = (100 * (df["votos_brancos"] + df["votos_nulos"])/ df["comparecimento"]).where(denominador_comparecimento)

# Mostrar as taxas calculadas
print("\nTAXAS POR SEÇÃO")
print(df[["secao", "taxa_abstencao", "taxa_comparecimento", "taxa_brancos_nulos"]].round(2))

# Listar as três seções com maior taxa de abstenção
print("\n3 SEÇÕES COM MAIOR TAXA DE ABSTENÇÃO")

maiores_abstencoes = df.sort_values(
    by="taxa_abstencao",
    ascending=False
).head(3)

print(
    maiores_abstencoes[
        ["secao", "bairro", "eleitores_aptos", "taxa_abstencao"]
    ].round(2)
)

print("--------------------------------------------")




# ATIVIDADE 5
print("-------------------- ATIVIDADE 5 --------------------") # NÃO ENTENDI OQ É QUANTIL e o desvio padrão, nem pesquisando sobre. Muito confuso. ~ perguntar para o Hyan depois

# Colunas que serão analisadas
colunas = ["eleitores_aptos", "taxa_abstencao"]

# Calcular as estatísticas de cada coluna
for coluna in colunas:
    dados = df[coluna]

    quartis = dados.quantile([0.25, 0.75])
    q1 = quartis.loc[0.25]
    q3 = quartis.loc[0.75]

    print(f"\nESTATÍSTICAS DE {coluna.upper()}")
    print("Média:", round(dados.mean(), 2))
    print("Mediana:", round(dados.median(), 2))
    print("Mínimo:", round(dados.min(), 2))
    print("Máximo:", round(dados.max(), 2))
    print("Amplitude:", round(dados.max() - dados.min(), 2))
    print("Primeiro quartil (Q1):", round(q1, 2))
    print("Terceiro quartil (Q3):", round(q3, 2))
    print("Intervalo interquartil (Q3 - Q1):", round(q3 - q1, 2))

# Desvio padrão populacional das taxas de abstenção
desvio_padrao = df["taxa_abstencao"].std(ddof=0)

print("\nDESVIO PADRÃO POPULACIONAL DA TAXA DE ABSTENÇÃO")
print(round(desvio_padrao, 2), "pontos percentuais")

# Comparação entre média e mediana da taxa de abstenção
media = df["taxa_abstencao"].mean()
mediana = df["taxa_abstencao"].median()

print("\nCOMPARAÇÃO ENTRE MÉDIA E MEDIANA")
print(f"A média da taxa de abstenção é {media:.2f}%, enquanto a mediana é {mediana:.2f}%. \n")

if media > mediana:
    print("Como a média é maior que a mediana, algumas taxas mais altas podem estar elevando a média.")
elif media < mediana:
    print("Como a média é menor que a mediana, algumas taxas mais baixas podem estar reduzindo a média.")
else:
    print("Como a média e a mediana são iguais, ambas indicam o mesmo valor central.")

print("--------------------------------------------")





# ATIVIDADE 6
print("-------------------- ATIVIDADE 6 --------------------")

# (A) Média simples das taxas de abstenção das 24 seções
media_simples = df["taxa_abstencao"].mean()

# (B) Taxa global de abstenção do município
taxa_global = (
    100 * df["abstencoes"].sum()
    / df["eleitores_aptos"].sum()
)

# Diferença em pontos percentuais
diferenca = abs(media_simples - taxa_global)

# Mostrar os resultados
print("\nCOMPARAÇÃO DAS TAXAS DE ABSTENÇÃO")
print(f"Média simples: {media_simples:.2f}%")
print(f"Taxa global: {taxa_global:.2f}%")
print(f"Diferença: {diferenca:.2f} pontos percentuais")

print("--------------------------------------------")






# ATIVIDADE 7
print("-------------------- ATIVIDADE 7 --------------------")

# Agrupar por bairro e somar os valores de cada seção
bairros = df.groupby("bairro")[["eleitores_aptos", "abstencoes", "comparecimento", "votos_validos"]].sum()

# Calcular a taxa de abstenção de cada bairro a partir dos totais
bairros["taxa_abstencao"] = (100 * bairros["abstencoes"] / bairros["eleitores_aptos"]).where(bairros["eleitores_aptos"] > 0)

# Ordenar os bairros pela taxa de abstenção, da maior para a menor
bairros = bairros.sort_values(by="taxa_abstencao", ascending=False)

# Mostrar os resultados
print("\nTOTAIS E TAXAS POR BAIRRO")
print(bairros.round(2))

# Identificar o bairro com a maior taxa de abstenção
maior_taxa = bairros["taxa_abstencao"].idxmax()
print("\nBairro com a maior taxa de abstenção:", maior_taxa)
print("Taxa de abstenção:", round(bairros.loc[maior_taxa, "taxa_abstencao"], 2), "%")

# Identificar o bairro com a maior quantidade de abstenções
maior_quantidade = bairros["abstencoes"].idxmax()
print("\nBairro com a maior quantidade de abstenções:", maior_quantidade)
print("Quantidade de abstenções:", bairros.loc[maior_quantidade, "abstencoes"])

# Verificar se é o mesmo bairro
print("\nÉ o mesmo bairro?", maior_taxa == maior_quantidade)
print("--------------------------------------------")




# ATIVIDADE 8
print("-------------------- ATIVIDADE 8 --------------------")

# Selecionar apenas os votos das três candidaturas
colunas_votos = ["votos_ana", "votos_bruno", "votos_carla"]

# Somar os votos de cada candidatura no município
votos_municipio = df[colunas_votos].sum()

# Calcular o total de votos válidos
total_validos = votos_municipio.sum()

# Calcular a participação de cada candidatura nos votos válidos
participacao = 100 * votos_municipio / total_validos

# Juntar os totais e os percentuais em uma tabela
resultado = votos_municipio.to_frame(name="votos")
resultado["participacao (%)"] = participacao

print("\nRESULTADO GERAL DO MUNICÍPIO")
print(resultado.round(2))

# Identificar a candidatura mais votada
ordenado = votos_municipio.sort_values(ascending=False)

mais_votada = ordenado.index[0]
segunda = ordenado.index[1]

diferenca_votos = ordenado.iloc[0] - ordenado.iloc[1]
diferenca_percentual = participacao[mais_votada] - participacao[segunda]

print("\nCANDIDATURA MAIS VOTADA")
print("Candidatura:", mais_votada)
print("Votos:", ordenado.iloc[0])
print("Diferença para a segunda colocada em votos:", diferenca_votos)
print("Diferença em pontos percentuais:", round(diferenca_percentual, 2))

# Somar os votos por bairro
votos_bairro = df.groupby("bairro")[colunas_votos].sum()

print("\nCANDIDATURA MAIS VOTADA POR BAIRRO")

for bairro, linha in votos_bairro.iterrows():
    maior_voto = linha.max()
    vencedoras = linha[linha == maior_voto].index.tolist()

    if len(vencedoras) > 1:
        print(f"{bairro}: EMPATE entre {', '.join(vencedoras)} ({maior_voto} votos)")
    else:
        print(f"{bairro}: {vencedoras[0]} ({maior_voto} votos)")
print("--------------------------------------------")





# ATIVIDADE 9
print("-------------------- ATIVIDADE 9 --------------------")

input("Ver graficos (Pressione enter): ")

# Taxa de abstenção por bairro
(df.groupby("bairro")["taxa_abstencao"].mean()).plot.bar()

plt.title("Abstenção por bairro")
plt.xlabel("Bairro")
plt.ylabel("Taxa de abstenção (%)")
plt.ylim(bottom=0)
plt.savefig("bairros.png", dpi=150, bbox_inches="tight")
plt.show()


# Histograma da taxa de abstenção
plt.hist(df["taxa_abstencao"].dropna(), bins=6)

plt.title("Abstenção nas seções")
plt.xlabel("Taxa de abstenção (%)")
plt.ylabel("Número de seções")
plt.savefig("histograma.png", dpi=150, bbox_inches="tight")
plt.show()


# Dispersão
plt.scatter(df["eleitores_aptos"], df["taxa_abstencao"])

plt.title("Eleitores aptos e abstenção")
plt.xlabel("Eleitores aptos (pessoas)")
plt.ylabel("Taxa de abstenção (%)")
plt.savefig("dispersao.png", dpi=150, bbox_inches="tight")
plt.show()


# CONCLUSÃO

#A taxa global de abstenção do município fictício foi de 18,59%, 
# correspondendo a 1.988 abstenções entre 10.695 eleitores aptos. 
# A candidatura de Ana foi a mais votada, com 3.146 votos, representando 40,12% dos votos válidos. 
# Entre os bairros, Lagoa apresentou a maior taxa de abstenção, com 19,38%, 
# enquanto Jardim apresentou a menor, com 17,81%. 
# Essa diferença mostra que as taxas de abstenção variaram entre os bairros analisados.
# Uma limitação da base é que ela reúne dados por seção e bairro, sem informações individuais dos eleitores. 
# Por isso, não é possível identificar quais pessoas votaram em cada candidatura nem determinar as causas da abstenção apenas com esses dados. 
# Como a eleição e os dados são fictícios, os resultados não devem ser generalizados para eleições reais.

#nota do aluno e minhas duvidas:
# .quantile()
# std(ddof=0) - o desvio padrão
