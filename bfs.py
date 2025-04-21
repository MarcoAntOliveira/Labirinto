from tree import *
from random_maze import maze
from collections import deque

# Classe BFS (sua)
class BFS:
    def __init__(self, maze, linha_inicial, coluna_inicial):
        self.maze = maze
        self.inicio = (linha_inicial, coluna_inicial)
        self.visitados = set()  # Agora, um set para garantir a busca eficiente
        self.tree = BinaryTree()
        self.saida = None
        self.posicao = list()

        self.caminho = deque()

    def adicionar_rotas(self, novo_no, linha, coluna):
        """
        Verifica as quatro direções possíveis (esquerda, direita, cima, baixo)
        e conecta os filhos ao nó atual se não forem paredes (1).
        """
        # Esquerda
        if coluna - 1 >= 0 and self.maze[linha][coluna - 1] != 1:
            if (linha, coluna - 1) not in self.visitados:
                novo_no.left_child = No((linha, coluna - 1))
                self.visitados.add((linha, coluna - 1))

        # Direita
        if coluna + 1 < len(self.maze[0]) and self.maze[linha][coluna + 1] !=1:
            if (linha, coluna + 1) not in self.visitados:
                novo_no.right_child = No((linha, coluna + 1))
                self.visitados.add((linha, coluna + 1))

        # Cima
        if linha - 1 >= 0 and self.maze[linha - 1][coluna] !=1:
            if (linha - 1, coluna) not in self.visitados:
                novo_no.up_child = No((linha - 1, coluna))
                self.visitados.add((linha - 1, coluna))

        # Baixo
        if linha + 1 < len(self.maze) and self.maze[linha + 1][coluna] != 1:
            if (linha + 1, coluna) not in self.visitados:
                novo_no.down_child = No((linha + 1, coluna))
                self.visitados.add((linha + 1, coluna))

    def checar_final(self, coluna, linha):
        """
        Verifica se a posição atual é a saída
        """
        if 0 <= linha < len(maze) and 0 <= coluna < len(maze[0]):
            return maze[linha][coluna] == 3
        return False

    def decidir(self, no: No):
        """
        Decide o próximo movimento baseado nos filhos não visitados
        """
        if no.right_child and no.right_child.pos not in self.visitados:
            return no.right_child.pos
        if no.down_child and no.down_child.pos not in self.visitados:
            return no.down_child.pos
        if no.left_child and no.left_child.pos not in self.visitados:
            return no.left_child.pos
        if no.up_child and no.up_child.pos not in self.visitados:
            return no.up_child.pos
        return None

    def mover(self, no: No, linha, coluna):
        if no.right_child:
            return [linha, coluna + 1]
        if no.down_child:
            return [linha + 1, coluna]
        if no.left_child:
            return [linha, coluna - 1]
        if no.up_child:
            return [linha - 1, coluna]
        return None  # Garante que algo seja retornado sempre

    def executar(self):
        linha, coluna = self.inicio
        print(f"{maze[linha][coluna]}")
        print(f"Início: {linha}, {coluna}")
        self.visitados.add((linha, coluna))
        raiz = No((linha, coluna))
        self.tree.root = raiz

        fila = deque()
        fila.append(raiz)
        self.caminho.append(raiz)
        no_atual = raiz
        self.adicionar_rotas(no_atual, linha, coluna)


        while fila:
            atual = fila.popleft()  # Tira o primeiro item da self. fila
            linha, coluna = atual.pos


            if self.checar_final(coluna, linha):
                self.saida = atual
                break

            # Expande as rotas para o próximo nó
            self.adicionar_rotas(atual, linha, coluna)

            # Adiciona os filhos à fila se existirem
            for child in [atual.left_child, atual.right_child, atual.up_child, atual.down_child]:
                if child:
                    fila.append(child)
                    self.caminho.append(child)



# ==================== MAIN ====================
def main():
    linha_inicial = 1
    coluna_inicial = 1
    bfs = BFS(maze, linha_inicial, coluna_inicial)
    bfs.executar()


    # if bfs.saida:
    #     bfs.reconstruir_caminho(bfs.saida)
    # else:
    #     print("Saída não encontrada no labirinto.")

if __name__ == "__main__":
    main()
