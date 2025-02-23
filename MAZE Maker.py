import random
import matplotlib.pyplot as plt
import numpy as np

# Function to generate a solvable maze
def generate_solvable_maze(size):
    maze = [[0 for _ in range(size)] for _ in range(size)]
    
    x, y = 0, 0
    maze[x][y] = 1  # Start point
    
    while x < size - 1 or y < size - 1:
        if x < size - 1 and (y == size - 1 or random.choice([True, False])):
            x += 1
        else:
            y += 1
        maze[x][y] = 1  # Mark as path
    
    for i in range(size):
        for j in range(size):
            if maze[i][j] == 0 and random.random() > 0.7:
                maze[i][j] = 1
    
    return maze

# DFS-based maze solving function
def solve_maze(maze):
    size = len(maze)
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    visited = [[False for _ in range(size)] for _ in range(size)]

    def is_valid(x, y):
        return 0 <= x < size and 0 <= y < size and maze[x][y] == 1 and not visited[x][y]

    def dfs(x, y):
        visited[x][y] = True
        if x == size - 1 and y == size - 1:
            return True
        
        for dx, dy in directions:
            new_x, new_y = x + dx, y + dy
            if is_valid(new_x, new_y):
                maze[new_x][new_y] = '.'  # Mark the path
                if dfs(new_x, new_y):
                    return True
                maze[new_x][new_y] = 1  # Backtrack
        return False
    
    maze[0][0] = '.'  # Start point
    if not dfs(0, 0):
        print("No solution found")
    return maze

# Function to visualize the maze using matplotlib
def plot_maze(maze):
    size = len(maze)
    maze_array = np.zeros((size, size))
    
    for i in range(size):
        for j in range(size):
            if maze[i][j] == 0:  # Wall
                maze_array[i][j] = 0  # Black
            elif maze[i][j] == 1:  # Path
                maze_array[i][j] = 1  # White
            elif maze[i][j] == '.':  # Solved path
                maze_array[i][j] = 0.5  # Gray

    plt.imshow(maze_array, cmap="bone")
    plt.title("Maze with Solved Path")
    plt.show()

# Function to print the maze in CLI as 0s and 1s
def print_maze(maze):
    for row in maze:
        row_print = ['.' if cell == '.' else str(cell) for cell in row]
        print(' '.join(row_print))

# Example usage
size = 20 # You can change the maze size here
maze = generate_solvable_maze(size)
print("Generated solvable maze:")

# Solve the maze
solved_maze = solve_maze(maze)

# Print the maze in CLI
print("\nMaze in CLI format (0 = wall, 1 = path):")
print_maze(solved_maze)

# Visualize the maze
plot_maze(solved_maze)
