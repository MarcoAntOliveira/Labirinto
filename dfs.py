from tree import *
from random_maze import maze


class DFS:
    def __init__(self, maze, linha_inicial, coluna_inicial):
        self.maze = maze
        self.inicio = (linha_inicial, coluna_inicial)
        self.visitados = set()
        self.tree = BinaryTree()
        self.saida = None
        self.caminho = []
        self.pilha_caminho = []
        self.custo = 0

    def adicionar_rotas(self, no, linha, coluna):
        # Mesmo princípio do BFS
        # Esquerda
        if coluna - 1 >= 0 and self.maze[linha][coluna - 1] != 1 and (linha, coluna - 1) not in self.visitados:
            no.left_child = No((linha, coluna - 1))

        # Direita
        if coluna + 1 < len(self.maze[0]) and self.maze[linha][coluna + 1] != 1 and (linha, coluna + 1) not in self.visitados:
            no.right_child = No((linha, coluna + 1))

        # Cima
        if linha - 1 >= 0 and self.maze[linha - 1][coluna] != 1 and (linha - 1, coluna) not in self.visitados:
            no.up_child = No((linha - 1, coluna))

        # Baixo
        if linha + 1 < len(self.maze) and self.maze[linha + 1][coluna] != 1 and (linha + 1, coluna) not in self.visitados:
            no.down_child = No((linha + 1, coluna))

    def checar_final(self, coluna, linha):
        return self.maze[linha][coluna] == 3

    def executar(self):
        linha, coluna = self.inicio
        raiz = No((linha, coluna))
        self.tree.root = raiz

        pilha = [raiz]
        self.visitados.add((linha, coluna))

        while pilha:
            atual = pilha.pop()
            linha, coluna = atual.pos
            self.caminho.append(atual)
            self.custo += 1

            if self.checar_final(coluna, linha):
                self.saida = atual
                print("Saída encontrada!")
                break

            self.adicionar_rotas(atual, linha, coluna)

            # Adiciona os filhos à pilha (em ordem inversa se quiser comportamento semelhante à direita > baixo > esquerda > cima)
            for child in [atual.down_child, atual.up_child, atual.right_child, atual.left_child]:
                if child and child.pos not in self.visitados:
                    pilha.append(child)
                    self.visitados.add(child.pos)
