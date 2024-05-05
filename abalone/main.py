from game.board import Board
from game.configs import load_config_from_file
from game.player import Player
from game.direction import Direction
from game.utils import format_move

def print_board(board):
    for row in board.board:
        print(row)

if __name__ == "__main__":
    config = load_config_from_file("tests/sandbox.txt")
    board = Board(config) 
    player = Player.W

    e4 = board.get_xy_from_name("E", 4)
    e6 = board.get_xy_from_name("E", 6)

    print_board(board)

    # Move E5 in direction E
    board.move_sideway((e4, e6), Direction.NW)

    print_board(board)
