# *Tipos de Aprendizado de Máquina*



&#x09;Para entendermos cada tipo de aprendizado de máquina, precisamos inicialmente compreender o que é Machine Learning.

&#x09;Machine Learning é a área que estuda como Inteligências Artificiais e os computadores podem identificar padrões através de dados, podendo ser útil para várias ocasiões.

&#x09;Exemplo: Identificar se um e-mail é spam, se um animal em um captcha é realmente um animal ou se um caminho a seguir é o melhor para um NPC. Mas quais os tipos de aprendizado de máquina?



## **Aprendizado Supervisionado**



&#x09;Para entender, precisamos saber dois conceitos básicos

&#x09;Características (features): As informações que farão o modelo prever.

&#x09;Rótulo (label ou alvo): A resposta que o modelo deve aprender a prever.

&#x09;No Aprendizado Supervisionado, você deve repassar as informações que devem ser previstas já com respostas, ensinando o modelo diretamente a reagir às features e chegar à label. Alguns exemplos são: 



1. **Identificar o rosto de um humano**
Features: Os olhos, a boca, o nariz e as orelhas. Podem ser formas de identificar. Podemos mandar várias informações já com as respostas facilitando o trabalho do modelo (Labels: Rosto humano e Rosto não humano)

2. **Detectar fraudes bancárias**
Features: Valor, horário e características detalhadas da transação facilitando a análise dos dados e diminuindo o tempo para reconhecer um possível problema

&#x09;Em ambos vemos um exemplo de **Classificação**

&#x09;**Classificação** acontece quando queremos prever por uma categoria ou classe, nós dois casos a resposta ou seria A ou B.

&#x09;Temos também a **Regressão**, que acontece quando queremos prever um valor numérico. Podemos usar por exemplo:



**3. Preço de uma casa**
Features: Tamanho, quantidade de cada cômodo na casa e se vem mobiliada ou não. Diante de tudo isso e com base nos valores seria possível calcular o preço da casa.


**4. Vendas esperadas no próximo mês**

&#x20;   O modelo aprende com base em dados históricos de vendas de uma empresa, pegando informações de vários meses distintos e se baseando nelas.

&#x20;   Features: Vendas anteriores, época do ano e campanhas.



## **Aprendizado Não Supervisionado**



&#x09;Esse tipo de aprendizado não fornece ao modelo a resposta correta que ele deve aprender a prever.

&#x09;Ele é útil quando não sabemos as respostas que devem ser retornadas. Um exemplo de situações distintas usando o aprendizado supervisionado e o não supervisionado seria uma loja querendo prever o cancelamento de um pedido, sabendo o perfil dos clientes, e outra querendo descobrir o padrão de consumo do cliente com base na semelhança e no agrupamento de dados.

&#x09;Exemplos:

1. **Padrões de compra**

&#x09;O modelo analisa milhares de compras e identifica produtos que costumam ser comprados juntos. Isso ajudaria a descobrir padrões de consumo para organizar produtos e planejar promoções.



**2. Organizar notícias por assunto**

&#x09;O modelo analisa textos e agrupa notícias com conteúdo semelhante. Assim, seria possível encontrar grupos de notícias sobre temas como esportes, tecnologia e política sem receber essas categorias como respostas de treinamento.



**3. Identificar comportamentos incomuns em Bancos**

&#x09;O modelo procura transações que diferem bastante dos padrões habituais. Assim, seria possível sinalizar operações que merecem investigação.



**4. Perfis de jogadores**

&#x09;O modelo analisa comportamentos como tempo de jogo, exploração e frequência de combate, com o objetivo de encontrar grupos de jogadores com estilos semelhantes.



## **Supervisionado x Não Supervisionado**



&#x09;Como saber diferenciar cada um?

&#x09;Se recebe exemplos com respostas conhecidas para prever resultados, é aprendizado supervisionado.

&#x09;Se procura grupos, semelhanças ou estruturas sem rótulos fornecidos, é aprendizado não supervisionado.

