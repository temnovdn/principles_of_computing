from game_2048 import TwentyFortyEight

game = TwentyFortyEight(4, 5)

print(game.get_grid_height(), game.get_grid_width())

print(game.__str__())

game.reset()

print(game.__str__())