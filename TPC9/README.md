# TPC9

**Data:** [29/04/2026]

## Problema

O objetivo deste trabalho foi a exploração e implementação de modelos de *Word Embeddings* utilizando a biblioteca `gensim`. O foco principal consistiu no treino e comparação de quatro variantes do algoritmo **Word2Vec** aplicadas ao texto dos dois primeiros livros da saga Harry Potter. Pretendeu-se analisar como a alteração de hiperparâmetros — especificamente a arquitetura (CBOW vs. Skip-Gram), o tamanho da janela de contexto e a dimensão dos vetores — influencia a capacidade do modelo em capturar relações semânticas e sintáticas.

## Lógica para solucionar o problema

A solução seguiu um fluxo de processamento de linguagem natural estruturado em três etapas principais:

### 1. Pré-processamento e Segmentação de Texto
Para garantir vetores de alta qualidade, o texto foi limpo e normalizado:
* Utilizámos a biblioteca **spaCy** com o modelo `pt_core_news_sm` para realizar uma segmentação de frases inteligente (`doc.sents`), evitando quebras de linha indevidas.
* Foram carregadas **14.610 frases** provenientes dos ficheiros "Harry Potter e A Pedra Filosofal.txt" e "Harry_Potter_Camara_Secreta-br.txt".
* Aplicámos filtros para converter todas as palavras para minúsculas e remover pontuação, assegurando a consistência do vocabulário.

### 2. Implementação das 4 Variantes de Word2Vec
Criámos quatro modelos com configurações distintas para observar diferentes comportamentos:
* **Modelo 1 (Base):** Utiliza a arquitetura **CBOW** (`sg=0`) com uma janela de 5 palavras e vetores de 150 dimensões.
* **Modelo 2 (Skip-Gram):** Implementa a arquitetura **Skip-Gram** (`sg=1`), focada em capturar melhor o significado de palavras raras ao prever o contexto a partir de uma palavra central.
* **Modelo 3 (Sintático):** Utiliza uma janela de contexto reduzida para **2** (`window=2`) com CBOW, forçando o modelo a aprender relações baseadas na proximidade gramatical imediata.
* **Modelo 4 (Temático/Contextual):** Aumenta a janela para **10** e os vetores para **300 dimensões** com Skip-Gram, permitindo capturar relações contextuais mais amplas e temas de cenas completas.

### 3. Avaliação e Testes de Analogia
Para validar o aprendizado de cada modelo, utilizámos as seguintes métricas:
* **Similaridade:** Verificação da proximidade entre termos (ex: "harry", "rony" e "hermione").
* **Intrusos:** Utilização do método `doesnt_match` para identificar palavras fora do contexto semântico de um grupo.
* **Analogias:** Implementação de funções personalizadas (ex: `analogy4`) para resolver equações vetoriais do tipo "Escola está para Feitiço assim como Varinha está para...".



## Conclusão e Resultados

A comparação final revelou diferenças significativas entre as configurações:
* O **Modelo 3 (Janela Curta)** foi o mais preciso na identificação de objetos, associando "vassoura" diretamente a "nimbus" e "2000".
* Os modelos **M2 e M4 (Skip-Gram)** apresentaram vizinhos focados em estados emocionais e ações, como "desesperado" ou "montar".
* O **Modelo 1 (Base)** tendeu a agrupar palavras por categorias funcionais mais genéricas (ex: "vassoura" associada a "página" ou "carta").

Este exercício demonstrou que a eficácia de um modelo de *embeddings* depende diretamente do ajuste dos seus parâmetros ao objetivo da análise (sintática ou semântica).