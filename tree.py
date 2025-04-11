from random_maze import *
from collections import deque
class No:
    def __init__(self, value, left=None, right=None, up=None, down=None):
        self.pos = value
        self.left_child = left
        self.right_child = right
        self.up_child = up
        self.down_child = down

class BinaryTree:
    def __init__(self):
        self.root = None
        self.next_lis = []
        self.searched = []

    def not_searched(self, pos):
        """Verifica se o valor já foi percorrido"""
        return pos in self.searched

    def inserir_no(self, pos):
        novo = No(pos)
        if self.not_searched(pos):
            print(f"Essa posição {pos} já foi percorrida.")
            return

        self.searched.append(pos)

        if self.root is None:
            self.root = novo
        else:
            atual = self.root
            while True:
                anterior = atual
                if pos < atual.pos:  # Ir para baixo
                    if atual.down_child is None:
                        anterior.down_child = novo
                        return
                    atual = atual.down_child
                elif pos > atual.pos:  # Ir para cima
                    if atual.up_child is None:
                        anterior.up_child = novo
                        return
                    atual = atual.up_child
                else:
                    # Se o valor for igual, tentamos a direita ou esquerda
                    if atual.right_child is None:
                        anterior.right_child = novo
                        return
                    atual = atual.right_child

# Função para exibir a árvore em pré-ordem
def pre_ordem(no):
    if no:
        print(no.pos, end=" -> ")
        pre_ordem(no.left_child)
        pre_ordem(no.right_child)
        pre_ordem(no.up_child)
        pre_ordem(no.down_child)

# Função para encontrar e imprimir as folhas (nós sem filhos)
def imprimir_folhas(no):
    if no:
        if not no.left_child and not no.right_child and not no.up_child and not no.down_child:
            print(no.pos, end=" ")
        imprimir_folhas(no.left_child)
        imprimir_folhas(no.right_child)
        imprimir_folhas(no.up_child)
        imprimir_folhas(no.down_child)
# Função principal (main) para testes

class BFS:
    def __init__(self, maze, linha_inicial, coluna_inicial):
        self.maze = maze
        self.inicio = (linha_inicial, coluna_inicial)
        self.visitados = set()
        self.caminho = {}  # para reconstruir o caminho se quiser
        self.tree = BinaryTree()


        

    # def procura_saida(self):
    #     fila = deque()
    #     fila.append(self.inicio)
    #     self.visitados.add(self.inicio)

    #     while fila:
    #         linha, coluna = fila.popleft()

    #         if self.eh_saida(linha, coluna):
    #             print("Saída encontrada!")
    #             return (linha, coluna)

    #         # Vizinhos: cima, baixo, esquerda, direita
    #         for dl, dc in [(-1,0), (1,0), (0,-1), (0,1)]:
    #             nova_linha = linha + dl
    #             nova_coluna = coluna + dc
    #             nova_pos = (nova_linha, nova_coluna)

    #             if self.posicao_valida(nova_linha, nova_coluna) and nova_pos not in self.visitados:
    #                 fila.append(nova_pos)
    #                 self.visitados.add(nova_pos)
    #                 self.caminho[nova_pos] = (linha, coluna)  # de onde veio

    #     print("Saída não encontrada.")
    #     return None

    def eh_saida(self, linha, coluna):
        # você pode definir a saída como qualquer critério, por exemplo:
        return self.maze[linha][coluna] == 3  # onde 3 representa a saída

    def posicao_valida(self, linha, coluna):
        linhas = len(self.maze)
        colunas = len(self.maze[0])
        return (
            0 <= linha < linhas and
            0 <= coluna < colunas and
            self.maze[linha][coluna] != 2  # 2 representa parede
        )


if __name__ == "__main__":
    arvore = BinaryTree()

    # Inserindo alguns nós
    arvore.inserir_no(5)
    arvore.inserir_no(3)
    arvore.inserir_no(7)
    arvore.inserir_no(2)
    arvore.inserir_no(4)
    arvore.inserir_no(6)
    arvore.inserir_no(8)

    # Exibindo a árvore em pré-ordem
    print("Árvore em pré-ordem:")
    pre_ordem(arvore.root)
    print("\n")

    # Exibindo as folhas da árvore
    print("Folhas da árvore:")
    imprimir_folhas(arvore.root)
    print()
