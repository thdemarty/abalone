from game.cell import Cell

def get_coord_from_xy(x, y):
    """Get the official coordinates system from the cell"""
    letters = ["I", "H", "G", "F", "E", "D", "C", "B", "A"]
    return (letters[x], y + 1)


def format_inline_move(move):
    """ Display an inline move in a human readable format """
    (pusher, direction) = move
    (letter, digit) = get_coord_from_xy(*pusher)
    return (f"{letter}{digit}", direction)

def format_sideway_move(move):
    """ Display a sideway move in a human readable format """
    (stack_boundaries, direction) = move
    (m1_coord, m2_coord) = stack_boundaries
    (letter1, digit1) = get_coord_from_xy(*m1_coord)
    (letter2, digit2) = get_coord_from_xy(*m2_coord)
    
    return (f"{letter1}{digit1}-{letter2}{digit2}", direction)


def format_move(move):
    (marbles, direction) = move
    if isinstance(marbles[0], int):
        return format_inline_move(move)
    else:
        return format_sideway_move(move)