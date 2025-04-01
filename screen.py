
import random
import pygame
from random_maze import maze

AMARELO = (255, 255, 0)
PRETO = (0, 0, 0)
VELOCIDADE = 1
AZUL = (0, 0, 255)

width, height = 40, 30

class Cenario:
    def __init__(self, tamanho, pacman) -> None:
        self.pacman = pacman
        self.tamanho = tamanho
        self.matriz = maze

# Metodo responsavel por pintar as colunas do labirinto
    def pintar_coluna(self, tela, numero_linha, linha):
        for numero_coluna, coluna in enumerate(linha):
            x = numero_coluna * self.tamanho
            y = numero_linha * self.tamanho
            cor = PRETO
            if coluna == 2:
                cor = AZUL
            pygame.draw.rect(tela, cor, (x, y, self.tamanho, self.tamanho), 0)
            if coluna == 1:
                pygame.draw.circle(tela, AMARELO, (x + self.tamanho/2, y+self.tamanho/2), self.tamanho//10, 0)


    def pintar(self, tela):
        for numero_linha, linha in enumerate(self.matriz):
            self.pintar_coluna(tela, numero_linha, linha)

    def calcular_regras(self):
        col = self.pacman.coluna_intencao
        lin = self.pacman.linha_intencao
        if 0 <= col <= 27 and 0 <= lin <= 28:
            if self.matriz[col][lin]!= 2:
                self.pacman.aceitar_movimento()



class Pacman:
    def __init__(self):
        self.screen = set_screen()
        self.coluna = 1
        self.linha = 1
        self.centro_x = self.screen.get_width() / 2
        self.centro_y = self.screen.get_height() / 2
        self.tamanho =  self.screen.get_width()//40
        self.raio = self.tamanho // 2
        self.vel_x = 0
        self.vel_y = 0
        self.coluna_intencao = self.coluna
        self.linha_intencao = self.linha

    # def calcular_regras(self):
    #     col = int(self.coluna_intencao)
    #     lin = int(self.linha_intencao)
    #     if 0 <= col < width and 0 <= lin < height:
    #         if self.matriz[lin][col] != 2:
    #             self.pacman.aceitar_movimento()

    def calcular_regras(self):
        self.coluna_intencao = self.coluna + self.vel_x
        self.linha_intencao= self.linha + self.vel_y

        self.centro_x = int(self.coluna*self.tamanho + self.raio)
        self.centro_y = int(self.linha*self.tamanho + self.raio)



    def pintar(self, tela):
        pygame.draw.circle(self.screen, AMARELO, (self.centro_x, self.centro_y), self.raio)

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

    # def processar_eventos(self, eventos):
    #     for e in eventos:
    #         if e.type == pygame.KEYDOWN:
    #             if e.key  == pygame.K_RIGHT:
    #                 self.vel_x = VELOCIDADE
    #             elif e.key  == pygame.K_LEFT:
    #                 self.vel_x = -VELOCIDADE
    #             elif e.key  == pygame.K_DOWN:
    #                 self.vel_y = VELOCIDADE
    #             elif e.key  == pygame.K_UP:
    #                 self.vel_y = -VELOCIDADE


    #         elif e.type == pygame.KEYUP:
    #             if e.key == pygame.K_RIGHT:
    #                 self.vel_x = 0
    #             elif e.key == pygame.K_LEFT:
    #                 self.vel_x = 0
    #             elif e.key == pygame.K_DOWN:
    #                 self.vel_y = 0
    #             elif e.key == pygame.K_UP:
    #                 self.vel_y = 0
    def aceitar_movimento(self):
        self.linha = self.linha_intencao
        self.coluna = self.coluna_intencao
    def processar_eventos_mouse(self, eventos):
        delay = 100
        for e in eventos:
            if e.type == pygame.MOUSEMOTION:
                mouse_x, mouse_y = e.pos
                self.coluna = int(mouse_x // self.tamanho)
                self.linha = int(mouse_y // self.tamanho)




    def aceitar_movimento(self):
        self.linha = int(self.linha_intencao)
        self.coluna = int(self.coluna_intencao)

    def processar_eventos_mouse(self, eventos):
        delay = 100
        for e in eventos:
            if e.type == pygame.MOUSEMOTION:
                mouse_x, mouse_y = e.pos
                self.coluna = int((mouse_x - self.centro_x) / delay)
                self.linha = int((mouse_y - self.centro_y) / delay)

def init_pygame():
  pygame.init()

def set_screen():
  screen  = pygame.display.set_mode((800, 600), 0)
  return screen





