# Labirinto - Projeto de Busca em Labirinto

Este projeto implementa um jogo de labirinto onde o Pacman deve encontrar o caminho da entrada até a saída usando o algoritmo de busca em largura (BFS).

## Estrutura do Projeto

O projeto é composto pelos seguintes arquivos principais:

- `main.py`: Arquivo principal que inicializa o jogo e gerencia o loop principal
- `screen.py`: Implementa a interface gráfica e a lógica de movimento do Pacman
- `bfs.py`: Implementa o algoritmo de busca em largura para encontrar o caminho
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
- `movimentar(self)`: Move o Pacman de acordo com o caminho do BFS
- `pintar(self, tela)`: Renderiza o Pacman na tela
- `aceitar_movimento(self)`: Atualiza a posição do Pacman após movimento válido

### 3. BFS (bfs.py)
Implementa o algoritmo de busca em largura para encontrar o caminho.

**Métodos principais:**
- `__init__(self, maze, linha_inicial, coluna_inicial)`: Inicializa o BFS com o labirinto e posição inicial
- `busca_rotas(self, novo_no, coluna, linha)`: Verifica as direções possíveis de movimento
- `checar_final(self, coluna, linha)`: Verifica se a posição atual é a saída
- `decidir(self, no)`: Decide o próximo movimento baseado nos filhos não visitados
- `executar(self)`: Executa o algoritmo BFS para encontrar o caminho

### 4. BinaryTree (tree.py)
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
   - Implementa o algoritmo BFS para encontrar o caminho mais curto
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

- O jogo é executado automaticamente, com o Pacman seguindo o caminho encontrado pelo BFS
- Pressione ESC ou feche a janela para encerrar o jogo

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

# Pacman
Este repositório é dedicado ao desenvolvimento do clássico jogo Pacman, com o objetivo de explorar conceitos de programação de jogos e interação com bibliotecas gráficas.

## Bibliotecas Utilizadas
Pygame: Biblioteca principal utilizada para criar e gerenciar a interface gráfica, eventos, e animações do jogo.
Classes Implementadas

## Cenario
Responsável por gerenciar o layout do labirinto, incluindo o desenho das paredes e o controle das regras do jogo.

### Métodos Principais:
#### pintar_coluna
Desenha as colunas do labirinto na tela principal com base no número de linhas especificado.

#### processar_eventos
Controla a movimentação do personagem, utilizando os eventos capturados pela biblioteca Pygame.

#### maze
Gera labirintos com paredes aleatórias, proporcionando novos desafios a cada execução.

#### calcular
Determina se o personagem atingiu uma parede do labirinto, impedindo movimentos inválidos.

## Pacman
Classe responsável por gerenciar as ações e comportamentos do personagem principal.

#### calcular
*determinar os movimentos possiveis que o personagem pode realizar*



```python
def calcular_regras(self):

col = self.pacman.coluna_intencao

lin = self.pacman.linha_intencao

if 0 <= col <= 5 and 0 <= lin <= 5:

if self.matriz[lin][col] != 2:

self.pacman.aceitar_movimento()
```


### Class BFS
