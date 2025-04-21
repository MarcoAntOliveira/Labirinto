from screen import *
from tree import *


def main():
    pygame.init()
    screen = pygame.display.set_mode((800, 600), 0)
    pacman = Pacman()
    cenario = Cenario(600 // len(maze), pacman)

    while True:
        # Capturar eventos
        eventos = pygame.event.get()
        for e in eventos:
            if e.type == pygame.QUIT:
                pygame.quit()
                exit()

        # Calcular regras e movimentar
        pacman.movimentar()
        cenario.calcular_regras()

        # Pintar a tela
        screen.fill(PRETO)
        cenario.pintar(screen)
        pacman.pintar(screen)
        pygame.display.update()
        pygame.time.delay(100)

if __name__ == "__main__":
    main()
