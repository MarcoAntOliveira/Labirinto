from screen import *
from tree import *


pygame.init()
# if __name__ == "__main__":


#     pacman = Pacman()
#     cenario = Cenario(600//30, pacman)

#     while(True):
#         #calcular regras
#         pacman.calcular_regras()
#         cenario.calcular_regras()

#         #Pintar a tela
#         screen.fill(PRETO)
#         cenario.pintar(screen)
#         pacman.pintar(screen)
#         pygame.display.update()
#         pygame.time.delay(100)

#         # capturar eventos
#         eventos = pygame.event.get()
#         for e in eventos:

#             if e.type == pygame.QUIT:
#                 exit()
#         pacman.processar_eventos_mouse(eventos)

if __name__ == "__main__":
    pygame.init()
    pacman = Pacman()
    cenario = Cenario(600 // len(maze), pacman)

    while True:
        # Capturar eventos
        eventos = pygame.event.get()
        for e in eventos:
            if e.type == pygame.QUIT:
                pygame.quit()
                exit()
        pacman.processar_eventos_mouse(eventos)

        # Calcular regras
        pos = (pacman.linha, pacman.coluna)
        pacman.calcular_regras()
        cenario.calcular_regras()

        # Pintar a tela
        screen.fill(PRETO)
        cenario.pintar(screen)
        pacman.pintar(screen)
        pygame.display.update()
        pygame.time.delay(100)



# def main():
#     # Labirinto: 0 = livre, 2 = parede, 3 = saída


#     linha_inicial = 0
#     coluna_inicial = 0

#     bfs = BFS(maze, linha_inicial, coluna_inicial)
#     saida = bfs.procura_saida()

#     if saida:
#         caminho = bfs.reconstruir_caminho(saida)
#         print("Caminho até a saída:", caminho)
#     else:
#         print("Não foi possível encontrar a saída.")

# if __name__ == "__main__":
#     main()
