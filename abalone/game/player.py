from enum import Enum


class Player(Enum):
    B = 1 # Black player
    W = 2 # White player

    def __repr__(self) -> str:
        return '⚫' if self == Player.B else '⚪'
    
    def __str__(self):
        return self.__repr__()