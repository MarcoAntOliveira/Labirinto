import random

def generate_random_maze(width, height, wall_density=0.25):
    maze = [[0 for _ in range(width)] for _ in range(height)]
    
    num_cells = width * height
    num_walls = int(num_cells * wall_density)
    
    wall_positions = random.sample(range(num_cells), num_walls)
    
    for pos in wall_positions:
        x = pos % width
        y = pos // width
        maze[y][x] = 1
    
    # Criar bordas do labirinto
    for x in range(width):
        maze[0][x] = 1
        maze[height-1][x] = 1
    for y in range(height):
        maze[y][0] = 1
        maze[y][width-1] = 1
    
    return maze

def print_maze(maze):
    for row in maze:
        print("".join(["#" if cell == 1 else " " for cell in row]))

width, height = 40, 30
maze = generate_random_maze(width, height)
print_maze(maze)
