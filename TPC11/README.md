# TPC11

**Data:** [20/05/2026]

## Problema

O objetivo deste trabalho foi a implementação de um sistema base de **Recuperação de Informação (IR)** focado no **Modelo de Espaço Vetorial**. O foco consistiu em construir um motor de busca simples, recorrendo ao algoritmo **TF-IDF** para a pesagem de termos e à **Similaridade do Cosseno** para classificar, ordenar e fazer o *ranking* de uma coleção de documentos textuais com base numa *query* de pesquisa.

## Lógica para solucionar o problema

A solução seguiu um fluxo de processamento de linguagem natural e álgebra linear estruturado nas seguintes etapas:

### 1. Pré-Processamento do Texto
* Utilizou-se a biblioteca `spaCy` com o modelo `en_core_web_sm` para processar a coleção de documentos e as pesquisas.
* O texto foi convertido para minúsculas (*lowercasing*) e os tokens foram extraídos de forma limpa.
* Foi feita a remoção de *stop words* e sinais de pontuação através dos atributos `.is_stop` e `.is_punct` do `spaCy`, garantindo que apenas as palavras com relevância semântica fossem mantidas.

### 2. Construção da Matriz TF-IDF
* **Term Frequency (TF):** Implementou-se a função `tf(doc)` para calcular a frequência relativa de cada termo num documento, dividindo a contagem absoluta do termo pelo total de palavras do documento.
* **Inverse Document Frequency (IDF):** Através da função `idf(collection)`, isolou-se o vocabulário global único e aplicou-se a fórmula logarítmica com base 10, utilizando a expressão `math.log(N/DF)`. Isto permitiu penalizar termos demasiado comuns e valorizar termos raros.
* **Matriz Global:** A função `tf_idf(collection)` cruzou as métricas anteriores para gerar uma matriz de pesos (lista de vetores), ordenada alfabeticamente pelo vocabulário global.

### 3. Processamento da Query e Cálculo do Ranking
* **Vetorização da Query:** A função `processar_query` limpa a string da pesquisa (neste caso, `"The bright sun"` passa a `['bright', 'sun']`), calcula o seu TF e projeta-o no mesmo espaço dimensional do vocabulário do corpus utilizando o IDF previamente guardado.
* **Similaridade do Cosseno:** Criou-se a função `calcular_cosseno` para calcular o produto interno (*dot product*) entre o vetor da *query* e o vetor de cada documento, dividindo-o pelo produto das suas magnitudes através de `math.sqrt()`.
* **Ordenação:** Os resultados foram ordenados de forma decrescente com `.sort(key=lambda x: x[1], reverse=True)` para devolver um *ranking* estruturado em formato de lista de tuplos.

## Conclusão e Resultados

O sistema demonstrou total eficácia na associação semântica e na ordenação dos documentos em ambiente de teste:
* **Coleção Base:** O algoritmo foi testado com um corpus de 3 documentos focados em elementos como *"sky"*, *"sun"*, *"blue"* e *"bright"*.
* **Inferência Prática:** Perante a query *"The bright sun"*, o motor de busca foi capaz de isolar os termos relevantes, calcular os vetores e gerar o *ranking* final ordenado automaticamente (apresentando os documentos associados a "D1", "D2", "D3" e as respetivas pontuações de similaridade).

Este exercício demonstrou a utilidade prática do modelo vetorial para a recuperação de informação estruturada, permitindo criar um classificador de relevância textual robusto a partir de conceitos algébricos base.