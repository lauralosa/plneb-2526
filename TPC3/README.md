# TPC3

**Data:** [05/03/2026]

## Problema

O texto original do dicionário apresenta quebras de página representadas pelo caracter *form feed* (`\f`). No formato original, a presença deste caracter impedia que as palavras situadas no início de cada página fossem reconhecidas como conceitos, pois a estrutura habitual de separação por duplas quebras de linha (`\n\n`) estava corrompida nessas zonas.

## Lógica para solucionar o problema


O processo de limpeza e extração foi feito recorrendo a Expressões Regulares (`re`). O algoritmo segue os seguintes passos lógicos:

1. **Leitura do Ficheiro:** O texto é carregado usando a codificação `utf8`.
2. **Remoção de Quebras de Página:**  Os caracteres `\f` (Form Feed) são removidos do texto para evitar desconfigurações nas páginas. 
3. **Marcação de Parágrafos:** Todos os duplos parágrafos (`\n\n`) são temporariamente marcados com uma arroba (`@`). Isto ajuda a identificar as separações principais no texto.
4. **Identificação de Conceitos:** Procura-se por padrões onde uma quebra de linha seguida de `@` antecede uma letra maiúscula (incluindo acentuadas). Estes casos representam geralmente o início de um novo conceito médico e são marcados com um cardinal (`#`).
5. **Reestruturação e Limpeza:** - Substitui-se o marcador de novo conceito (`\n\n#`) por uma quebra de linha simples (`\n`), ajustando o espaçamento.
    - Removem-se as restantes arrobas (`@`) que serviam apenas de marcação temporária.
6. **Extração:** O texto final limpo é dividido (`re.split`) pelas quebras de linha duplas (`\n\n`), gerando uma lista onde cada elemento corresponde a um conceito médico e à sua definição.