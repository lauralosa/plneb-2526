# TPC8

**Data:** [16/04/2026]

## Problema

O objetivo deste trabalho foi expandir a aplicação do Dicionário Médico desenvolvida na aula anterior, focando-se na implementação de um motor de pesquisa interna. A aplicação deveria permitir que o utilizador localizasse termos ou descrições específicas através de uma interface dedicada, oferecendo filtros avançados como a distinção entre maiúsculas/minúsculas (*Case Sensitive*) e a procura por termos exatos (*Word Boundary*). Adicionalmente, era necessário destacar visualmente o termo pesquisado nos resultados apresentados.

## Lógica para solucionar o problema

A solução baseia-se nos seguintes passos técnicos:

### 1. Centralização da Navegação (Layout Global)
Para melhorar a experiência do utilizador e a manutenção do código, procedeu-se à refatoração do sistema de templates:
* A barra de navegação (**Navbar**) foi movida para o ficheiro `layout.html`, tornando-a global e acessível em todas as páginas do site sem necessidade de repetição de código em cada template.
* O menu passou a incluir um link direto para a nova funcionalidade de **Pesquisa**.

### 2. Rota de Pesquisa no Backend (Flask e Argumentos GET)
Ao contrário das rotas de inserção de dados, a pesquisa foi implementada utilizando o método **GET**, o que permite que os parâmetros da busca fiquem registados no URL:
* Criámos a rota `/pesquisar` no ficheiro `aula8.py` que utiliza `request.args.get()` para capturar o texto da pesquisa (`query`) e o estado dos interruptores de filtragem (*switches*).

### 3. Implementação dos Filtros de Pesquisa
A lógica de filtragem foi construída no Python para garantir precisão nos resultados:
* **Case Sensitive**: Se o filtro estiver desativado, tanto a `query` como os textos do dicionário são convertidos para minúsculas através do método `.lower()` antes da comparação.
* **Palavra Exata (Word Boundary)**: Para evitar correspondências parciais indesejadas, implementámos uma lógica que limpa a pontuação básica e utiliza o método `.split()` para verificar a existência da palavra isolada dentro das descrições ou designações.

### 4. Destaque Visual e Segurança (Filtro Safe)
Para facilitar a identificação dos resultados, a aplicação destaca o termo pesquisado no texto:
* Utilizamos o método `.replace()` no backend para envolver a string pesquisada em tags HTML de negrito (`<b>`).
* No template `pesquisar.html`, os resultados são renderizados utilizando o filtro **`| safe`** do Jinja2. Este passo é fundamental para que o Flask interprete as tags de negrito como código HTML e não como texto simples.

### 5. Atualização da Interface (Bootstrap 5)
A estética da aplicação foi atualizada para integrar as novas funcionalidades de forma coesa:
* A página inicial (`home.html`) foi simplificada, removendo a navbar local e adicionando cartões e botões de acesso rápido à pesquisa.
* Foram utilizados componentes **Form Switches** do Bootstrap na página de pesquisa para uma seleção intuitiva dos filtros.
* Os resultados são apresentados numa tabela organizada, permitindo a navegação direta para a página individual de cada conceito.