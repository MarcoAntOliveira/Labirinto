import pygame
from random_maze import maze
from bfs import BFS
from tree import WIDTH, HEIGHT, BinaryTree
from colors import *
import random
from dfs import DFS

class Cenario:
    def __init__(self, tamanho, pac) -> None:
        self.pacman = pac
        self.tamanho = tamanho
        self.matriz = maze
        self.pontos = 0



    def pintar_coluna(self, tela, numero_linha, linha):
        for numero_coluna, coluna in enumerate(linha):
            x = numero_coluna * self.tamanho
            y = numero_linha * self.tamanho

            if coluna == 1:  # parede
               pygame.draw.rect(tela, AZUL, (x, y, self.tamanho, self.tamanho), 0)
            elif coluna == 0:  # caminho vazio
               pygame.draw.circle(tela, AMARELO, (x + self.tamanho/2, y + self.tamanho/2), self.tamanho//10, 0)
            elif coluna == 2:  # início
               pygame.draw.circle(tela, VERDE, (x + self.tamanho/2, y + self.tamanho/2), self.tamanho//10, 0)
            elif coluna == 3:  # fim
               pygame.draw.circle(tela, ROSA, (x + self.tamanho/2, y + self.tamanho/2), self.tamanho//10, 0)
            elif (numero_linha, numero_coluna) in self.pacman.trilha:
              pygame.draw.circle(tela, VERMELHO, (x + self.tamanho/2, y + self.tamanho/2), self.tamanho//10, 0)
            else:
               pygame.draw.circle(tela, AMARELO, (x + self.tamanho/2, y + self.tamanho/2), self.tamanho//10, 0)

    def pintar(self, tela):
        for numero_linha, linha in enumerate(self.matriz):
            self.pintar_coluna(tela, numero_linha, linha)


    def calcular_regras(self):

      # Método responsavel por verifcar se a proxima posição do pacman éválida
      col = self.pacman.coluna_intencao
      lin = self.pacman.linha_intencao
      if 0 <= lin < len(self.matriz) and 0 <= col < len(self.matriz[0]):
          if self.matriz[lin][col] != 1:
              self.pacman.aceitar_movimento()

class Pacman:
    def __init__(self):
        # Inicializa o Pacman na posição de início (1,1)
        self.linha = 1
        self.coluna = 1
        # self.bfs = BFS(maze, self.linha, self.coluna)
        self.dfs = DFS(maze, self.linha, self.coluna)
        self.centro_x = screen.get_width() // len(maze)
        self.centro_y = screen.get_height() // len(maze)

        self.tamanho = screen.get_width()//30
        self.raio = self.tamanho // 2

        # self.bfs.executar()  # Executa o BFS para encontrar o caminho
        self.dfs.executar()  # Executa o DFS para encontrar o caminho
        self.coluna_intencao = self.coluna
        self.linha_intencao = self.linha
        self.trilha = []



    # def movimentar(self):
    #     """
    #     Move o agente para o próximo passo baseado na fila da BFS.
    #     """

    #     if self.bfs.caminho:
    #       no = self.bfs.caminho.popleft()
    #       self.linha_intencao, self.coluna_intencao = no.pos
    #       self.bfs.caminho_percorrido.append(no.pos)

    #     else:
    #         print("Fila vazia — caminho completo ou BFS não foi executada.")
    def movimentar(self):
      if self.dfs.caminho:
          no = self.dfs.caminho.pop()
          self.trilha.append(no.pos)
        
          self.linha_intencao, self.coluna_intencao = no.pos

      else:
          print("Pilha vazia — caminho completo ou DFS não foi executada.")

    def pintar(self, tela):
      """
      responsável por fazer a pintura do personagem na tela

      """
      # Atualiza a posição visual do Pacman
      self.centro_x = self.coluna * self.tamanho + self.raio
      self.centro_y = self.linha * self.tamanho + self.raio

      pygame.draw.circle(screen, AMARELO, (self.centro_x, self.centro_y), self.raio)

      #desenho boca
      canto_boca = (self.centro_x, self.centro_y)
      labio_superior = (self.centro_x + self.raio, self.centro_y - self.raio)
      labio_inferior = (self.centro_x + self.raio , self.centro_y)
      pontos = [canto_boca, labio_superior, labio_inferior]
      pygame.draw.polygon(tela,PRETO, pontos, 0)

      #desenho olho
      olho_x =  int(self.centro_x + self.raio/5)
      olho_y = int(self.centro_y - self.raio*0.50)
      olho_raio = int(self.raio/10)
      pygame.draw.circle(tela, PRETO, (olho_x, olho_y), olho_raio, 0)

    def aceitar_movimento(self):
        """
        Se o movimento for válido, atualiza a posição do Pacman
        """
        self.linha = self.linha_intencao
        self.coluna = self.coluna_intencao
        print(f"se movendo para linha{self.linha} e coluna {self.coluna}")
        pygame.time.delay(10)

    def calcular_regras(self):
      col = int(self.coluna_intencao)
      lin = int(self.linha_intencao)
      # Verifica se a posição está dentro dos limites do labirinto
      if 0 <= col < len(maze[0]) and 0 <= lin < len(maze):
          # Verifica se não é parede (1)
          if maze[lin][col] != 1:
              self.aceitar_movimento()


screen  = pygame.display.set_mode((800, 600), 0)

