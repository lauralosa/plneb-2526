# TPC10

**Data:** [06/05/2026]

## Problema

O objetivo deste trabalho foi a implementação de um modelo de **Token Classification** para a tarefa de **Reconhecimento de Entidades Mencionadas (NER)** em língua portuguesa. Utilizou-se o modelo pré-treinado **BERTimbau** (`neuralmind/bert-base-portuguese-cased`) para realizar o *fine-tuning* num dataset específico. O foco consistiu em treinar o modelo para identificar e classificar automaticamente entidades como nomes de pessoas, locais, organizações, profissões e datas em textos não estruturados.

## Lógica para solucionar o problema

A solução seguiu um fluxo de processamento de linguagem natural estruturado nas seguintes etapas:

### 1. Preparação do Dataset
* Utilizei o dataset `lfcc/portuguese_ner`, carregado via biblioteca `datasets`.
* O conjunto de dados foi dividido em **treino (3.716 frases)** e **teste (930 frases)**.
* As entidades estão anotadas com 11 etiquetas distintas (esquema BIO), abrangendo categorias como Pessoa, Local, Organização, Profissão e Data.

### 2. Tokenização e Alinhamento de Etiquetas
* O pré-processamento utilizou o tokenizer do BERTimbau, que decompõe palavras em *subwords* (WordPiece).
* Implementámos a função `align_labels_with_tokens` para garantir que as etiquetas originais fossem atribuídas apenas ao primeiro sub-token de cada palavra, marcando os restantes com `-100` para serem ignorados no treino.
* Foi aplicada a truncagem para um máximo de **512 tokens** para garantir a compatibilidade com a arquitetura do BERT.

### 3. Fine-Tuning e Configuração do Modelo
* **Modelo:** Inicializámos o `AutoModelForTokenClassification` com 11 labels e os respetivos mapeamentos `id2label` e `label2id`.
* **Treino:** O modelo foi treinado durante **2 épocas** com uma taxa de aprendizagem de `2e-5` e decaimento de peso de `0.01`.
* **Métricas:** Utilizámos a biblioteca `seqeval` para calcular métricas de Precision, Recall, F1 e Accuracy ao nível da entidade completa.

## Conclusão e Resultados

O modelo apresentou resultados de elevada precisão após as duas iterações de treino:
* **Métricas Globais:** Atingimos uma **Accuracy de 98,38%** e um **F1-Score de 95,41%** no conjunto de teste.
* **Inferência Prática:** Através de um pipeline com a estratégia `aggregation_strategy="first"`, o modelo demonstrou robustez ao identificar corretamente "Maria Teresa" como **Pessoa** (confiança de 0.95) e "Ministro da Economia" como **Profissao** (confiança de 0.77).

Este exercício demonstrou a eficácia do BERTimbau em capturar a semântica do português, permitindo criar um extrator de entidades altamente confiável com um esforço de treino reduzido.