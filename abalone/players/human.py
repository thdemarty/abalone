# Third-party imports
import inquirer

# Local imports
from players.abstract import AbstractPlayer
from game.game import Abalone
from game.board import Board
from game.direction import Direction

def format_marble(marble_coord, board: Board):
    return board.get_name_from_xy(*marble_coord)


class HumanPlayer(AbstractPlayer):
    """A human implementation of a player"""
    def play(self, game: Abalone, history):
        # Ask for the move type
        move_type = inquirer.prompt([
            inquirer.List("move_type", 
            message="Type of move",
            choices=["inline", "sideways"],)])["move_type"]    
        # Ask for marble 1
        marble1_candidate = set()
        if move_type == "inline":
            message = "Select the pusher"
            for move in game.get_legal_moves(game.current_player):
                
                if isinstance(move[0][0], int):
                    marble1_candidate.add(move[0])
        else:
            message = "Select one of the marbles in the stack to move"
            for move in game.get_legal_moves(game.current_player):
                if isinstance(move[0][0], tuple):
                    marble1_candidate.add(move[0][0])
                    marble1_candidate.add(move[0][1])
        marble1_candidate = list(map(lambda coord: format_marble(coord, game.board), marble1_candidate))
        marble1_candidate.sort()

        marble1 = inquirer.prompt([
            inquirer.List("marble1", message=message, choices=marble1_candidate, carousel=True)
        ])['marble1']

        marble1 = (game.board.get_xy_from_name(marble1[0], int(marble1[1])))
                   
        # Ask for marble 2 if the move is sideways
        if move_type == "sideways":
            marble2_candidate = set()
            for move in game.get_legal_moves(game.current_player):
                if isinstance(move[0][0], tuple):
                    # print(marble1, move[0][0], move[0][1])
                    if move[0][0] == marble1:
                        marble2_candidate.add(move[0][1])
                    if move[0][1] == marble1:
                        marble2_candidate.add(move[0][0])

            marble2_candidate = list(map(lambda coord: format_marble(coord, game.board), marble2_candidate))
            marble2_candidate.sort()

            marble2 = inquirer.prompt([
                inquirer.List("marble2", message="Select the second marble", choices=marble2_candidate, carousel=True)
            ])['marble2']

        # Construct the marbles in the move
        if move_type == "inline":
            marbles = marble1
        else:
            marble2_coord = game.board.get_xy_from_name(marble2[0], int(marble2[1]))
            marbles = (marble1, marble2_coord)
            

        # Ask for the direction
        directions_candidate = set()
        
        for move in game.get_legal_moves(game.current_player):
            

            if isinstance(move[0][0], tuple):
                # print("This a sideways move")
                # print(marbles, move[0][0], move[0][1])
                if marbles[0] == move[0][0] and marbles[1] == move[0][1]:
                    directions_candidate.add(move[1])
            elif marbles == move[0]:
                directions_candidate.add(move[1])
                

        directions_candidate = list(map(lambda direction: direction, directions_candidate))
        # directions_candidate.sort()


        direction = inquirer.prompt([
            inquirer.List("direction", message="Select the direction", choices=directions_candidate, carousel=True)
        ])['direction']
        
        # Get the direction direction corresponding to the tuple vector in Direction enum
        direction = Direction._value2member_map_[direction]
        

        return (marbles, direction)