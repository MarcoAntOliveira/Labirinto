import random
import pygame
from random_maze import *

AMARELO = (255, 255, 0)
PRETO = (0, 0, 0)
VELOCIDADE = 1
AZUL = (0, 0, 255)

class Cenario:
    def __init__(self, tamanho, pac) -> None:
        self.pacman = pac
        self.tamanho = tamanho
        self.matriz = maze
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

    '''def maze(self):
        # Dimensões do labirinto
        width, height = 40, 30

        # Matriz do labirinto: 2 representa parede, 0 rep, resenta caminho livre
        maze = [[0 for _ in range(width)] for _ in range(height)]

        # Criar bordas do labirinto
        for x in range(width):
            maze[0][x] = 2
            maze[height-1][x] = 2

        for y in range(height):
            maze[y][0] = 2
            maze[y][width-1] = 2


        # Exemplo de estrutura interna do labirinto
        for y in range(2, height-2, 2):
            for x in range(2, width-2, 2):
                maze[y][x] = 2
                if x+1 < width-1:
                    maze[y][x+1] = 2
                if y+1 < height-1:
                    maze[y+1][x] = 2

        return maze'''

    # def maze(self):
    #     wall_density=0.15
    #     width, height = 40, 30
    #     maze = [[0 for _ in range(width)] for _ in range(height)]

    #     num_cells = width * height
    #     num_walls = int(num_cells * wall_density)

    #     wall_positions = random.sample(range(num_cells), num_walls)
    #     pills_positions = random.sample(range(num_cells), num_walls)


    #     for pos in wall_positions:
    #         x = pos % width
    #         y = pos // width
    #         maze[y][x] = 2

    #     for pos in pills_positions:
    #         if pos in wall_positions:
    #             pass
    #         x_pills = pos % width
    #         y_pills = pos // width
    #         maze[y_pills][x_pills] = 1

    #     # Criar bordas do labirinto
    #     for x in range(width):
    #         maze[0][x] = 2
    #         maze[height-1][x] = 2
    #     for y in range(height):
    #         maze[y][0] = 2
    #         maze[y][width-1] = 2

    #     return maze
    def calcular_regras(self):
        col = self.pacman.coluna_intencao
        lin = self.pacman.linha_intencao
        if 0 <= col <= 5 and 0 <= lin <= 5:
            if self.matriz[lin][col] != 2:
                self.pacman.aceitar_movimento()



class Pacman:
    def __init__(self):
        self.coluna = 1
        self.linha = 1
        self.centro_x = screen.get_width() / 2
        self.centro_y = screen.get_height() / 2
        self.tamanho =  screen.get_width()//30
        self.raio = self.tamanho // 2

        self.vel_x = 0
        self.vel_y = 0
        self.coluna_intencao = self.coluna
        self.linha_intencao = self.linha

    def calcular_regras(self):
        col = int(self.coluna_intencao)
        lin = int(self.linha_intencao)
        if 0 <= col < len(maze[0]) and 0 <= lin < len(maze[1]):
            if maze[lin][col] != 2:
                self.aceitar_movimento()

    # def calcular_regras(self):
    #     self.coluna_intencao = self.coluna + self.vel_x
    #     self.linha_intencao= self.linha + self.vel_y

    #     self.centro_x = int(self.coluna*self.tamanho + self.raio)
    #     self.centro_y = int(self.linha*self.tamanho + self.raio)



    def pintar(self, tela):
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
        self.linha = self.linha_intencao
        self.coluna = self.coluna_intencao
    def processar_eventos_mouse(self, eventos):
        delay = 100
        for e in eventos:
            if e.type == pygame.MOUSEMOTION:
                mouse_x, mouse_y = e.pos
                self.coluna = (mouse_x - self.centro_x) / delay
                self.linha = (mouse_y - self.centro_y) / delay


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



pygame.init()

screen  = pygame.display.set_mode((800, 600), 0)

if __name__ == "__main__":
    pacman = Pacman()
    cenario = Cenario(600//30, pacman)

while(True):
    #calcular regras
    pacman.calcular_regras()
    cenario.calcular_regras()

    #Pintar a tela
    screen.fill(PRETO)
    cenario.pintar(screen)
    pacman.pintar(screen)
    pygame.display.update()
    pygame.time.delay(100)

    # capturar eventos
    eventos = pygame.event.get()
    for e in eventos:

        if e.type == pygame.QUIT:
            exit()
    pacman.processar_eventos_mouse(eventos)
