import random

 # 23x23 enquadramento do pcaman fica perfeito
WIDTH = 23  # Width of the maze (must be odd).
HEIGHT = 23  # Height of the maze (must be odd).

assert WIDTH % 2 == 1 and WIDTH >= 3
assert HEIGHT % 2 == 1 and HEIGHT >= 3
SEED = 1
random.seed(SEED)

# Use these characters for displaying the maze:
EMPTY = 0
MARK = '@'
WALL = 1  # Character 2 is '█'
START = 2
END = 3
PASSED = 4
NORTH, SOUTH, EAST, WEST = 'n', 's', 'e', 'w'

# Create the filled-in maze data structure to start:
maze = [[WALL for _ in range(WIDTH)] for _ in range(HEIGHT)]

def printMaze(maze, markX=None, markY=None):
    """Displays the maze data structure in the maze argument."""
    for y in range(HEIGHT):
        for x in range(WIDTH):
            if markX == x and markY == y:
                print(MARK, end='')
            else:
                print(maze[y][x], end='')
        print()

def visit(x, y):
    """Carve out empty spaces in the maze at x, y and recursively visit neighbors."""
    maze[y][x] = EMPTY  # "Carve out" the space at x, y.
    printMaze(maze, x, y)
    print('\n\n')

    while True:
        unvisitedNeighbors = []
        if y > 1 and (x, y - 2) not in hasVisited:
            unvisitedNeighbors.append(NORTH)
        if y < HEIGHT - 2 and (x, y + 2) not in hasVisited:
            unvisitedNeighbors.append(SOUTH)
        if x > 1 and (x - 2, y) not in hasVisited:
            unvisitedNeighbors.append(WEST)
        if x < WIDTH - 2 and (x + 2, y) not in hasVisited:
            unvisitedNeighbors.append(EAST)

        if not unvisitedNeighbors:
            return

        nextDirection = random.choice(unvisitedNeighbors)
        if nextDirection == NORTH:
            nextX, nextY = x, y - 2
            maze[y - 1][x] = EMPTY
        elif nextDirection == SOUTH:
            nextX, nextY = x, y + 2
            maze[y + 1][x] = EMPTY
        elif nextDirection == WEST:
            nextX, nextY = x - 2, y
            maze[y][x - 1] = EMPTY
        elif nextDirection == EAST:
            nextX, nextY = x + 2, y
            maze[y][x + 1] = EMPTY

        hasVisited.append((nextX, nextY))
        visit(nextX, nextY)

# Carve out the paths in the maze data structure:
hasVisited = [(1, 1)]
visit(1, 1)


# Mark the start and end points
maze[1][1] = START
maze[HEIGHT - 2][WIDTH - 2] = END

# Display the final resulting maze
temp_maze = [''.join(str(cell) for cell in row) for row in maze]
print('\n'.join(temp_maze))
