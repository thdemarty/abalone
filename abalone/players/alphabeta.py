# Third-party imports
import random

# import inquirer
from copy import deepcopy

# Local imports
from game.game import Abalone
from game.player import Player

from players.abstract import AbstractPlayer


# Constants
CUTOFF_DEPTH = 3
WEIGHTS_SIZE = 6


class AlphaBetaPlayer(AbstractPlayer):
    def __init__(self, weights = None):
        if weights:
            self.weights = weights
        else:
            self.weights = [random.uniform(-1, 1) for _ in range(WEIGHTS_SIZE)]
        super().__init__()
        

    def play(self, game: Abalone, history):
        ab = AlphaBeta(self.weights)
        player = game.current_player

        best_move = ab.get_best_move(game, player)

        # score = ab.evaluate(game, player)
        
        # inquirer.confirm("")
        return best_move


class AlphaBeta:
    """Alpha-Beta algorithm (minimax with alpha-beta prunning)."""

    def __init__(self, weights):
        self.alpha = float("-inf")
        self.beta = float("inf")
        self.best_move = None
        self.best_score = None
        self.weights = weights

        
    def get_best_move(self, game: Abalone, player):
        if player == Player.B:
            self.best_score = float("-inf")
            for move in game.get_legal_moves(player):
                new_game = deepcopy(game)
                new_game.board.move(Player.B, move)
                score = self.alphabeta(new_game, self.alpha, self.beta, CUTOFF_DEPTH)
                # print(score, game.board.board)
                if score > self.best_score:
                    self.best_score = score
                    self.best_move = move
            
        else:
            self.best_score = float("inf")
            for move in game.get_legal_moves(player):
                new_game = deepcopy(game)
                new_game.board.move(Player.W, move)
                score = self.alphabeta(new_game, self.alpha, self.beta, CUTOFF_DEPTH)
                # print(score, game.board.board)
                if score < self.best_score:
                    self.best_score = score
                    self.best_move = move
        
        return self.best_move
        

    def alphabeta(self, game: Abalone, alpha, beta, depth):
        if game.is_game_over() or depth == CUTOFF_DEPTH:
            return self.evaluate(game, game.current_player)
        
        else:
            if game.current_player == Player.W:
                value = float("inf")
                for move in game.get_legal_moves():
                    new_game = deepcopy(game)
                    new_game.board.move(Player.W, move)
                    value = min(value, self.alphabeta(new_game, alpha, beta, depth - 1))
                    if value <= alpha:
                        return value
                    beta = min(beta, value)
            else:
                value = float("-inf")
                for move in game.get_legal_moves():
                    new_game = deepcopy(game)
                    new_game.board.move(Player.B, move)
                    value = max(value, self.alphabeta(new_game, alpha, beta, depth - 1))
                    if value >= beta:
                        return value
                    alpha = max(alpha, value)
        
        return value

    
    def evaluate(self, game: Abalone, player):
        # if game.is_game_over():
        #    return float("inf") if game.get_winner() == player else float("-inf")

        opponent = Player.B if player == Player.W else Player.W
        res = (
            - self.weights[0] * AlphaBeta.evaluate_distance_to_center(game, player)
            - self.weights[1] * AlphaBeta.evaluate_marbles_out(game, player)
            - self.weights[5] * AlphaBeta.evaluate_density_score(game, player)
            + self.weights[2] * AlphaBeta.evaluate_distance_to_center(game, opponent)
            + self.weights[3] * AlphaBeta.evaluate_distance_to_center(game, opponent)
            + self.weights[4] * AlphaBeta.evaluate_marbles_out(game, opponent)
        )

        return res

    @staticmethod
    def evaluate_distance_to_center(game: Abalone, player: Player):
        center = (4, 4)
        player_marbles = game.board.get_player_marbles(player)
        mean_distance = 0

        for marble in player_marbles:
            mean_distance += game.board.get_distance_between(marble, center)

        return mean_distance / len(player_marbles)

    @staticmethod
    def evaluate_density_score(game: Abalone, player: Player):
        """Evaluate the density for marbles of a player"""

        player_marbles = game.board.get_player_marbles(player)
        density_score = 0

        # Evaluate the density for each marble
        for marble in player_marbles:
            density_score += game.board.get_local_density_score(player, marble)

        return density_score / len(player_marbles)

    @staticmethod
    def evaluate_marbles_out(game: Abalone, player: Player):
        """Give the number of marbles out of the board."""
        scoreboard = game.get_scoreboard()
        return 14 - scoreboard[player]
