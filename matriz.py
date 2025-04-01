import random


def maze():
    # Dimensões do labirinto
    width, height = 40, 30
    
    # Matriz do labirinto: 2 representa parede, 0 representa caminho livre
    maze = [[0 for _ in range(width)] for _ in range(height)]
    
    # Criar bordas do labirinto
    for x in range(width):
        maze[0][x] = 2
        maze[height-1][x] = 2
    for y in range(height):
        maze[y][0] = 2
        maze[y][width-1] = 2
        random.randint(1, 10)
    
    # Exemplo de estrutura interna do labirinto
    for y in range(2, height-2, 2):
        for x in range(2, width-2, 2):
            maze[y][x] = 2
            if x+1 < width-1:
                maze[y][x+1] = 2
            if y+1 < height-1:
                maze[y+1][x] = 2

    return maze


