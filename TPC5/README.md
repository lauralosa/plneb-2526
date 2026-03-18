# TPC5

**Data:** [19/03/2026]

## Problema

O objetivo deste trabalho era extrair uma base de dados completa de doenças do portal **Atlas da Saúde**. O principal desafio residia no facto de a informação estar distribuída por dois níveis:
1. Uma **página de listagem alfabética** que continha apenas o nome e um resumo curto da doença.
2. Uma **página de detalhe específica** para cada doença, onde se encontra a descrição completa (`full_desc`).

A estrutura original da listagem não permitia obter toda a informação necessária num único pedido, exigindo uma estratégia de navegação dinâmica e extração profunda de dados.

## Lógica para solucionar o problema

A solução foi estruturada num script Python que automatiza a navegação e a recolha de dados em cascata:

* **Geração de URLs Dinâmicos:** Utilização da biblioteca `string` para iterar por todas as letras do abecedário (`a-z`), construindo os URLs de cada secção do índice (ex: `.../doencasAaZ/a`).

* **Processamento de Nível 1 (Listagem):**
    O script acede à página de cada letra e, usando o `BeautifulSoup`, identifica todos os blocos `views-row`. Daqui extrai a **designação** e a **small_desc**.

* **Processamento de Nível 2 (Deep Scraping):**
    Para cada doença encontrada, o código extrai o link relativo (`href`), reconstrói o URL absoluto e realiza um **novo pedido HTTP** para entrar na página de detalhe. É aqui que procura a `div` com a classe `field-name-body` para obter o texto integral.

* **Tratamento e Persistência de Dados:**
    Os dados são limpos com o método `.strip()` para remover espaços e quebras de linha inúteis. No final, o dicionário resultante é exportado para um ficheiro `doencasTPC.json` com indentação e suporte a caracteres especiais (UTF-8).

