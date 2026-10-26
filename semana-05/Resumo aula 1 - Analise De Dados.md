# Resumo: Análise de Dados com Python

## 1. Ambiente de Desenvolvimento (Google Colab)
* O aprendizado de análise de dados em Python não exige instalação de programas no computador, sendo feito diretamente pelo **Google Colab**, uma ferramenta gratuita e online.
* O Colab executa os códigos nos servidores do Google, conecta-se ao Google Drive e requer apenas uma conta do Gmail para acesso.
* Na plataforma, o código é escrito em arquivos chamados *notebooks*, e o comando `print()` pode ser utilizado para exibir textos simples.

## 2. Importação e Leitura da Base de Dados
* O estudo analisa uma base de dados em formato `.csv` referente a clientes de um banco para entender as causas de cancelamento do serviço.
* A biblioteca **Pandas** é a ferramenta padrão do Python para manipular bases de dados com eficiência e costuma ser importada sob o apelido `pd` (`import pandas as pd`).
* A leitura do arquivo é feita através do comando `pd.read_csv('clientesbanco.csv')`, armazenando o resultado na variável `tabela`.
* Caso a execução seja feita fora do Colab, o Pandas exige instalação prévia no terminal com `pip install pandas`.
* Para exibir o conteúdo das tabelas de forma organizada e visualmente formatada, utiliza-se o comando `display(tabela)`.
* Erros de codificação (`UTF-8`) causados por acentos e caracteres especiais do português são corrigidos incluindo o parâmetro `encoding='latin1'` na função de leitura.

## 3. Tratamento de Dados (Valores Vazios)
* O tratamento dos dados é a etapa inicial de qualquer análise e consiste na **remoção de valores vazios (*NaN* ou *Not a Number*)**, pois dados ausentes prejudicam as conclusões.
* O comando `tabela = tabela.dropna()` elimina automaticamente todas as linhas com informações incompletas.
* A verificação geral das colunas e da quantidade de linhas preenchidas é realizada com `display(tabela.info())`.

## 4. Análise Descritiva Estatística
* A função `tabela.describe()` calcula métricas estatísticas gerais para as colunas numéricas, como médias, valores mínimos e máximos.
* Para limitar a quantidade de casas decimais e facilitar a leitura dos dados, encadeia-se o método `.round(1)` ao comando.

## 5. Visualização e Análise Gráfica com Plotly Express
* A biblioteca **Plotly Express** é utilizada para criar gráficos interativos e mini-dashboards, sendo importada como `px` (`import plotly.express as px`).
* Fora do Google Colab, essa biblioteca também precisa ser instalada previamente.
* A geração de um gráfico ocorre em duas etapas: definição da estrutura com `px.histogram()` e exibição com `grafico.show()`.
* No histograma, configuram-se a base de dados, a coluna do eixo X (`contatos_12_meses`) e o parâmetro `color='categoria'` para dividir visualmente clientes ativos e cancelados por cores.
* Os gráficos gerados possuem recursos interativos que permitem aplicar zoom com o mouse em áreas específicas para detalhar a investigação.
* A análise revelou que **quanto maior o número de contatos do cliente com o call center, maior é a proporção de cancelamento**.
* Clientes que realizaram 6 contatos nos últimos 12 meses atingiram **100% de taxa de cancelamento**, sinalizando um ponto crítico para ações de retenção.