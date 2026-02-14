import os
import math


def load_towns(path):
    """Simple function to load the list of towns from a text file."""
    dir = "../traveler_project/data"
    full_path = os.path.join(dir, path)
    if os.path.exists(full_path):
        with open(full_path, "r") as file:
            contents = file.read().splitlines()  # creating a list of 'Town, X, Y'
            town_details = [
                tuple(content.split()) for content in contents
            ]  # convertint the string 'Town X, Y' into a tuple ('Town, X, Y')
            return town_details
    else:
        raise FileNotFoundError(f"Missing file: {path}")


def distance(townA, townB):
    """Calculate Euclidean Distance Between 2 towns and return the result"""

    x1, y1 = float(townA[1]), float(townA[2])  # Get the X, Y coords for town A
    x2, y2 = float(townB[1]), float(townB[2])  # Get the X, Y coords for town B

    result = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

    return round(result, 3)


if "__name__" == "__main__":
    load_towns("towns.txt")
    distance(load_towns("towns.txt")[0], load_towns("towns.txt")[1])
