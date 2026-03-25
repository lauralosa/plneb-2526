# TPC6

**Data:** [26/03/2026]

## Problema

O objetivo deste trabalho era processar o texto do livro "Harry Potter e A Pedra Filosofal" para identificar relações de coocorrência entre personagens. A lógica baseia-se na premissa de que, se duas personagens são mencionadas na mesma frase, existe uma relação ou interação entre elas.

## Lógica para solucionar o problema

A solução baseia-se nos seguintes passos técnicos:

### 1. Processamento com spaCy
Utilizamos a biblioteca `spaCy` com o modelo **`pt_core_news_lg`** (Large). 
* O modelo "Large" é essencial aqui porque possui vetores de palavras mais ricos, permitindo uma maior precisão no **Reconhecimento de Entidades Nomeadas (NER)**, evitando que nomes de personagens sejam confundidos com palavras comuns.

### 2. Segmentação de Frases
O texto é dividido em frases individuais através da propriedade `.sents`. 
* Esta é a nossa unidade de medida: **Frase = Contexto de Interação**.

### 3. Extração e Filtragem de Entidades
Para cada frase:
1. Identificamos todas as entidades nomeadas (`.ents`).
2. Filtramos apenas aquelas que o spaCy classifica como **`PER`** (Pessoas/Personagens).
3. Eliminamos duplicados dentro da mesma frase (ex: se o nome "Harry" aparecer três vezes na mesma frase, ele só conta como uma instância para as relações dessa frase).

### 4. Construção da Rede de Adjacência
Se uma frase contiver **duas ou mais personagens**, o algoritmo cria um "par" entre todas elas:
* Utilizamos um **dicionário de dicionários** (`amigos = {}`) para armazenar os pesos.
* **Lógica do Contador:**
    * Se a relação `Personagem A -> Personagem B` é nova, iniciamos o contador a 1.
    * Se já existia uma interação anterior, incrementamos o valor (`+1`).