"""
Clone of 2048 game.
"""

# import poc_2048_gui
import random

# Directions, DO NOT MODIFY
UP = 1
DOWN = 2
LEFT = 3
RIGHT = 4

# Offsets for computing tile indices in each direction.
# DO NOT MODIFY this dictionary.
OFFSETS = {UP: (1, 0),
           DOWN: (-1, 0),
           LEFT: (0, 1),
           RIGHT: (0, -1)}


def merge(line):
    """
    Helper function that merges a single row or column in 2048
    """
    result_of_multiply = [0] * (len(line))

    counter = 0
    for index in xrange(len(line)):
        if line[index] != 0:
            result_of_multiply[counter] = line[index]
            counter += 1

    for index in xrange(len(result_of_multiply) - 1):
        if result_of_multiply[index] == result_of_multiply[index + 1]:
            result_of_multiply[index] *= 2
            result_of_multiply[index + 1] = 0

    final_result = [0] * (len(line))

    counter = 0
    for index in xrange(len(line)):
        if result_of_multiply[index] != 0:
            final_result[counter] = result_of_multiply[index]
            counter += 1
    return final_result


class TwentyFortyEight:
    """
    Class to run the game logic.
    """

    def __init__(self, grid_height, grid_width):
        self.grid_height = grid_height
        self.grid_width = grid_width
        self.tiles = [[0 for col in range(self.get_grid_width() + 1)] for row in range(self.get_grid_height() + 1)]
        self.new_tile()
        self.new_tile()

    def reset(self):
        """
        Reset the game so the grid is empty except for two
        initial tiles.
        """
        self.tiles = [[0 for col in range(self.get_grid_width())] for row in range(self.get_grid_height())]
        self.new_tile()
        self.new_tile()

    def __str__(self):
        """
        Return a string representation of the grid for debugging.
        """
        string = ''
        for row in xrange(self.get_grid_height()):
            for col in xrange(self.get_grid_width()):
                string += str(self.get_tile(row, col)) + ' '
            string += '\n'
        return string

    def get_grid_height(self):
        """
        Get the height of the board.
        """
        return self.grid_height

    def get_grid_width(self):
        """
        Get the width of the board.
        """
        return self.grid_width

    def move(self, direction):
        """
        Move all tiles in the given direction and add
        a new tile if any tiles moved.
        """
        if direction == UP:
            offset = OFFSETS.get('UP')
            for column in xrange(self.get_grid_width()):
                for  in self.tiles[column]:
                    if tile == 0:


        elif direction == DOWN:
            pass
        elif direction == LEFT:
            pass
        elif direction == RIGHT:
            pass

    def new_tile(self):
        """
        Create a new tile in a randomly selected empty
        square.  The tile should be 2 90% of the time and
        4 10% of the time.
        """
        possible_tiles = [2]*9
        possible_tiles.append(4)
        row = random.randint(0, self.get_grid_height() - 1)
        col = random.randint(0, self.get_grid_width() - 1)
        while self.tiles[row][col] != 0:
            row = random.randint(0, self.get_grid_height() - 1)
            col = random.randint(0, self.get_grid_width() - 1)
        self.tiles[row][col] = random.choice(possible_tiles)



    def set_tile(self, row, col, value):
        """
        Set the tile at position row, col to have the given value.
        """
        self.tiles[row][col] = value

    def get_tile(self, row, col):
        """
        Return the value of the tile at position row, col.
        """
        return self.tiles[row][col]


# poc_2048_gui.run_gui(TwentyFortyEight(4, 4))
