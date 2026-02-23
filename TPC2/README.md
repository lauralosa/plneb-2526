# TPC1

**Data:** [26/02/2026]


## Resumo
Este trabalho prático contém a resolução da Ficha 1 acerca de Expressões Regulares (match, search, findall, sub e split).

---

## Explicação das Funções

### 1.1 Início da linha
**Função:** `re.match(pattern, string)`
* **Lógica:** A função verifica se a palavra "hello" aparece no início exato de uma linha de texto.
* **Implementação:** Utilizei a expressão regular `r"^hello"` com o método `re.match()`. Embora este método procure por defeito no início da string, a adição do caractere `^` torna a intenção explícita no código.

### 1.2 Qualquer posição
**Função:** `re.search(pattern, string)`
* **Lógica:** A função procura a primeira ocorrência da palavra "hello" em qualquer parte da linha de texto.
* **Implementação:** Utilizei a expressão regular `r"hello"`. O método `re.search()` varre automaticamente toda a string até encontrar uma correspondência válida, ignorando a sua posição.

### 1.3 Todas as ocorrências
**Função:** `re.findall(pattern, string)`
* **Lógica:** A função pesquisa e recolhe todas as ocorrências da palavra "hello" numa string, ignorando se está escrita em maiúsculas ou minúsculas.
* **Implementação:** Utilizei a expressão regular `r"(?i)hello"`. O modificador `(?i)` indica à Regex que a pesquisa deve ser *case-insensitive*, e o `re.findall()` devolve todas as correspondências numa lista.

### 1.4 Substituição
**Função:** `re.sub(pattern, replacement, string)`
* **Lógica:** A função localiza todas as ocorrências da palavra "hello" (independentemente da capitalização) e substitui-as por uma nova string "*YEP*".
* **Implementação:** Utilizei a expressão regular `r"(?i)hello"` como padrão de pesquisa e a string `"*YEP*"` como substituto no método `re.sub()`, que altera todas as ocorrências na linha.

### 1.5 Separação por vírgulas
**Função:** `re.split(pattern, string)`
* **Lógica:** A função divide uma linha de texto em múltiplas partes utilizando a vírgula como delimitador.
* **Implementação:** Utilizei a expressão regular `r",\s*"`. O delimitador principal é a vírgula `,`, e o `\s*` serve para consumir quaisquer espaços em branco opcionais logo a seguir, garantindo que as strings resultantes não começam com espaços vazios.

### 2. Palavra Mágica
**Função:** `palavra_magica(frase)`
* **Lógica:** A função valida se uma frase termina com a expressão "por favor" seguida de um ou mais sinais de pontuação válidos.
* **Implementação:** Utilizei a expressão regular `r"por favor[.,;?!]+$"`. O grupo `[.,;?!]+` exige pelo menos um sinal de pontuação e a âncora `$` assegura que esta sequência ocorre obrigatoriamente no final absoluto da string.

### 3. Narcisismo
**Função:** `narcissismo(linha)`
* **Lógica:** A função conta a quantidade de vezes que a palavra "eu" aparece na string, garantindo que é uma palavra isolada e não parte de outra.
* **Implementação:** Utilizei `re.findall(r"\beu\b", linha, flags=re.IGNORECASE)`. Os delimitadores `\b` (*word boundaries*) asseguram que apenas a palavra exata "eu" é capturada (ignorando "pneu" ou "teu"), e apliquei a contagem com `len()` à lista devolvida.

### 4. Troca de Curso
**Função:** `troca_de_curso(linha, novo_curso)`
* **Lógica:** A função substitui todas as menções do curso "LEI" na frase pelo nome de um novo curso passado como argumento.
* **Implementação:** Utilizei `re.sub(r"LEI", novo_curso, linha)`. O padrão procura literalmente pela string "LEI" e substitui-a imediatamente pelo valor contido na variável `novo_curso`.

### 5. Soma String
**Função:** `soma_string(linha)`
* **Lógica:** A função extrai os números de uma string onde estes estão separados por vírgulas e devolve o valor da sua soma.
* **Implementação:** Utilizei `re.split(r",", linha)` para separar a string original numa lista de strings numéricas. De seguida, utilizei compreensão de listas com `int()` para as converter em inteiros e apliquei a função `sum()`.

### 6. Pronomes
**Função:** `pronomes(frase)`
* **Lógica:** A função identifica e extrai todos os pronomes pessoais que ocorram isoladamente na frase.
* **Implementação:** Utilizei `re.findall(r"\b(eu|tu|ele|ela|nós|vós|eles|elas)\b", frase, flags=re.IGNORECASE)`. O operador `|` funciona como um OR lógico, enquanto os delimitadores `\b` previnem que sequências dentro de outras palavras sejam falsamente identificadas como pronomes.

### 7. Variável Válida
**Função:** `variavel_valida(nome)`
* **Lógica:** A função verifica se uma string obedece às regras de sintaxe para o nome de uma variável (começar por letra e conter apenas letras, números ou *underscores*).
* **Implementação:** Utilizei `re.match(r"^[a-zA-Z][a-zA-Z0-9_]*$", nome)`. As âncoras `^` e `$` avaliam a string inteira. `[a-zA-Z]` força o primeiro caractere a ser uma letra e `[a-zA-Z0-9_]*` permite que os restantes sejam qualquer combinação dos caracteres permitidos.

### 8. Inteiros
**Função:** `inteiros(texto)`
* **Lógica:** A função recolhe todos os números inteiros presentes no texto, quer sejam positivos ou negativos.
* **Implementação:** Utilizei `re.findall(r"-?\d+", texto)`. O padrão `\d+` garante a extração de sequências de um ou mais dígitos, enquanto o `-?` permite capturar o sinal de menos se este existir, tornando-o opcional.

### 9. Underscores
**Função:** `underscores(texto)`
* **Lógica:** A função substitui qualquer espaço ou bloco de múltiplos espaços consecutivos por um único *underscore*.
* **Implementação:** Utilizei `re.sub(r" +", "_", texto)`. O espaço acompanhado do quantificador `+` assegura que um ou mais espaços consecutivos são tratados como um só bloco e substituídos por apenas um caractere `_`.

### 10. Códigos Postais
**Função:** `codigos_postais(lista)`
* **Lógica:** A função divide cada código postal da lista fornecida num par de números, usando o hífen como separador.
* **Implementação:** Iterei sobre a lista de códigos e apliquei `re.split(r"-", cp)`. A divisão resulta numa lista com dois elementos que, de seguida, converti explicitamente para um tuplo `tuple()` antes de adicionar à lista final de pares.