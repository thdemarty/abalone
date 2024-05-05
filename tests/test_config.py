from unittest import TestCase

from abalone.game.configs import load_config_from_file
from abalone.game.cell import Cell

class ConfigTest(TestCase):
    def test_load_config_from_file(self):
        config = load_config_from_file("boilerplate.txt")
        
        expected_config = [
            [Cell.X, Cell.X, Cell.X, Cell.X, Cell.B, Cell.B, Cell.B, Cell.B, Cell.B],
            [Cell.X, Cell.X, Cell.X, Cell.B, Cell.B, Cell.B, Cell.B, Cell.B, Cell.B],
            [Cell.X, Cell.X, Cell._, Cell._, Cell.B, Cell.B, Cell.B, Cell._, Cell._],
            [Cell.X, Cell._, Cell._, Cell._, Cell._, Cell._, Cell._, Cell._, Cell._],
            [Cell._, Cell._, Cell._, Cell._, Cell._, Cell._, Cell._, Cell._, Cell._],
            [Cell._, Cell._, Cell._, Cell._, Cell._, Cell._, Cell._, Cell._, Cell.X],
            [Cell._, Cell._, Cell.W, Cell.W, Cell.W, Cell._, Cell._, Cell.X, Cell.X],
            [Cell.W, Cell.W, Cell.W, Cell.W, Cell.W, Cell.W, Cell.X, Cell.X, Cell.X],
            [Cell.W, Cell.W, Cell.W, Cell.W, Cell.W, Cell.X, Cell.X, Cell.X, Cell.X],
        ]
        
        self.assertEqual(config, expected_config)
