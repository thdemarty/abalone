# Abalone
A simplified implementation of the Abalone game (no broadside move) with implementation of AI (MinMax, MinMax with alpha-beta prunning, etc.)

> This repository is a semester project as part of the AI for games course.

## Getting started
To install the project on your computer, you will have to create a virtual environment with python-venv with the following command:

```bash
python3 -m venv env
```

To position yourself into the virtualenv run the command `source venv env`:

The following step is to install all required dependencies that are listed into the file `requirements.txt`. To install those, run the following command:

```bash
pip install -r requirements.txt
```

To launch a game you need to run the following command:

```bash
python play.py
```

If you want to train the weights of the evaluations functions, run the following command:

```bash
python train.py
```

## Explanation
### The game
#### The board

The first problem encountered was how the board should be implemented. Indeed, in [Abalone](https://en.wikipedia.org/wiki/Abalone_(board_game)), the game board is hexagonal, so the possible displacements are tricky to modelise. 

I successfully implement it by realising that an hexagonal board is just a stretched squared matrix (See the illustration below).

![board modelisation](<docs/img/board.png>)

Each cell has a value representing the state of the board. There are 4 different states which are :
* The cell is empty : `value=0`
* The cell contains a marble from player black : `value=1`
* The cell contains a marble from player white : `value=2`
* The cell is out of board : `value=-1`


Thus, the above configuration which is the default configuration when we start a new game, is equivalent to the following two-dimensions array :


```python
board = [
  [-1, -1, -1, -1,  2,  2,  2,  2,  2],
  [-1, -1, -1,  2,  2,  2,  2,  2,  2],
  [-1, -1,  0,  0,  0,  2,  2,  2,  0],
  [-1,  0,  0,  0,  0,  0,  0,  0,  0],
  [ 0,  0,  0,  0,  0,  0,  0,  0,  0],
  [ 0,  0,  0,  0,  0,  0,  0,  0, -1],
  [ 0,  0,  1,  1,  1,  0,  0, -1, -1],
  [ 1,  1,  1,  1,  1,  1, -1, -1, -1],
  [ 1,  1,  1,  1,  1, -1, -1, -1, -1],
 ]
```

#### Move directions

We just have seen that our hexagonal board could be seen as a stretched matrix. But to really see the board as hexagonal, we need to constraint the displacements along the possible directions.

On an hexagonal grid, we can only move to the following directions:
* North-Est (NE)
* North-West (NW)
* West (W)
* Est (E)
* South-Est (SE)
* South-West (SW)

But we need to know to which directions we associate which unit vectors (and be careful with the grid orientation).

To know that, we construct the following table that gives us the direction and makes us easy to compute unit vectors (be careful with the axes)

```
                    ┏━━━━┳━━━━┳━━━━┓
                    ┃ ❌ ┃ NW ┃ NE ┃
                    ┣━━━━╋━━━━╋━━━━┫
                  x ┃ W  ┃ ⚫ ┃  E ┃
                  ↓ ┣━━━━╋━━━━╋━━━━┫
                    ┃ SW ┃ SE ┃ ❌ ┃
                    ┗━━━━┻━━━━┻━━━━┛
                           y →
```

We get the following vectors associated with each directions:
* $NE = (-1,  1)$
* $SE = ( 1,  0)$
* $SW = ( 1, -1)$
* $NW = (-1,  0)$
* $W =  ( 0, -1)$
* $E =  ( 0,  1)$

### Artificial intelligence

For this project, i decided to do a MinMax algorithm with alpha-beta prunning. The implementation was pretty easy (see inside players [alphabeta.py](/abalone/players/alphabeta.py))


#### Evaluation functions

There are 3 evaluations functions in this program used to evaluate a state of the game (the board). Each of the functions described below are weightened by a weight that a genetic algorithm will try to optimize.

##### Distance to center
The first one is the easiest one. It computes for the player given in parameters the distance to the center cell (in the default layout, this is the cell E5). The return value is the average distance of all the marbles for the player given.

##### Density
The second one is a bit more complicated. It returns the average density of the marbles of the player. The density for a marble is the sum of the distance of all other marbles of the player divided by the number of marbles of the player. The sum of the density for each marble is then divided by the number of marbles remaining for the player given.

##### Remaining marbles
The third one is a little more easy than the previous one. Indeed, it gives for the player the number of its marbles that have been pushed out of the board. 

#### Genetic algorithm
As it was said earlier, each of the evaluation functions are weightened. The Genetic Algorithm (GA) have to "mutate" the weights in order to get the best weight that make the best AI. For each generation, it takes the best score of the best individual in the generation that defeats its opponent in a minimum of move (We are taking in account the size of the move to evaluate each individual of a generation). 

Then the algorithm "mutate" by implementing a bit of noise to the best weight and adding to next generation mutated best weights from previous generation and the best_weights of the previous generation to check if there is any downgrade of performance across the generations.

### Going further
#### Create a better human interface
The testing was really painful since the human player interface is really not convenient to play with. I should have develop a __real__ human interface.

#### Missing a offensive heuristic
The Alpha-Beta MinMax player is too defensive for the current version. It is totally normal though since there are no heuristics that rewards an offensive behavior yet. This took me a long time to figure out a heuristic but unfortunately I never manage to go beyond the thought state...

#### Transition tables
If I had more time for this project, I would have done a sort of transition table (_cache_ for evaluation function) to avoid re-computing everytime each states when we already had evaluated it. I did try something in [cache.py](/abalone/players/cache.py) but I never succeded to implement it.

#### Genetic algorithm
In the current version, the genetic algorithm is not well implemented. Between each generation, it takes the best weights from the previous generation and add a random value between -0.5 and +0.5 (uniformely). I never implemented anything related to "crossovers" as many genetic algorithm implementation had implemented. This is something i could maybe explore if I have more time. I could also implement instead the _Cross-Entropy Method_ (CEM) as in the tetris example gave to us.


