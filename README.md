# Labirinto - Projeto de Busca em Labirinto

Este projeto implementa um jogo de labirinto onde o Pacman deve encontrar o caminho da entrada até a saída usando algoritmos de busca em largura (BFS) e profundidade (DFS).
![execução do jogo](images/image.png)

## Estrutura do Projeto

O projeto é composto pelos seguintes arquivos principais:

- `main.py`: Arquivo principal que inicializa o jogo e gerencia o loop principal
- `screen.py`: Implementa a interface gráfica e a lógica de movimento do Pacman
- `bfs.py`: Implementa o algoritmo de busca em largura para encontrar o caminho
- `dfs.py`: Implementa o algoritmo de busca em profundidade para encontrar o caminho
- `random_maze.py`: Gera o labirinto aleatoriamente
- `tree.py`: Implementa a estrutura de árvore para armazenar o caminho
- `cores.py`: Define as cores utilizadas no jogo

## Classes Principais

### 1. Cenario (screen.py)
Responsável por renderizar e gerenciar o labirinto.

**Métodos principais:**
- `__init__(self, tamanho, pac)`: Inicializa o cenário com tamanho e referência ao Pacman
- `pintar_coluna(self, tela, numero_linha, linha)`: Renderiza uma coluna do labirinto
- `pintar(self, tela)`: Renderiza todo o labirinto
- `calcular_regras(self)`: Verifica a validade dos movimentos do Pacman

### 2. Pacman (screen.py)
Controla o personagem principal e seus movimentos.

**Métodos principais:**
- `__init__(self)`: Inicializa o Pacman na posição inicial
- `calcular_regras(self)`: Verifica se o movimento é válido
- `movimentar(self)`: Move o Pacman de acordo com o caminho do BFS/DFS
- `pintar(self, tela)`: Renderiza o Pacman na tela
- `aceitar_movimento(self)`: Atualiza a posição do Pacman após movimento válido

### 3. BFS (bfs.py)
Implementa o algoritmo de busca em largura para encontrar o caminho.

**Métodos principais:**
- `__init__(self, maze, linha_inicial, coluna_inicial)`: Inicializa o BFS com o labirinto e posição inicial
- `adicionar_rotas(self, novo_no, linha, coluna)`: Verifica as direções possíveis de movimento
- `checar_final(self, coluna, linha)`: Verifica se a posição atual é a saída
- `decidir(self, no)`: Decide o próximo movimento baseado nos filhos não visitados
- `voltar(self, no)`: Implementa backtracking quando necessário
- `executar(self)`: Executa o algoritmo BFS para encontrar o caminho

### 4. DFS (dfs.py)
Implementa o algoritmo de busca em profundidade para encontrar o caminho.

**Métodos principais:**
- `__init__(self, maze, linha_inicial, coluna_inicial)`: Inicializa o DFS com o labirinto e posição inicial
- `adicionar_rotas(self, novo_no, linha, coluna)`: Verifica as direções possíveis de movimento
- `checar_final(self, coluna, linha)`: Verifica se a posição atual é a saída
- `executar(self)`: Executa o algoritmo DFS para encontrar o caminho

### 5. BinaryTree (tree.py)
Implementa a estrutura de árvore binária para armazenar o caminho.

**Métodos principais:**
- `__init__(self)`: Inicializa a árvore
- `insert(self, value)`: Insere um novo valor na árvore
- `search(self, value)`: Busca um valor na árvore

## Funcionalidades Principais

1. **Geração de Labirinto**
   - Gera um labirinto aleatório com paredes, caminhos, entrada e saída
   - Garante que existe pelo menos um caminho da entrada até a saída

2. **Busca de Caminho**
   - Implementa dois algoritmos de busca:
     - BFS (Busca em Largura): Expande todos os nós em um nível antes de avançar
     - DFS (Busca em Profundidade): Explora o caminho mais profundo primeiro
   - Armazena o caminho em uma estrutura de árvore
   - Evita loops e caminhos inválidos

3. **Movimentação do Pacman**
   - Move o Pacman automaticamente pelo caminho encontrado
   - Verifica colisões com paredes
   - Atualiza a posição visual do personagem

4. **Interface Gráfica**
   - Renderiza o labirinto com diferentes cores para cada elemento
   - Mostra o Pacman e sua direção de movimento
   - Atualiza a tela em tempo real

## Como Executar

1. Certifique-se de ter o Python 3.x instalado
2. Instale as dependências necessárias:
   ```bash
   pip install pygame
   ```
3. Execute o arquivo principal:
   ```bash
   python main.py
   ```

## Controles

- O jogo é executado automaticamente, com o Pacman seguindo o caminho encontrado pelo BFS/DFS
- Pressione ESC ou feche a janela para encerrar o jogo

## Algoritmos de Busca

### Busca em Largura (BFS)
- Expande o nó raiz e em seguida todos os sucessores do nó raiz
- Depois, os sucessores desses nós, e assim por diante
- Garante encontrar o caminho mais curto

### Busca em Profundidade (DFS)
- Expande o nó mais profundo na borda atual da árvore
- Não havendo mais sucessores, a busca retorna à próxima profundidade acima que não foi explorada
- Pode encontrar um caminho mais rapidamente, mas não necessariamente o mais curto

## Labirinto
Implementar os métodos de busca em largura e profundidade para uma ambiente de "labirinto".
Habilidade desenvolvida: compreender como utilizar os métodos de busca na resolução de um problema.

O método deve executar em um ambiente composto por uma matriz quadrada de ordem n (até 10). Células com valor "1" representarão lugares que o agente não poderá percorrer. A célula com valor 2 representa o local de onde o agente iniciará e a célula de valor 3 o lugar onde ele precisa chegar.

Considere o custo de passo com valor igual para qualquer movimentação e que será permitida a movimentação em quadro direções (cima, baixo, esquerda e direita). A implementação deve ter uma função sucessor e uma função de teste de objetivo.
Para mais informações veja:
[como resolver](http://www.galirows.com.br/meublog/blog/proposta-de-trabalho-metodos-de-busca-para-resolver-um-labirinto/)
Para o envio, compacte em um arquivo o que for necessário para a execução do código, instruções sobre dependências para rodar o código e possíveis instruções para execução (caso a interface não seja intuitiva).

O trabalho deve ser implementado em dupla ou individualmente. Indique no fórum o nome da dupla ou se você fará sozinho (pode ser alterado posteriormente, desde que uma semana antes da entrega da atividade).

Habilidade desenvolvida: compreender como utilizar os métodos de busca na resolução de um problema.

Caso esteja com dificuldade em representar o mapa em uma árvore para busca, segue uma breve explicação abaixo:
[explicação](https://www.youtube.com/watch?v=C8otuQJB60c&t=7s)

### Busca em Largura

- Expande o nó raiz e em seguida todos os sucessores
do nó raiz. Depois, os sucessores desses nós, e assim
por diante.

### Busca em profundidade
 - Expande o nó mais profundo na borda atual da
árvore.
-  Não havendo mais sucessores, a busca retorna à
próxima profundidade acima que não foi
explorada.
