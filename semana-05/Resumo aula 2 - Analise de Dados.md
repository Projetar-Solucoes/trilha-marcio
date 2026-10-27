# Resumo Prático: Análise de Dados com Pandas em Python

Este guia reúne os principais conceitos, comandos e operações fundamentais da biblioteca **Pandas**, estruturado a partir do tutorial em vídeo "Pandas para Iniciantes" da *Asimov Dados*.

---

## 1. Instalação e Importação

Para utilizar o Pandas e habilitar a leitura de planilhas do Excel, é necessário instalar as bibliotecas `pandas` e `openpyxl` via terminal:

```bash
pip install openpyxl pandas
```

No código Python, a convenção padrão para importar a biblioteca é:

```python
import pandas as pd
```

Os comandos funcionam em múltiplos ambientes de desenvolvimento, tais como **Jupyter Notebook**, **VS Code**, **PyCharm**, **Google Colab** ou diretamente no terminal.

---

## 2. Estruturas Principais de Dados

* **DataFrame**: É a estrutura central do Pandas, consistindo em uma tabela bidimensional com linhas e colunas rotuladas. Pode ser instanciado a partir de um dicionário Python:
  ```python
  dados = {'nome': ['Ana', 'Bruno', 'Carlos'], 'idade':}
  df = pd.DataFrame(dados)
  ```
* **Series**: Representa uma coluna individual de um DataFrame ou uma sequência unidimensional de dados. Pode ser criada manualmente passando uma lista:
  ```python
  s = pd.Series()
  ```

---

## 3. Leitura de Arquivos de Dados

Em cenários reais, os dados são importados diretamente de arquivos externos:

* **Planilhas Excel (`.xlsx`)**:
  ```python
  df = pd.read_excel('dados_empresa.xlsx', sheet_name='funcionarios')
  ```
* **Outros formatos suportados**: O Pandas disponibiliza funções equivalentes como `pd.read_csv()` para arquivos CSV e `pd.read_sql()` para consultas a bancos de dados.

---

## 4. Visualização e Seleção de Dados

* **Inspecionar primeiras e últimas linhas**:
  * `df.head()`: Exibe as 5 primeiras linhas do DataFrame.
  * `df.tail()`: Exibe as 5 últimas linhas do DataFrame.
* **Selecionar uma única coluna** (retorna uma *Series*):
  ```python
  df['nome']
  ```
* **Selecionar múltiplas colunas** (retorna um *DataFrame*):
  ```python
  df[['nome', 'idade']]
  ```

---

## 5. Operações Matemáticas e Criação de Colunas

É possível realizar operações vetorizadas entre colunas ou com valores escalares e atribuir o resultado a uma nova coluna:

```python
# Multiplica os salários por 12 para criar a coluna de salário anual
df['salario_anual'] = df['salario'] * 12
```

---

## 6. Filtragem de Dados (Filtros Booleanos)

A filtragem ocorre mediante a criação de **Séries Booleanas** (`True`/`False`) resultantes de comparações condicionais:

* **Filtro simples**:
  ```python
  filtro = df['idade'] > 30
  df_filtrado = df[filtro]
  ```
* **Combinação de múltiplos filtros**:
  * **Operador E (`&`)**: Seleciona linhas em que **todas** as condições sejam satisfeitas.
    ```python
    df[(df['idade'] > 30) & (df['salario'] > 5000)]
    ```
  * **Operador OU (`|`)**: Seleciona linhas em que **pelo menos uma** condição seja satisfeita.
    ```python
    df[(df['idade'] > 30) | (df['salario'] > 5000)]
    ```
  * **Inversão de condição (`~`)**: Inverte os valores lógicos (filtro NOT).
    ```python
    df[~(df['salario'] > 5000)]  # Retorna salários menores ou iguais a 5000
    ```

---

## 7. Tratamento de Dados Ausentes (`NaN`)

Valores nulos ou ausentes são representados pelo identificador `NaN`.

* **Remoção de valores nulos**:
  * `df.dropna()`: Descarta todas as linhas que contenham ao menos um valor nulo.
  * `df.dropna(subset=['idade'])`: Restringe o descarte apenas às linhas com nulo na coluna especificada.
* **Preenchimento (Imputação) de valores nulos**:
  ```python
  media_idade = df['idade'].mean()  # Calcula a média da coluna
  df['idade'] = df['idade'].fillna(media_idade)  # Preenche os nulos com a média
  ```
* **Arredondamento e conversão de tipos**:
  ```python
  df['idade'] = df['idade'].round().astype(int)
  ```

---

## 8. Ordenação e Frequência de Categorias

* **Ordenar linhas por valores de uma coluna**:
  ```python
  df.sort_values(by='salario', ascending=False)  # Ordenação decrescente
  ```
* **Contagem de frequência (`value_counts`)**:
  ```python
  df['departamento'].value_counts()  # Contagem absoluta
  df['departamento'].value_counts(normalize=True) * 100  # Proporção percentual
  ```

---

## 9. Agrupamento e Agregação (`groupby` e `agg`)

O método `groupby` divide os dados em grupos com base em colunas categóricas para cálculo de estatísticas.

* **Cálculo de média por grupo**:
  ```python
  df.groupby('departamento')['salario'].mean()
  ```
* **Outras métricas comuns**: `.sum()`, `.max()`, `.min()`, `.count()`.
* **Agrupamento por múltiplas colunas**:
  ```python
  df.groupby(['departamento', 'ativo'])['salario'].mean()
  ```
* **Múltiplas agregações personalizadas (`.agg`)**:
  ```python
  df.groupby('departamento').agg(
      idade_maxima=('idade', 'max'),
      idade_media=('idade', 'mean'),
      salario_medio=('salario', 'mean')
  )
  ```

---

## 10. Pipeline Completo em Uma Única Linha

Exemplo de encadeamento de operações para filtrar, agrupar, agregar estatísticas e ordenar o resultado em um único comando:

```python
resultado = (
    df[df['ativo']]  # 1. Filtra apenas funcionários ativos
    .groupby('departamento')  # 2. Agrupa os dados por departamento
    .agg(
        n_funcionarios=('idade', 'count'),  # Contagem de funcionários
        idade_media=('idade', 'mean'),       # Média de idade
        salario_minimo=('salario', 'min'),   # Menor salário
        salario_maximo=('salario', 'max')    # Maior salário
    )
    .sort_values(by='n_funcionarios', ascending=False)  # 3. Ordena pelo número de funcionários
)
```