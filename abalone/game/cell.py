from enum import Enum

class Cell(Enum):
    _ = 0  # Empty
    B = 1  # Black
    W = 2  # White
    X = -1 # Out of board (not a cell)

    def __str__(self):
        if self == Cell._:
            return "⭕"
        elif self == Cell.B:
            return "⚫"
        elif self == Cell.W:
            return "⚪"
        else:
            return "❌"
        
    def __repr__(self) -> str:
        return self.name