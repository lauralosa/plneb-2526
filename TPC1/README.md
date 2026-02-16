# TPC1

**Data:** [18/02/2026]


## Resumo
Este trabalho prático consiste no desenvolvimento de um conjunto de funções em Python para manipulação e análise de strings.

---

## Explicação das Funções

### 1. Reverse String
**Função:** `reverse_string(s)`
* **Lógica:** A função recebe uma string e inverte a sua ordem.
* **Implementação:** Utilizei o *slicing* `[::-1]` para percorrer a string de trás para a frente e, através de um ciclo `for`, reconstruí a string invertida caractere a caractere numa nova variável.

### 2. Contar 'a' e 'A'
**Função:** `countA(s)`
* **Lógica:** Conta quantas vezes as letras "a" (minúscula) e "A" (maiúscula) aparecem numa string.
* **Implementação:** Percorri a string com um ciclo e, para cada letra, verifiquei com uma condição `if` se esta correspondia a 'a' ou 'A'. Se sim, o contador é incrementado.

### 3. Contar Vogais
**Função:** `countvowels(s)`
* **Lógica:** Calcula o número total de vogais numa palavra.
* **Implementação:** Defini uma string de referência que contemq todas as vogais (`aeiouAEIOU`). O algoritmo percorre a palavra recebida e verifica se cada letra existe nessa string de referência.

### 4. Converter para Minúsculas
**Função:** `lowercase(s)`
* **Lógica:** Transforma toda a string em letras minúsculas.
* **Implementação:** Utilizei o método nativo do Python `.lower()` para efetuar a conversão direta.

### 5. Converter para Maiúsculas
**Função:** `uppercase(s)`
* **Lógica:** Transforma toda a string em letras maiúsculas.
* **Implementação:** Utilizei o método nativo do Python `.upper()` para efetuar a conversão direta.

### 6. Verificar Capicua
**Função:** `isCapicua(s)`
* **Lógica:** Verifica se uma string é igual quando lida da esquerda para a direita e da direita para a esquerda.
* **Implementação:** Criei manualmente a inversão da string usando um ciclo `range` com passo negativo (`-1`), percorrendo os índices do último até ao primeiro. No final, comparei a string invertida construída com a original.

### 7. Strings Balanceadas
**Função:** `balancedString(s1, s2)`
* **Lógica:** Verifica se todos os caracteres presentes em `s1` também existem em `s2`.
* **Implementação:** O algoritmo percorre cada letra de `s1`. Se encontrar alguma letra que **não** esteja presente em `s2`, a função retorna imediatamente `False`. Se o ciclo terminar sem interrupções, retorna `True`.

### 8. Contar Ocorrências
**Função:** `countOcurrences(s1, s2)`
* **Lógica:** Conta quantas vezes a palavra `s1` aparece dentro do texto `s2`.
* **Implementação:** Utilizei um ciclo que percorre `s2` até onde a palavra `s1` ainda cabe (`len(s2) - len(s1)`). A cada posição, extraí um "pedaço" (*slice*) de `s2` com o mesmo tamanho de `s1` e comparei se eram iguais.

### 9. Verificar Anagrama
**Função:** `isAnagrama(s1, s2)`
* **Lógica:** Verifica se `s1` é um anagrama de `s2` (se têm exatamente as mesmas letras, apenas em ordem diferente).
* **Implementação:** Converti ambas as strings em listas de caracteres. De seguida, ordenei ambas as listas (`.sort()`). Se as listas ordenadas forem iguais, significa que as palavras são anagramas.

---

## Como executar - exemplo


Para correr o exercício 1:
```bash
python tpc1/ex1.py