class TT:
    """ Simple implementation of a transposition table """
    def __init__(self):
        self.moves = dict()

    def store(self, depth, state, move, score):
        """ Store in the transposition table """
        if state not in self.moves:
            # Create a new entry
            self.moves[state] = dict()

        self.moves[state][depth] = (move, score)


    def lookup(self, depth, state):
        """ 
        Perform a lookup in the transposition table.
        Returns:
            * 0 if the state is not found in the table, and give `None` for 
                    the best move and score
            * 1 if the state is found, but not at the given depth, but still
                    give the best move and score for the highest depth
            * 2 if the state is found at the given depth, and give the best 
                    move and score
        """
        
        if state in self.moves:
            # State already stored
            if depth in self.moves[state]:
                # Depth already stored
                return 2, self.moves[state][depth][0], self.moves[state][depth][1] 
            else:
                # State not found for this depth => return False, but still give best move, with its associated score
                depths = [d for d in self.moves[state].keys()]

                if len(depths) == 0:
                    # No entries at all
                    return 0, None, None
                
                max_depth = max(depths)

                return 1, self.moves[state][max_depth][0], self.moves[state][max_depth][1]
            
        return 0, None, None