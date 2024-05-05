# File handling the starting/testing configuration of the game
# Imports/Exports etc.
# Creation of configurations via gui
from game.cell import Cell
import pathlib

CONFIG_DIR = pathlib.Path(__file__).parent.parent.parent / "configs"

def load_config_from_file(file_name):
    """ Load a configuration from file """
    prefixes = [4, 3, 2, 1, 0, 0, 0, 0, 0]
    suffixes = [0, 0, 0, 0, 0, 1, 2, 3, 4]
    config = []
    with open(CONFIG_DIR / file_name, "r") as file:
        lines = file.readlines()
        for i, line in enumerate(lines):
            line = line.strip()

            if line == []:
                continue
            config_row = []

            # Adding the left padding 
            for _ in range(prefixes[i]):
                config_row.append(Cell.X)

            for char in list(line):
                if char == "⭕":
                    config_row.append(Cell._)
                elif char == "⚫":
                    config_row.append(Cell.B)
                elif char == "⚪":
                    config_row.append(Cell.W)

            # Adding the right padding
            for _ in range(suffixes[i]):
                config_row.append(Cell.X)

            config.append(config_row)

    return config
        







