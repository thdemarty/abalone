# Third-party imports
from unittest import TestCase

# Local imports
from abalone.game.configs import load_config_from_file
from abalone.game.game import Abalone
from abalone.game.player import Player
from abalone.players.alphabeta import AlphaBeta


class EvaluationTestCase(TestCase):
    """ Test case for the evaluation functions """

    def test_evaluate_distance_to_center(self):
        # Default configuration
        board = load_config_from_file("boilerplate.txt")
        game = Abalone(board)
        player = Player.W

        minmax = AlphaBeta(game)
        expected = 3.28571428
        score = minmax.evaluate_distance_to_center(game, player)
        self.assertAlmostEqual(expected, score)
        
        # Other configuration with marble of player at the center
        board = load_config_from_file("tests/distance_to_center.txt")
        game = Abalone(board)
        player = Player.W

        minmax = AlphaBeta(game)
        expected = 0
        score = minmax.evaluate_distance_to_center(game, player)
        self.assertAlmostEqual(expected, score)
 