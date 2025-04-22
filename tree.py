from random_maze import *
from collections import deque
class No:
    def __init__(self, value, left=None, right=None, up=None, down=None, pai = None):
        self.pos = tuple(value)
        self.left_child = left
        self.right_child = right
        self.up_child = up
        self.down_child = down
        self.pai = pai

class BinaryTree:
          def __init__(self):
            self.root = None
            self.next_lis = []


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

          def imprimir_arvore(self):
              if not self.root:
                  print("Árvore vazia.")
                  return

              fila = deque()
              fila.append((self.root, 0))  # (nó, nível)
              visitados = set()

              nivel_atual = -1
              while fila:
                  no, nivel = fila.popleft()

                  if no.pos in visitados:
                      continue
                  visitados.add(no.pos)

                  if nivel != nivel_atual:
                      nivel_atual = nivel
                      print(f"\nNível {nivel}: ", end="")

                  print(f"{no.pos}", end=" ")

                  if no.left_child:
                      fila.append((no.left_child, nivel + 1))
                  if no.right_child:
                      fila.append((no.right_child, nivel + 1))
                  if no.up_child:
                      fila.append((no.up_child, nivel + 1))
                  if no.down_child:
                      fila.append((no.down_child, nivel + 1))


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

