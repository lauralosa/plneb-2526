# TPC7

**Data:** [09/04/2026]

## Problema

O objetivo deste trabalho era desenvolver uma aplicação web interativa para a consulta de um Dicionário Médico. A aplicação deveria fornecer uma interface gráfica amigável para utilizadores humanos consultarem termos e definições, bem como um endpoint de API para disponibilizar os dados brutos a sistemas automatizados. Todo o design deveria ser suportado pelo framework Bootstrap para garantir responsividade e uma estética profissional.

## Lógica para solucionar o problema

A solução baseia-se nos seguintes passos técnicos:

### 1. Carregamento de Dados (JSON)
A base de dados é originária de um ficheiro local (`dicionario_medico.json`).
* Utilizamos o módulo `json` do Python para carregar o conteúdo do ficheiro para um dicionário em memória logo no arranque do servidor.

### 2. Criação do Servidor Web com Flask
Utilizamos a micro-framework `Flask` para criar o backend da aplicação e gerir as diferentes rotas (URLs):
* **`/`**: Rota principal que devolve a Homepage.
* **`/conceitos`**: Rota que devolve a lista completa de todos os termos médicos disponíveis (extraídos com `db.keys()`).
* **`/conceitos/<designacao>`**: Rota dinâmica que recebe o nome do conceito no próprio URL, pesquisa no dicionário e devolve a página com a respetiva definição.
* **`/api/conceitos`**: Rota orientada a máquinas que devolve o dicionário Python diretamente no formato JSON.

### 3. Sistema de Templates (Jinja2)
Para evitar a repetição de código HTML, utilizamos a herança de templates do motor Jinja2 (integrado no Flask):
* Criámos um ficheiro **`layout.html`** que funciona como o esqueleto do site e importa automaticamente o Bootstrap 5 para todas as páginas.
* As restantes páginas (`home.html`, `conceitos.html`, `conceito.html`) utilizam a sintaxe `{% extends 'layout.html' %}` para herdar essa estrutura.
* Injeção de dados: Utilizamos blocos lógicos como `{% for conceito in conceitos %}` para gerar as listas HTML dinamicamente e `{{ designacao }}` para imprimir o texto das variáveis de Python no ecrã.

### 4. Interface Dinâmica e Responsiva (Bootstrap 5)
A estética da aplicação foi construída com recurso a classes do Bootstrap 5, sem necessidade de escrever ficheiros CSS personalizados:
* Utilização de **Grids** (`row`, `col-md-8`) e **Containers** para centrar e organizar o conteúdo.
* Utilização de **Cards** para destacar as definições dos conceitos e a navegação da homepage.
* Utilização de componentes interativos como **List Groups** (`list-group-item-action`) para criar a lista de conceitos clicáveis.

### 5. Tratamento de Erros de Navegação
Foi implementada uma lógica de validação na rota individual dos conceitos:
* Se o utilizador pesquisar por uma `<designacao>` que exista no dicionário, a página `conceito.html` é renderizada.
* Se o conceito não existir, a aplicação captura essa falha através de uma condição `else` e renderiza um template **`erro.html`**. Esta página apresenta uma mensagem visualmente destacada (usando `alert-danger` do Bootstrap) e fornece botões para redirecionar o utilizador em segurança de volta para a lista.