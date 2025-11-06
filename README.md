# 🧩 Sistema de Batalha Pokémon com Max-Heap (Fila de Prioridade)

Este projeto simula batalhas entre equipes de Pokémon utilizando uma **estrutura de dados Max-Heap (fila de prioridade)** para organizar os Pokémons com base em suas **velocidades**.

---

## ⚙️ Descrição do Contexto e Critérios de Prioridade

O sistema representa uma batalha entre dois treinadores:
- O jogador escolhe **6 Pokémons** de uma lista pré-definida.
- O oponente recebe **os 6 restantes** de forma aleatória.
- Cada Pokémon possui:
  - **Nome**
  - **Velocidade** (valor numérico que define sua prioridade)

Durante a batalha:
- O Pokémon com **maior velocidade** vence o confronto contra o de menor velocidade.
- Em caso de empate, o vencedor é decidido **por sorteio**.
- O Pokémon vencedor **permanece em campo** até ser derrotado.

Após o término da batalha, todos os Pokémons que participaram (do jogador e do inimigo) são organizados dentro de uma **árvore binária Max-Heap**, onde:
- O Pokémon mais rápido fica **na raiz (topo)** da estrutura.
- Os demais são dispostos **em ordem decrescente de prioridade (velocidade)** nos níveis seguintes.

---

## 🧠 Justificativa da Estrutura Escolhida

### Por que usar uma **Fila de Prioridade (Max-Heap)** e não uma **Fila Simples (Queue)**?

Uma **fila simples** segue a regra **FIFO (First In, First Out)** — o primeiro a entrar é o primeiro a sair.  
Esse comportamento **não reflete o sistema de batalhas Pokémon**, pois a ordem de ataque depende da **velocidade**, não da ordem de escolha.

A **fila de prioridade (Max-Heap)** permite que o **Pokémon mais rápido** tenha sempre **maior prioridade**, sendo posicionado no topo da estrutura.  
Isso representa com mais precisão o funcionamento de batalhas baseadas em agilidade.

| Característica | Fila Simples | Fila de Prioridade (Max-Heap) |
|-----------------|--------------|-------------------------------|
| Ordem de atendimento | Ordem de inserção | **Maior velocidade primeiro** |
| Critério de prioridade | Nenhum | **Velocidade do Pokémon** |
| Complexidade de inserção | O(1) | **O(log n)** |
| Complexidade de acesso ao maior elemento | O(n) | **O(1)** |
| Adequado para batalhas Pokémon? | ❌ Não | ✅ Sim |

Além disso, o Max-Heap permite visualizar a **hierarquia de velocidades** de forma clara e didática, sendo uma excelente aplicação prática de estruturas de dados em um contexto lúdico.

---

## ⏱️ Análise de Complexidade das Operações

O **Max-Heap** é uma **árvore binária completa** que garante que:
- Cada nó tem valor (velocidade) **maior que o de seus filhos**.
- É geralmente implementado com **listas (arrays)** para eficiência.

As principais operações usadas no projeto são:

| Operação | Descrição | Complexidade | Explicação |
|-----------|------------|---------------|-------------|
| `insert(pokemon)` | Insere um Pokémon no heap | **O(log n)** | O Pokémon é adicionado no final e “subido” (heapify-up) até encontrar sua posição correta. |
| `build_heap(lista)` | Constrói o heap a partir de todos os Pokémons participantes | **O(n)** | Reorganiza todos os nós de forma eficiente (bottom-up). |
| `remove()` *(não usada diretamente)* | Remove o Pokémon mais rápido (raiz) | **O(log n)** | Troca o topo com o último elemento e reorganiza a árvore (heapify-down). |
| `peek()` | Consulta o Pokémon mais rápido | **O(1)** | O topo da árvore é sempre o Pokémon com maior velocidade. |

---

## 📊 Resumo Geral

| Item | Explicação |
|------|-------------|
| **Critério de prioridade** | Velocidade do Pokémon (maior valor = maior prioridade) |
| **Estrutura utilizada** | Max-Heap (fila de prioridade) |
| **Motivo da escolha** | Permite simular batalhas com base em agilidade e hierarquia |
| **Operações principais** | Inserção `O(log n)` • Construção `O(n)` • Remoção `O(log n)` • Consulta `O(1)` |
| **Representação final** | Árvore binária onde o Pokémon mais veloz ocupa o topo |

---

## 🧾 Conclusão

A implementação de uma **fila de prioridade baseada em Max-Heap** oferece uma maneira eficiente e lógica de representar batalhas Pokémon onde a **velocidade** é o fator determinante.  
Dessa forma, o sistema une **conceitos de estrutura de dados** e **dinâmica de jogos** em um exemplo prático, intuitivo e divertido.
