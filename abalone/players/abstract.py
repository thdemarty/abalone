from abc import abstractmethod
from game.game import Abalone


class AbstractPlayer:

    @abstractmethod
    def play(self, board: Abalone, history):
        """ Abstract method that returns the move to perform."""
    