# Relatório de Implementação Técnica: Website ABE

Este documento descreve as metodologias de desenvolvimento e as escolhas técnicas aplicadas no ficheiro `tpc4.html`, focando-se na estrutura do DOM, semântica HTML5 e lógica de layout.

---

## 1. Estrutura e Semântica HTML5
O projeto foi desenvolvido seguindo as boas práticas de semântica para garantir uma árvore de documentos (DOM) organizada e acessível:
* **`nav`**: Implementação de um menu de navegação global com links de âncora interna.
* **`header`**: Definição da secção de introdução (*Hero Section*) utilizando uma hierarquia de títulos `h1` e `p`.
* **`section`**: Segmentação do conteúdo por blocos lógicos (`#sobre`, `#estilos`, `#horarios`, `#espetaculos`), facilitando a manutenção e o SEO.
* **`footer`**: Agrupamento de informações de contacto e links externos.

## 2. Engenharia de Layout e Estilização (CSS3)
A estilização foca-se na eficiência de containers e no comportamento responsivo:
* **Box Model & Reset**: Utilização do seletor universal `*` com `box-sizing: border-box` para garantir o cálculo preciso de larguras e paddings.
* **Sistemas de Grelha (Grid & Flexbox)**:
    * **CSS Grid**: Utilizado na secção de estilos para criar uma malha de 5 colunas (`grid-template-columns: repeat(5, 1fr)`) e na secção de horários para uma distribuição adaptativa (`repeat(auto-fit, minmax(200px, 1fr))`).
    * **Flexbox**: Aplicado na navegação (`display: flex`) para distribuição espacial dos elementos e no carrossel para alinhamento horizontal dos slides.
* **Posicionamento**: Uso de `position: fixed` na barra de navegação para garantir a sua permanência no topo do *viewport* durante o scroll.
* **Efeitos de Estado (`:hover`)**: Implementação de pseudo-classes para feedback visual, como a inversão de cores nos itens de estilo e a remoção do filtro `grayscale` nas imagens dos horários.

## 3. Dinamismo e Manipulação do DOM (JavaScript)
Para evitar o uso de bibliotecas pesadas, foi implementado um script nativo (Vanilla JS) para o carrossel:
* **Lógica de Translação**: O script captura o elemento `#slider` e altera a propriedade `transform: translateX` com base num índice calculado.
* **Controlo de Fluxo**: Implementação de condições `if/else` para criar um ciclo infinito, onde o slide volta ao início após atingir o limite do array de elementos.

## 4. Adaptabilidade (Responsividade)
O design responde a diferentes resoluções através de **Media Queries**:
* Foi definido um ponto de quebra em `900px` que reestrutura as grelhas complexas de múltiplas colunas para um layout de coluna única (`1fr`), garantindo a integridade da interface em dispositivos móveis.

---
**Nota técnica:** O código utiliza fontes externas via Google Fonts API e segue o padrão UTF-8 para codificação de caracteres.