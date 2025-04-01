
import random
import pygame
from random_maze import temp_maze, WIDTH, HEIGHT

AMARELO = (255, 255, 0)
PRETO = (0, 0, 0)
VELOCIDADE = 1
AZUL = (0, 0, 255)

# width, height = 40, 30

class Cenario:
    def __init__(self, tamanho, pacman) -> None:
        self.pacman = pacman
        self.tamanho = tamanho
        self.matriz = maze

# Metodo responsavel por pintar as colunas do labirinto
    def pintar_coluna(self, tela):
        for pos in self.matriz:
          x = [1] * self.tamanho
          y =  pos[0] * self.tamanho
          cor = PRETO
          if maze.values == 2:
            cor = AZUL
            pygame.draw.rect(tela, cor, (x, y, self.tamanho, self.tamanho), 0)
          if maze.values == 0:
                pygame.draw.circle(tela, AMARELO, (x + self.tamanho/2, y+self.tamanho/2), self.tamanho//10, 0)


    def pintar(self, tela):
        for pos in self.matriz:
            self.pintar_coluna(tela)

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
        if 0 <= col <= 27 and 0 <= lin <= 28:
            if self.matriz.values()!= 2:
                self.pacman.aceitar_movimento()



class Pacman:
    def __init__(self):
        self.screen = set_screen()
        self.coluna = 1
        self.linha = 1
        self.centro_x = self.screen.get_width() / 2
        self.centro_y = self.screen.get_height() / 2
        self.tamanho =  self.screen.get_width()//30
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





