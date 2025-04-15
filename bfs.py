from tree import *
from random_maze import maze

# Classe BFS (sua)
class BFS:
    def __init__(self, maze, linha_inicial, coluna_inicial):
        self.maze = maze
        self.inicio = (linha_inicial, coluna_inicial)
        self.visitados = set()
        self.caminho = {}  # para reconstruir o caminho se quiser
        self.tree = BinaryTree()

    def executar(self):
        from collections import deque

        fila = deque()
        fila.append(self.inicio)
        self.visitados.add(self.inicio)

        while fila:
            atual = fila.popleft()
            linha, coluna = atual
            print(f"Visitando: {atual}")
            self.tree.inserir_no(atual)

            # Direções: cima, baixo, esquerda, direita
            direcoes = [(-1, 0), (1, 0), (0, -1), (0, 1)]

            for dl, dc in direcoes:
                nova_linha, nova_coluna = linha + dl, coluna + dc
                vizinho = (nova_linha, nova_coluna)

                if (0 <= nova_linha < len(self.maze) and
                    0 <= nova_coluna < len(self.maze[0]) and
                    self.maze[nova_linha][nova_coluna] == 0 and
                    vizinho not in self.visitados):

                    fila.append(vizinho)
                    self.visitados.add(vizinho)
                    self.caminho[vizinho] = atual  # para reconstruir o caminho depois

# Função main para testar
def main():

    linha_inicial = 1
    coluna_inicial = 1

    bfs = BFS(maze, linha_inicial, coluna_inicial)
    bfs.executar()

    print("\nCaminho percorrido:")
    for destino, origem in bfs.caminho.items():
        print(f"{origem} -> {destino}")

if __name__ == "__main__":
    main()
