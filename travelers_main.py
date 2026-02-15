import os
import math
import shlex


def load_towns(path):
    """Simple function to load the list of towns from a text file."""
    dir = "../traveler_project/data"
    full_path = os.path.join(dir, path)
    if os.path.exists(full_path):
        with open(full_path, "r") as file:
            contents = file.read().splitlines()  # creating a list of 'Town, X, Y'
            town_details = [
                tuple(shlex.split(line)) for line in contents if line.strip()
            ]  # convertint the string 'Town X, Y' into a tuple ('Town, X, Y')
            return town_details
    else:
        raise FileNotFoundError(f"Missing file: {path}")


def distance(townA, townB):
    """Calculate Euclidean Distance Between 2 towns and return the result"""

    x1, y1 = float(townA[1]), float(townA[2])  # Get the X, Y coords for town A
    x2, y2 = float(townB[1]), float(townB[2])  # Get the X, Y coords for town B

    result = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

    return round(result, 5)


def itinenary_greedy(towns):
    """Determine the order to visit all the the towns in the list based on the shorted distance"""
    # step 0: remove Paris from the list
    # step 1: calculate the distance between Paris and every other town
    # step 2: pick the smallest distance and that will be the next town
    # step 4: remove the current town in the list
    # repeat step 1 to 4
    itinerary = []
    current_town = towns.pop(0)
    itinerary.append((current_town[0], 0))

    while towns:
        distances = []
        for i in range(len(towns)):
            d = distance(current_town, towns[i])
            distances.append((i, d))

        # Find the shortest the distance between the current town and the next one based on the list of towns
        closest_town_details = min(distances, key=lambda x: x[1])

        closest_town_index = closest_town_details[0]
        closest_town_distance = closest_town_details[1]
        current_town = towns.pop(closest_town_index)
        itinerary.append((current_town, closest_town_distance))

    return itinerary


def total_distance(itinerary):
    """Caluclate the total distance traveled based on the heuristic itinerary."""
    total = 0

    total_distance_traveled = sum(i[1] for i in itinerary)

    return total_distance_traveled


if "__name__" == "__main__":
    # Load towns once and reuse
    towns = load_towns("towns.txt")

    # Calculate distance between first two towns
    distance(towns[0], towns[1])

    # Compute itinerary once and reuse
    itinerary = itinenary_greedy(towns)

    # Calculate total distance
    total_distance(itinerary)
