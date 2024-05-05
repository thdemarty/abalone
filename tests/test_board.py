from unittest import TestCase

from abalone.game.board import Board
from abalone.game.cell import Cell
from abalone.game.configs import load_config_from_file
from abalone.game.direction import Direction
# from game.player import Player


class BoardTest(TestCase):
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

    @classmethod
    def tearDownClass(cls):
        pass

    def test_initial_layout(self):
        board = Board()

        expected_board = [
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

        self.assertListEqual(board.board, expected_board)

    def test_get_xy_from_coord(self):
        board = Board()

        self.assertRaises(AssertionError, board.get_xy_from_name, "A", 0)
        self.assertRaises(AssertionError, board.get_xy_from_name, "J", 1)
        self.assertRaises(AssertionError, board.get_xy_from_name, "A", 10)
        self.assertTupleEqual(self.a1, (8, 0))
        self.assertTupleEqual(self.i9, (0, 8))
        self.assertTupleEqual(self.e5, (4, 4))

    def test_get_neighbors_xy(self):
        board = Board()

        # Cell A1
        expected = sorted([(8, 1), (7, 0), (7, 1)])
        self.assertListEqual(
            sorted(board.get_neighbors_xy_from_coord("A", 1)), expected
        )

        # Cell E5
        expected = sorted([(4, 3), (3, 4), (3, 5), (4, 5), (5, 4), (5, 3)])
        self.assertListEqual(
            sorted(board.get_neighbors_xy_from_coord("E", 5)), expected
        )

        # Cell I9
        expected = sorted([(0, 7), (1, 7), (1, 8)])
        self.assertListEqual(
            sorted(board.get_neighbors_xy_from_coord("I", 9)), expected
        )

        # Cell C7
        expected = sorted([(7, 5), (6, 5), (5, 6), (5, 7)])
        self.assertListEqual(
            sorted(board.get_neighbors_xy_from_coord("C", 7)), expected
        )

        # Cell I7
        expected = sorted([(0, 5), (0, 7), (1, 6), (1, 5)])
        self.assertListEqual(
            sorted(board.get_neighbors_xy_from_coord("I", 7)), expected
        )

    def test_get_marbles_of_player(self):
        config = load_config_from_file("boilerplate.txt")
        board = Board(config)  # noqa

        # TODO fill this test

    def test_get_cells_between(self):
        config = load_config_from_file("boilerplate.txt")
        board = Board(config)

        # get cells between A1 and A5
        expected = ([(8, 0), (8, 1), (8, 2), (8, 3), (8, 4)], Direction.E)
        self.assertTupleEqual(expected, board.get_cells_between(self.a1, self.a5))

        # get cells between e5 and i9
        expected = ([(4, 4), (3, 5), (2, 6), (1, 7), (0, 8)], Direction.NE)
        self.assertTupleEqual(expected, board.get_cells_between(self.e5, self.i9))

        # get cells between c7 and g3 (Not valid)
        expected = (None, None)
        self.assertTupleEqual(expected, board.get_cells_between(self.c7, self.g3))

        # get cells between e5 and out of board
        out = (0, 0)
        self.assertRaises(Exception, board.get_cells_between, self.e5, out)

    def test_get_line_to_edge(self):
        """ Test get line to edge from a cell in a given direction """
        config = load_config_from_file("boilerplate.txt")
        board = Board(config)

        # get line to edge from E5 in direction NW
        expected = [(4, 4), (3, 4), (2, 4), (1, 4), (0, 4)]
        self.assertListEqual(expected, board.get_line_to_edge(self.e5, Direction.NW))
        
        # get line to edge from E5 in direction NE
        expected = [(4, 4), (3, 5), (2, 6), (1, 7), (0, 8)]
        self.assertListEqual(expected, board.get_line_to_edge(self.e5, Direction.NE))
        
        # get line to edge from E5 in direction E
        expected = [(4, 4), (4, 5), (4, 6), (4, 7), (4, 8)]
        self.assertListEqual(expected, board.get_line_to_edge(self.e5, Direction.E))
        
        # get line to edge from E5 in direction SE
        expected = [(4, 4), (5, 4), (6, 4), (7, 4), (8, 4)]
        self.assertListEqual(expected, board.get_line_to_edge(self.e5, Direction.SE))

        # get line to edge from E5 in direction SW
        expected = [(4, 4), (5, 3), (6, 2), (7, 1), (8, 0)]
        self.assertListEqual(expected, board.get_line_to_edge(self.e5, Direction.SW))
        
        # get line to edge from E5 in direction W
        expected = [(4, 4), (4, 3), (4, 2), (4, 1), (4, 0)]
        self.assertListEqual(expected, board.get_line_to_edge(self.e5, Direction.W))

    def test_get_distance_between(self):
        config = load_config_from_file("boilerplate.txt")
        board = Board(config)

        # get distance between A1 and A5
        expected = 4
        self.assertEqual(expected, board.get_distance_between(self.a1, self.a5))

        # get distance between e5 and i9
        expected = 4
        self.assertEqual(expected, board.get_distance_between(self.e5, self.i9))

        # get distance between c7 and g3
        expected = 8
        self.assertEqual(expected, board.get_distance_between(self.c7, self.g3))
