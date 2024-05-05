import random
import sys
import datetime
from tqdm import tqdm

from game.game import Abalone
from players.alphabeta import AlphaBetaPlayer
from game.player import Player
# from matplotlib import pyplot as plt


# Equivalent to 4 games (4 game of 2 players each so 8 players in total)
POPULATION_SIZE = 2*5
MAX_GENERATIONS = 1000
# To avoid infinite games where no one wins
MAX_MOVES_IN_GAME = 250

# The population size must be even since we will have 2 players for each game
assert POPULATION_SIZE % 2 == 0

def train(weights=None):
    # Weights can be passed as an argument to train the model from already existing weights
    # If no weights are passed, the model will be trained from scratch (random weights)
    
    generation_id = 0
    
    
    if not weights:
        population_weights = [[random.uniform(-1, 1) for _ in range(6)] for _ in range(POPULATION_SIZE)]
    
    else:
        # With a bit of noise
        print("Training from existing weights")
        print("Initial weights ", end="")
        print (["{0:0.2f}".format(w) for w in weights])
        population_weights = [weights for _ in range(POPULATION_SIZE)]
        population_weights[0] = weights # Keep the best weights from the previous generation

    while generation_id < MAX_GENERATIONS:
        # Launch multiple games of Abalone
        results = []
        best_scores_over_generation = [] # A list to store the best score of each generation
        
        print("\n************ Generation", generation_id, "************\n")
        
        # TODO: parallelize the launch of the games
        for i in tqdm(range(0, POPULATION_SIZE, 2)):
            
            # Initialize the players with weights
            black = AlphaBetaPlayer(population_weights[i])
            white = AlphaBetaPlayer(population_weights[i+1])
            
            game = Abalone()

            game.run(black, white, display=False, max_moves=MAX_MOVES_IN_GAME)
            winner = game.get_winner()
            weights = black.weights if winner == Player.B else white.weights
            # Get weights of the winner
            print(len(game.history))
            # rewards the player that won a game in a minimum number of moves
            # The score takes in account the player that have the most marbles in the smallest number of moves
            model_score = game.get_scoreboard()[winner] / len(game.history)
            results.append((weights, model_score))

        
            
        # Handle the weights of the evaluation function
        # And regenerate weights with the best weights (genetic algorithm)    
        results.sort(key=lambda x: x[1], reverse=True)
        best_weights = results[0][0]
        print("Generation best weights ", end="")
        print (["{0:0.2f}".format(w) for w in best_weights])
        print("Generation best_score", results[0][1])
        best_scores_over_generation.append(results[0][1])

        # Save the best weights to a file
        
        # current date and time
        now = datetime.datetime.now()

        with open(f"{now.isoformat()}_weights_G{generation_id}.txt", "w") as f:
            f.write(",".join([str(weight) for weight in best_weights]))



        # ========= Genetic Algorithm =========
        # Mutation of the weights
        



        for i in range(POPULATION_SIZE):
            # Create weights that are a bit different from the best weights
            # A pounderation is added to the weights with the best score
            population_weights[i] = [weight + random.uniform(-0.5, 0.5) for weight in best_weights]
            
        # Keep the best weights from the previous generation to next generation to
        # make sure we don't lose the best score
        population_weights[0] = best_weights
        # ========= End of Genetic Algorithm =========
        generation_id += 1

    # Plot the evolution of the best score
    # plt.plot(best_scores_over_generation)




if __name__ == "__main__":
    if len(sys.argv) == 2:
        # A path to a weights file can be passed as an argument
        # A weight file contains the weights of the evaluation function separated by commas
        weights_file = sys.argv[1]
        with open(weights_file, "r") as f:
            weights = [float(weight) for weight in f.read().split(",")]
        train(weights)
    else:
        # Train from scratch
        train()
        