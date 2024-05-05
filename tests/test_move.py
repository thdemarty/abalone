from unittest import TestCase

from abalone.game.configs import load_config_from_file
from abalone.game.board import Board
from abalone.game.player import Player
from abalone.game.direction import Direction
from abalone.game.cell import Cell


class MoveTestCase(TestCase):
    @classmethod
    def setUpClass(cls):
        board = Board()
        cls.a1 = board.get_xy_from_name("A", 1)
        cls.a2 = board.get_xy_from_name("A", 2)
        cls.a3 = board.get_xy_from_name("A", 3)
        cls.a4 = board.get_xy_from_name("A", 4)
        cls.a5 = board.get_xy_from_name("A", 5)

        cls.b1 = board.get_xy_from_name("B", 1)
        cls.b2 = board.get_xy_from_name("B", 2)
        cls.b3 = board.get_xy_from_name("B", 3)
        cls.b4 = board.get_xy_from_name("B", 4)
        cls.b5 = board.get_xy_from_name("B", 5)
        cls.b6 = board.get_xy_from_name("B", 6)

        cls.c1 = board.get_xy_from_name("C", 1)
        cls.c2 = board.get_xy_from_name("C", 2)
        cls.c3 = board.get_xy_from_name("C", 3)
        cls.c4 = board.get_xy_from_name("C", 4)
        cls.c5 = board.get_xy_from_name("C", 5)
        cls.c6 = board.get_xy_from_name("C", 6)
        cls.c7 = board.get_xy_from_name("C", 7)

        cls.d1 = board.get_xy_from_name("D", 1)
        cls.d2 = board.get_xy_from_name("D", 2)
        cls.d3 = board.get_xy_from_name("D", 3)
        cls.d4 = board.get_xy_from_name("D", 4)
        cls.d5 = board.get_xy_from_name("D", 5)
        cls.d6 = board.get_xy_from_name("D", 6)
        cls.d7 = board.get_xy_from_name("D", 7)
        cls.d8 = board.get_xy_from_name("D", 8)

        cls.e1 = board.get_xy_from_name("E", 1)
        cls.e2 = board.get_xy_from_name("E", 2)
        cls.e3 = board.get_xy_from_name("E", 3)
        cls.e4 = board.get_xy_from_name("E", 4)
        cls.e5 = board.get_xy_from_name("E", 5)
        cls.e6 = board.get_xy_from_name("E", 6)
        cls.e7 = board.get_xy_from_name("E", 7)
        cls.e8 = board.get_xy_from_name("E", 8)
        cls.e9 = board.get_xy_from_name("E", 9)

        cls.f2 = board.get_xy_from_name("F", 2)
        cls.f3 = board.get_xy_from_name("F", 3)
        cls.f4 = board.get_xy_from_name("F", 4)
        cls.f5 = board.get_xy_from_name("F", 5)
        cls.f6 = board.get_xy_from_name("F", 6)
        cls.f7 = board.get_xy_from_name("F", 7)
        cls.f8 = board.get_xy_from_name("F", 8)
        cls.f9 = board.get_xy_from_name("F", 9)

        cls.g3 = board.get_xy_from_name("G", 3)
        cls.g4 = board.get_xy_from_name("G", 4)
        cls.g5 = board.get_xy_from_name("G", 5)
        cls.g6 = board.get_xy_from_name("G", 6)
        cls.g7 = board.get_xy_from_name("G", 7)
        cls.g8 = board.get_xy_from_name("G", 8)
        cls.g9 = board.get_xy_from_name("G", 9)

        cls.h4 = board.get_xy_from_name("H", 4)
        cls.h5 = board.get_xy_from_name("H", 5)
        cls.h6 = board.get_xy_from_name("H", 6)
        cls.h7 = board.get_xy_from_name("H", 7)
        cls.h8 = board.get_xy_from_name("H", 8)
        cls.h9 = board.get_xy_from_name("H", 9)

        cls.i5 = board.get_xy_from_name("I", 5)
        cls.i6 = board.get_xy_from_name("I", 6)
        cls.i7 = board.get_xy_from_name("I", 7)
        cls.i8 = board.get_xy_from_name("I", 8)
        cls.i9 = board.get_xy_from_name("I", 9)

    def test_check_inline_move(self):
        config = load_config_from_file("tests/check_inline_move.txt")
        board = Board(config)
        player = Player.W

        # Check inline move of E5 in direction whatever -> False
        pusher = board.get_xy_from_name("E", 5)
        direction = Direction.E
        self.assertFalse(board.check_inline_move(player, pusher, direction))

        # Check inline move of A1 in direction NE -> False (Passed)
        pusher = board.get_xy_from_name("A", 1)
        direction = Direction.NE
        self.assertFalse(board.check_inline_move(player, pusher, direction))

        # Check inline move of A3 in direction NW -> True (Failed)

        pusher = board.get_xy_from_name("A", 3)
        direction = Direction.NW
        self.assertTrue(board.check_inline_move(player, pusher, direction))

        # Check inline move of B2 in direction E  -> False
        pusher = board.get_xy_from_name("B", 2)
        direction = Direction.E
        self.assertFalse(board.check_inline_move(player, pusher, direction))

        # Check inline move of B2 in direction SE -> False

        pusher = board.get_xy_from_name("B", 2)
        direction = Direction.NE
        self.assertFalse(board.check_inline_move(player, pusher, direction))

        # Check inline move of B3 in direction W -> True
        pusher = board.get_xy_from_name("B", 3)
        direction = Direction.W
        self.assertTrue(board.check_inline_move(player, pusher, direction))

    def test_get_all_inline_moves(self):
        config = load_config_from_file("tests/get_all_inline_moves.txt")
        board = Board(config)

        d4 = board.get_xy_from_name("D", 4)
        e4 = board.get_xy_from_name("E", 4)
        e5 = board.get_xy_from_name("E", 5)
        e6 = board.get_xy_from_name("E", 6)
        e7 = board.get_xy_from_name("E", 7)
        f6 = board.get_xy_from_name("F", 6)

        expected = {
            (d4, Direction.NW),
            (e4, Direction.NW),
            (e4, Direction.SE),
            (e5, Direction.SW),
            (e6, Direction.W),
            (e7, Direction.NE),
            (f6, Direction.SW),
        }

        self.assertSetEqual(set(board.get_all_inline_moves(Player.W)), expected)

    def test_check_sideway_move(self):
        # TODO pls
        pass

    def test_get_all_sideway_moves(self):
        # TODO pls
        pass

    def test_move_inline(self):
        player = Player.W

        # Case H0 : Move E5 in direction E
        config = load_config_from_file("tests/inline_moves/3h0.txt")
        board = Board(config)
        expected_board = [
            [Cell.X, Cell.X, Cell.X, Cell.X, Cell._, Cell._, Cell._, Cell._, Cell._],
            [Cell.X, Cell.X, Cell.X, Cell._, Cell._, Cell._, Cell._, Cell._, Cell._],
            [Cell.X, Cell.X, Cell._, Cell._, Cell._, Cell._, Cell._, Cell._, Cell._],
            [Cell.X, Cell._, Cell._, Cell._, Cell._, Cell._, Cell._, Cell._, Cell._],
            [Cell._, Cell._, Cell._, Cell.W, Cell._, Cell.W, Cell.W, Cell._, Cell._],
            [Cell._, Cell._, Cell._, Cell._, Cell._, Cell._, Cell._, Cell._, Cell.X],
            [Cell._, Cell._, Cell._, Cell._, Cell._, Cell._, Cell._, Cell.X, Cell.X],
            [Cell._, Cell._, Cell._, Cell._, Cell._, Cell._, Cell.X, Cell.X, Cell.X],
            [Cell._, Cell._, Cell._, Cell._, Cell._, Cell.X, Cell.X, Cell.X, Cell.X],
        ]

        board.move_inline(player, self.e5, Direction.E)
        self.assertListEqual(board.board, expected_board)

        # Case H1 : Move E5 in direction E
        config = load_config_from_file("tests/inline_moves/3h1.txt")
        board = Board(config)
        expected_board = [
            [Cell.X, Cell.X, Cell.X, Cell.X, Cell._, Cell._, Cell._, Cell._, Cell._],
            [Cell.X, Cell.X, Cell.X, Cell._, Cell._, Cell._, Cell._, Cell._, Cell._],
            [Cell.X, Cell.X, Cell._, Cell._, Cell._, Cell._, Cell._, Cell._, Cell._],
            [Cell.X, Cell._, Cell._, Cell._, Cell._, Cell._, Cell._, Cell._, Cell._],
            [Cell._, Cell._, Cell._, Cell._, Cell._, Cell.W, Cell.W, Cell.W, Cell.B],
            [Cell._, Cell._, Cell._, Cell._, Cell._, Cell._, Cell._, Cell._, Cell.X],
            [Cell._, Cell._, Cell._, Cell._, Cell._, Cell._, Cell._, Cell.X, Cell.X],
            [Cell._, Cell._, Cell._, Cell._, Cell._, Cell._, Cell.X, Cell.X, Cell.X],
            [Cell._, Cell._, Cell._, Cell._, Cell._, Cell.X, Cell.X, Cell.X, Cell.X],
        ]

        board.move_inline(player, self.e5, Direction.E)
        self.assertListEqual(board.board, expected_board)

        # Case H2 : Move E5 in direction E
        config = load_config_from_file("tests/inline_moves/3h2.txt")
        board = Board(config)
        expected_board = [
            [Cell.X, Cell.X, Cell.X, Cell.X, Cell._, Cell._, Cell._, Cell._, Cell._],
            [Cell.X, Cell.X, Cell.X, Cell._, Cell._, Cell._, Cell._, Cell._, Cell._],
            [Cell.X, Cell.X, Cell._, Cell._, Cell._, Cell._, Cell._, Cell._, Cell._],
            [Cell.X, Cell._, Cell._, Cell._, Cell._, Cell._, Cell._, Cell._, Cell._],
            [Cell._, Cell._, Cell._, Cell._, Cell._, Cell.W, Cell.W, Cell.W, Cell.B],
            [Cell._, Cell._, Cell._, Cell._, Cell._, Cell._, Cell._, Cell._, Cell.X],
            [Cell._, Cell._, Cell._, Cell._, Cell._, Cell._, Cell._, Cell.X, Cell.X],
            [Cell._, Cell._, Cell._, Cell._, Cell._, Cell._, Cell.X, Cell.X, Cell.X],
            [Cell._, Cell._, Cell._, Cell._, Cell._, Cell.X, Cell.X, Cell.X, Cell.X],
        ]

        board.move_inline(player, self.e5, Direction.E)
        self.assertListEqual(board.board, expected_board)

        # Case D0 : Move E5 in direction SW
        config = load_config_from_file("tests/inline_moves/3d0.txt")
        board = Board(config)
        expected_board = [
            [Cell.X, Cell.X, Cell.X, Cell.X, Cell._, Cell._, Cell._, Cell._, Cell._],
            [Cell.X, Cell.X, Cell.X, Cell._, Cell._, Cell._, Cell._, Cell._, Cell._],
            [Cell.X, Cell.X, Cell._, Cell._, Cell._, Cell._, Cell._, Cell._, Cell._],
            [Cell.X, Cell._, Cell._, Cell._, Cell._, Cell.W, Cell._, Cell._, Cell._],
            [Cell._, Cell._, Cell._, Cell._, Cell._, Cell._, Cell._, Cell._, Cell._],
            [Cell._, Cell._, Cell._, Cell.W, Cell._, Cell._, Cell._, Cell._, Cell.X],
            [Cell._, Cell._, Cell.W, Cell._, Cell._, Cell._, Cell._, Cell.X, Cell.X],
            [Cell._, Cell._, Cell._, Cell._, Cell._, Cell._, Cell.X, Cell.X, Cell.X],
            [Cell._, Cell._, Cell._, Cell._, Cell._, Cell.X, Cell.X, Cell.X, Cell.X],
        ]

        board.move_inline(player, self.e5, Direction.SW)
        self.assertListEqual(board.board, expected_board)

        # Case D1 : Move E5 in direction SW
        config = load_config_from_file("tests/inline_moves/3d1.txt")
        board = Board(config)
        expected_board = [
            [Cell.X, Cell.X, Cell.X, Cell.X, Cell._, Cell._, Cell._, Cell._, Cell._],
            [Cell.X, Cell.X, Cell.X, Cell._, Cell._, Cell._, Cell._, Cell._, Cell._],
            [Cell.X, Cell.X, Cell._, Cell._, Cell._, Cell._, Cell._, Cell._, Cell._],
            [Cell.X, Cell._, Cell._, Cell._, Cell._, Cell._, Cell._, Cell._, Cell._],
            [Cell._, Cell._, Cell._, Cell._, Cell._, Cell._, Cell._, Cell._, Cell._],
            [Cell._, Cell._, Cell._, Cell.W, Cell._, Cell._, Cell._, Cell._, Cell.X],
            [Cell._, Cell._, Cell.W, Cell._, Cell._, Cell._, Cell._, Cell.X, Cell.X],
            [Cell._, Cell.W, Cell._, Cell._, Cell._, Cell._, Cell.X, Cell.X, Cell.X],
            [Cell.B, Cell._, Cell._, Cell._, Cell._, Cell.X, Cell.X, Cell.X, Cell.X],
        ]

        board.move_inline(player, self.e5, Direction.SW)
        self.assertListEqual(board.board, expected_board)

        # Case D2 : Move E5 in direction SW
        config = load_config_from_file("tests/inline_moves/3d2.txt")
        board = Board(config)
        expected_board = [
            [Cell.X, Cell.X, Cell.X, Cell.X, Cell._, Cell._, Cell._, Cell._, Cell._],
            [Cell.X, Cell.X, Cell.X, Cell._, Cell._, Cell._, Cell._, Cell._, Cell._],
            [Cell.X, Cell.X, Cell._, Cell._, Cell._, Cell._, Cell._, Cell._, Cell._],
            [Cell.X, Cell._, Cell._, Cell._, Cell._, Cell._, Cell._, Cell._, Cell._],
            [Cell._, Cell._, Cell._, Cell._, Cell._, Cell._, Cell._, Cell._, Cell._],
            [Cell._, Cell._, Cell._, Cell.W, Cell._, Cell._, Cell._, Cell._, Cell.X],
            [Cell._, Cell._, Cell.W, Cell._, Cell._, Cell._, Cell._, Cell.X, Cell.X],
            [Cell._, Cell.W, Cell._, Cell._, Cell._, Cell._, Cell.X, Cell.X, Cell.X],
            [Cell.B, Cell._, Cell._, Cell._, Cell._, Cell.X, Cell.X, Cell.X, Cell.X],
        ]

        board.move_inline(player, self.e5, Direction.SW)
        self.assertListEqual(board.board, expected_board)

    def test_move_sideway(self):
        """ Test if the sideway move is working correctly """
        
        # test sideway move E4 - E5 - E6 to direction NW
        config = load_config_from_file("tests/sideway_moves/3h.txt")
        board = Board(config)

        expected_board = [
            [Cell.X, Cell.X, Cell.X, Cell.X, Cell._, Cell._, Cell._, Cell._, Cell._],
            [Cell.X, Cell.X, Cell.X, Cell._, Cell._, Cell._, Cell._, Cell._, Cell._],
            [Cell.X, Cell.X, Cell._, Cell._, Cell._, Cell._, Cell._, Cell._, Cell._],
            [Cell.X, Cell._, Cell._, Cell.W, Cell.W, Cell.W, Cell._, Cell._, Cell._],
            [Cell._, Cell._, Cell._, Cell._, Cell._, Cell._, Cell._, Cell._, Cell._],
            [Cell._, Cell._, Cell._, Cell._, Cell._, Cell._, Cell._, Cell._, Cell.X],
            [Cell._, Cell._, Cell._, Cell._, Cell._, Cell._, Cell._, Cell.X, Cell.X],
            [Cell._, Cell._, Cell._, Cell._, Cell._, Cell._, Cell.X, Cell.X, Cell.X],
            [Cell._, Cell._, Cell._, Cell._, Cell._, Cell.X, Cell.X, Cell.X, Cell.X],
        ]
        board.move_sideway((self.e4, self.e6), Direction.NW)
        self.assertListEqual(board.board, expected_board)

