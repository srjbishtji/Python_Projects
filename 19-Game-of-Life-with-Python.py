# The game of life, imagined by the British mathematician John H. Conway, is a Solitaire type game analogous to the rise, fall and alternations of a society of living organisms. 

# The game of life was one of the earliest examples of a problem in modern mathematics called cellular automata.

# The Game of Life :

# The game uses a rectangular grid of cells of infinite size in which each cell is empty or occupied by an organism. It is said that occupied cells are alive, while empty ones are dead. The game is played over a specific period, with each turn creating a new “generation” based on the arrangement of living organisms in the current configuration.

# The status of a cell in the next generation is determined by applying the following four basic rules to each cell of the current configuration:

# If a cell is alive and has two or three living neighbours, the cell stays alive in the next generation.
# A living cell that has no living neighbours or only one living neighbour dies of isolation in the next generation.
# A living cell that has four or more living neighbours dies from overpopulation in the next generation.
# A dead cell with exactly three living neighbours results in birth and becomes alive in the next generation.

# Implementing The Game of Life with Python :

# The Game of Life begins with an initial setup provided by the user. Successive generations are created by applying the set of rules simultaneously to each cell in the grid. Interesting patterns can develop as the population of organisms changes, increases, or eventually disappears. Now let’s see how to implement the game of life with Python:

# Code :

from typing import List

class GameOfLife:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        # Neighbors array to find 8 neighboring cells for a given cell
        neighbors = [(1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1)]

        rows = len(board)
        cols = len(board[0])

        # Create a copy of the original board
        copy_board = [[board[row][col] for col in range(cols)] for row in range(rows)]

        # Iterate through board cell by cell
        for row in range(rows):
            for col in range(cols):

                # For each cell count the number of live neighbors
                live_neighbors = 0
                for neighbor in neighbors:
                    r = row + neighbor[0]
                    c = col + neighbor[1]

                    # Check the validity of the neighboring cell and if it was originally a live cell
                    if 0 <= r < rows and 0 <= c < cols and copy_board[r][c] == 1:
                        live_neighbors += 1

                # Rule 1 or Rule 3: Live cell with fewer than 2 or more than 3 live neighbors dies
                if copy_board[row][col] == 1 and (live_neighbors < 2 or live_neighbors > 3):
                    board[row][col] = 0
                # Rule 4: Dead cell with exactly 3 live neighbors becomes alive
                if copy_board[row][col] == 0 and live_neighbors == 3:
                    board[row][col] = 1
# Example usage
if __name__ == "__main__":
    game = GameOfLife()
    
    # Example board
    board = [
        [0, 1, 0],
        [0, 0, 1],
        [1, 1, 1],
        [0, 0, 0]
    ]

    print("Original board:")
    for row in board:
        print(row)

    game.gameOfLife(board)

    print("\nBoard after one step:")
    for row in board:
        print(row)