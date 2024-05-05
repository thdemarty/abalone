import random

from players.abstract import AbstractPlayer


class RandomPlayer(AbstractPlayer):
    """ A random player that picks a random move among the possible ones. """
    def play(self, game, history):
        legal_moves = game.get_legal_moves(game.current_player)
        # ask for confirmation
        # inquirer.confirm("Press Enter to continue")
        return random.choice(legal_moves)



