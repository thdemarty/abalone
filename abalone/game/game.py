import os
from game.player import Player
from game.board import Board


class Abalone:
    """The class to represent the game of Abalone"""

    def __init__(self, board=None, starting_player: Player = Player.B):
        self.current_player = starting_player
        self.board: Board = Board(board)
        self.history = []

    def is_game_over(self):
        """Check if the game is over"""
        black_marbles = self.board.get_player_marbles(Player.B)
        white_marbles = self.board.get_player_marbles(Player.W)
        return len(black_marbles) == 8 or len(white_marbles) == 8

    def get_scoreboard(self):
        """Get the scoreboard of the game"""
        scoreboard = {Player.B: 0, Player.W: 0}
        black_marbles = self.board.get_player_marbles(Player.B)
        white_marbles = self.board.get_player_marbles(Player.W)
        scoreboard[Player.B] = len(black_marbles)
        scoreboard[Player.W] = len(white_marbles)
        return scoreboard

    def get_winner(self):
        scoreboard = self.get_scoreboard()
        # return the player with the most marbles
        return max(scoreboard, key=scoreboard.get)

    def get_legal_moves(self, player):
        return self.board.get_legal_moves(player)

    def switch_player(self):
        self.current_player = Player.W if self.current_player == Player.B else Player.B

    def display_scoreboard(self):
        scoreboard = self.get_scoreboard()
        scoreboard_str = """
 ┏━━━━━━━━━━━━━━━━━┓
 ┃ ⚫ {0:<2}  |  {1:>2} ⚪ ┃
 ┗━━━━━━━━━━━━━━━━━┛
        """.format(scoreboard[Player.B], scoreboard[Player.W])

        return scoreboard_str

    def run(self, black, white, display=True, max_moves=-1):
        """Run the game of Abalone"""
        # if max_moves is -1 then the game will run until the game is over
        # otherwise, the game will run until max_moves is reached
        if max_moves == -1:
            # Infinite loop until the game is over
            while not self.is_game_over():    
                if display:
                    os.system("clear")
                    print(len(self.history), "moves")
                    print(self.display_scoreboard())
                    print(self)
                
                move = (
                    black.play(self, self.history)
                    if self.current_player == Player.B
                    else white.play(self, self.history)
                )
                
                self.board.move(self.current_player, move)
                self.history.append(move)
                self.switch_player()

        else:
            # max_moves is defined
            while not self.is_game_over() and len(self.history) < max_moves:
                if display:
                    os.system("clear")
                    print(len(self.history), "moves")
                    print(self.display_scoreboard())
                    print(self)
                
                move = (
                    black.play(self, self.history)
                    if self.current_player == Player.B
                    else white.play(self, self.history)
                )
                
                self.board.move(self.current_player, move)
                self.history.append(self.board)
                self.switch_player()

        if display:
            print(self)
            print(f"Game over! The winner is {self.get_winner()}")
            print("In", len(self.history), "moves")


    def __str__(self):
        return str(self.board)
