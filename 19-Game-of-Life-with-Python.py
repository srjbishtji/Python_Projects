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

