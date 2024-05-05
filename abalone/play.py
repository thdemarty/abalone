# Third-party imports
import inquirer
# Local imports
from game.game import Abalone
from players.random import RandomPlayer
from players.alphabeta import AlphaBetaPlayer
from players.human import HumanPlayer

""" Launch a GUI game of Abalone """

# Ask for type of player for black 
questions = [
    inquirer.List('black',
                    message="Choose the type of player for black",
                    choices=['Random', 'AlphaBeta', 'Human'],
                    ),
    inquirer.List('white',
                    message="Choose the type of player for white",
                    choices=['Random', 'AlphaBeta', 'Human'],
                    ),
]

def get_weights():
    use_weights = inquirer.prompt([
        inquirer.List("use_weights", "Weights selection", 
                      choices=["Import weights from file", "Random weights"]),
    ])["use_weights"]

    if use_weights == "Random weights":
        return None
    while True:
        # While the user does not select a valid file
        try:
            file_path = inquirer.prompt([
                inquirer.Text("file_path", "Enter the path to the weights file")
            ])["file_path"]
            with open(file_path, "r") as f:
                # The file contains weights (float) separated by a comma
                weights = [float(weight) for weight in f.read().split(",")]
                break
        except FileNotFoundError:
            print("File not found")
    
    print("Weights loaded successfully from file.")
    print("Here is the loaded weights: ", [round(weight, 2) for weight in weights])
    # load the weights from the file


answers = inquirer.prompt(questions)

black_type = answers['black']
white_type = answers['white']


if black_type == 'Random':
    black = RandomPlayer()

if white_type == 'Random':
    white = RandomPlayer()

if black_type == 'AlphaBeta':
    weights = get_weights()
    if weights is not None:
        black = AlphaBetaPlayer(weights=weights)
    black = AlphaBetaPlayer()

if white_type == 'AlphaBeta':
    weights = get_weights()
    if weights is not None:
        white = AlphaBetaPlayer(weights=weights)
    white = AlphaBetaPlayer()

if black_type == 'Human':
    black = HumanPlayer()

if white_type == 'Human':
    white = HumanPlayer()

# Ask to launch the game
launch = inquirer.prompt([
    inquirer.List("launch", 
    message="Do you want to launch the game?",
    choices=["Yes", "No"],)])["launch"]

if launch == "No":
    exit()

# Launch the game
game = Abalone()

game.run(black, white, display=True, max_moves=-1)



