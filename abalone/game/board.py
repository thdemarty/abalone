from typing import Tuple

from game.cell import Cell
from game.player import Player
from game.direction import Direction


class Board:
    def __init__(self, board=None):
        self.board = board if board is not None else self.initialize()

    def __eq__(self, other: object) -> bool:
        # Check if the other object is an instance of the Board class
        if not isinstance(other, Board):
            return False

        return self.board == other.board

    def __str__(self):
        board_str = ""
        prefixes = ["    I ", "   H ", "  G ", " F ", "E ", " D ", "  C ", "   B ", "    A "]
        for i, row in enumerate(self.board):
            board_str += prefixes[i]
            
            for cell in row:
                if cell == Cell.X:
                    continue
                board_str += str(cell)
            if i > 4:
                board_str += " " + str(9 + 4 - i + 1)
            
            
            board_str += "\n"
            
        board_str += "       1 2 3 4 5"
        return board_str

    def get_xy_from_name(self, letter, digit):
        """Get the cell according to the official coordinates system"""
        letters = ["I", "H", "G", "F", "E", "D", "C", "B", "A"]

        # Check if position asked is valid
        assert 1 <= digit <= 9
        assert letter in letters

        x = letters.index(letter)
        y = digit - 1

        return (x, y)

    def get_name_from_xy(self, x, y):
        """Get the official coordinates system from the cell"""
        letters = ["I", "H", "G", "F", "E", "D", "C", "B", "A"]

        # Check if position asked is valid
        assert 0 <= x <= 8
        assert 0 <= y <= 8

        return f"{letters[x]}{y + 1}"

    def get_cell_from_coord(self, letter, digit):
        return self.get_cell(*self.get_xy_from_name(letter, digit))

    def get_cell(self, x, y):
        if x < 0 or x >= len(self.board) or y < 0 or y >= len(self.board[0]):
            return Cell.X

        return self.board[x][y]

    def get_neighbors_from_xy(self, x, y):
        """Get the neighbors of a cell"""
        neighbors = []
        for dir in Direction:
            (dx, dy) = dir.value
            (nx, ny) = (x + dx, y + dy)
            if self.get_cell(nx, ny).value != Cell.X.value:
                neighbors.append((nx, ny))
        return neighbors

    def get_neighbors_xy_from_coord(self, letter, digit):
        """Get the xy coordinates of neighbors of a cell"""
        neighbors = []
        (x, y) = self.get_xy_from_name(letter, digit)
        for dir in Direction:
            (dx, dy) = dir.value
            (nx, ny) = (x + dx, y + dy)
            if self.get_cell(nx, ny).value != Cell.X.value:
                neighbors.append((nx, ny))
        return neighbors

    def get_neighbor_xy_dir(self, cell_coord, direction):
        """Get the xy coordinates of a neighbor of a cell in a specific direction"""
        (x, y) = cell_coord
        (dx, dy) = direction.value
        (nx, ny) = (x + dx, y + dy)
        return (nx, ny)

    def initialize(self):
        return [
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

    def get_player_marbles(self, player: Player):
        """Get the coordinates of all the marbles of a player"""
        marbles = []
        for i, row in enumerate(self.board):
            for j, cell in enumerate(row):
                if cell.value == player.value:
                    marbles.append((i, j))

        return marbles

    def get_line_to_edge(self, scell_coord, direction):
        """Get the xy of cells from scell_coord to the edge in a direction"""

        if self.get_cell(*scell_coord).value == Cell.X.value:
            raise Exception("Could not get line to edge from a cell outside the board")

        line = [scell_coord]

        while self.get_cell(*line[-1]).value != Cell.X.value:
            ncell_coord = self.get_neighbor_xy_dir(line[-1], direction)
            line.append(ncell_coord)

        line.pop()  # remove the cell outside the board

        return line

    def set_marble(self, xy_coord, cell_value: Cell):
        """Set a new value to a cell"""
        (x, y) = xy_coord
        self.board[x][y] = cell_value

    def get_stack_of_3_own_marbles(self, player: Player):
        stacks = set()

        for cell in self.get_player_marbles(player):
            for n1 in self.get_neighbors_from_xy(*cell):
                if self.get_cell(*n1).value == player.value and n1 != cell:
                    if (n1, cell) not in stacks or (cell, n1) not in stacks:
                        cells = sorted([cell, n1])

                        stacks.add(tuple(cells))

                for n2 in self.get_neighbors_from_xy(*n1):
                    if (
                        self.get_cell(*n2).value == player.value
                        and n2 != n1
                        and n2 != cell
                    ):
                        if (n2, cell) not in stacks or (cell, n2) not in stacks:
                            cells = sorted([cell, n2])
                            stacks.add(tuple(cells))

        return list(stacks)

    def get_num_marble_line(self, player, line):
        """Count the number of each player marbles involved in a line"""
        not_in_turn: Player = Player.B if player == Player.W else Player.W

        own_marbles = 0
        while (
            own_marbles < len(line)
            and self.get_cell(*line[own_marbles]).value == player.value
        ):
            own_marbles += 1
        opp_marbles = 0
        while (
            own_marbles + opp_marbles < len(line)
            and self.get_cell(*line[own_marbles + opp_marbles]).value
            == not_in_turn.value
        ):
            opp_marbles += 1

        return own_marbles, opp_marbles

    def get_distance_between(self, cell1, cell2):
        """Get the distance between two cells"""
        return max(
            abs(cell1[0] - cell2[0]),
            abs(cell1[1] - cell2[1]),
            abs(cell1[0] - cell2[0] + cell1[1] - cell2[1]),
        )

    # ******** Move functions ********

    def get_all_sideway_moves(self, player: Player):
        """Get all the possible sideway moves for a player"""
        moves = set()
        for stack in self.get_stack_of_3_own_marbles(player):
            for direction in Direction:
                if self.check_sideway_move(player, *stack, direction):
                    moves.add((stack, direction))

        return list(moves)

    def get_all_inline_moves(self, player: Player):
        """Get all the possible inline moves for a player"""
        moves = []
        for marble_xy in self.get_player_marbles(player):
            for direction in Direction:
                if self.check_inline_move(player, marble_xy, direction):
                    moves.append((marble_xy, direction))
        return moves

    def check_inline_move(self, player, pusher, direction) -> bool:
        """Check if an inline move is valid"""
        (x, y) = pusher
        (dx, dy) = direction.value
        mp = self.get_cell(x, y)

        if mp.value != player.value:
            return False

        (x1, y1) = (x + dx, y + dy)
        c1 = self.get_cell(x1, y1)

        if c1.value == Cell.X.value:
            return False

        elif c1.value == Cell._.value:
            return True

        elif c1.value == player.value:
            (x2, y2) = (x1 + dx, y1 + dy)
            c2 = self.get_cell(x2, y2)

            if c2.value == Cell.X.value:
                # Move the m1 outside the board
                return False

            elif c2.value == Cell._.value:
                return True

            elif c2.value == player.value:
                # Handle sumito with 3 marbles (p, c1, c2) are of the player

                (x3, y3) = (x2 + dx, y2 + dy)
                c3 = self.get_cell(x3, y3)

                if c3.value == Cell.X.value:
                    # Can't push the c2 outside the board
                    return False

                elif c3.value == Cell._.value:
                    return True

                elif c3.value == player.value:
                    return False

                else:
                    # c3 is a marble of the opponents
                    (x4, y4) = (x3 + dx, y3 + dy)
                    c4 = self.get_cell(x4, y4)

                    if c4.value == Cell.X.value or c4.value == Cell._.value:
                        return True
                    elif c4.value == player.value:
                        return False
                    else:
                        # (p, c1, c2) are of the player
                        # (c3, c4) are of the opponent
                        (x5, y5) = (x4 + dx, y4 + dy)
                        c5 = self.get_cell(x5, y5)

                        if c5.value == Cell.X.value or c5.value == Cell._.value:
                            return True
                        else:
                            return False
            else:
                # c2 is a marble of the opponent
                (x3, y3) = (x2 + dx, y2 + dy)
                c3 = self.get_cell(x3, y3)
                if c3.value == Cell.X.value or c3.value == Cell._.value:
                    return True
                elif c3.value == player.value:
                    return False
                else:
                    # c3 is a marble of the opponent : can't push
                    return False
        else:
            # c1 is a marble of the opponent
            # Since a single marble can't be involved
            # in a sumito, the move is invalid
            return False

    def get_cells_between(self, scell_coord, ecell_coord):
        """
        Return the list of cells coordinates between two coordinates and the direction needed.
        if it is possible, else return None None
        """
        cells = []  # result list

        if (
            self.get_cell(*scell_coord).value == Cell.X.value
            or self.get_cell(*ecell_coord).value == Cell.X.value
        ):
            raise Exception(
                "Could not get cells between two cells if one of them is outside the board"
            )

        for direction in Direction:
            cells = [scell_coord]
            while self.get_cell(*cells[-1]).value != Cell.X.value:
                ncell_coord = self.get_neighbor_xy_dir(cells[-1], direction)
                cells.append(ncell_coord)
                if ncell_coord == ecell_coord:
                    return cells, direction

        return None, None

    def check_sideway_move(self, player, scell_coord, ecell_coord, direction) -> bool:
        """Check if a sideway move is valid"""

        (cells, dir) = self.get_cells_between(scell_coord, ecell_coord)
        (dx, dy) = direction.value

        if cells is None:
            return False

        if len(cells) > 3 or len(cells) < 2:
            # A sideway move with 1 cell is an inline move...
            return False

        for cell_coord in cells:
            cell = self.get_cell(*cell_coord)
            if cell.value != player.value:
                return False  # if cells are not of the player, this is invalid

            # Destination cell for the cell handled
            dcell_coord = self.get_neighbor_xy_dir(cell_coord, direction)
            dcell = self.get_cell(*dcell_coord)

            # check if the cell + direction is valid (for ALL cells)
            if dcell.value != Cell._.value:
                return False

        return True

    def get_legal_moves(self, player: Player):
        """Get all the legal moves for a player"""
        return self.get_all_inline_moves(player) + self.get_all_sideway_moves(player)

    def move(self, player, move):
        """Move a marble according to a move"""
        (cells, direction) = move
        if isinstance(cells[0], int):
            self.move_inline(player, cells, direction)
        else:
            self.move_sideway(cells, direction)

    def move_marble(self, marble, direction):
        """A utility function to move the marble in a direction"""
        (x, y) = marble
        (dx, dy) = direction.value
        # Get cell value
        ccell = self.get_cell(x, y)
        # Move the marble by updating the board
        self.board[x][y] = Cell._
        self.board[x + dx][y + dy] = ccell

    def move_inline(self, player: Player, pusher: Tuple[int], direction: Direction):
        """Perform an inline move"""
        # We suppose that the move is valid here (fixme later)
        line = self.get_line_to_edge(pusher, direction)

        own_marbles, opp_marbles = self.get_num_marble_line(player, line)

        own_marble_color = Cell.B if player == Player.B else Cell.W
        opp_marble_color = Cell.W if player == Player.B else Cell.B

        # Move final marble involved in the move to destination cell
        dest = self.get_neighbor_xy_dir(line[own_marbles + opp_marbles - 1], direction)
        if self.get_cell(*dest).value != Cell.X.value:
            self.set_marble(dest, opp_marble_color)

        self.set_marble(line[own_marbles], own_marble_color)
        self.set_marble(pusher, Cell._)

    def move_sideway(self, boundaries, direction):
        """Perform a sideway move"""
        cells, _ = self.get_cells_between(boundaries[0], boundaries[1])

        for cell in cells:
            self.move_marble(cell, direction)

    def get_local_density_score(self, player, marble):
        """Evaluate the density for a marble"""
        local_density = 0
        player_marbles = self.get_player_marbles(player)

        for cell in player_marbles:
            if cell != marble:
                local_density += self.get_distance_between(cell, marble)

        return local_density / len(player_marbles)
