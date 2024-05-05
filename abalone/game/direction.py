from enum import Enum

class Direction(Enum):
    """ 
    The direction and its associated vector.
    To understand the vectors, consider reading the README.md
    """
    NE = (-1,  1) 
    SE = ( 1,  0)
    SW = ( 1, -1)
    NW = (-1,  0)
    W =  ( 0, -1)
    E =  ( 0,  1)

    def __str__(self):
        return self.name
    
    def __repr__(self) -> str:
        return self.name

