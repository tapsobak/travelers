from travelers_main import *

towns_loaded = load_towns("towns.txt")
print("List of Towns and X & Y Coords Below!!!\n")
print(towns_loaded)
print(f"\nTotal numbers of towns: {len(towns_loaded)}")
print(
    f"\nEuclian Distance between {towns_loaded[0][0]} and {towns_loaded[1][0]} is: {distance(towns_loaded[0], towns_loaded[1])}"
)

print("Itinerary based on the distance of the closest next town!!!")
print(itinenary_greedy(load_towns("towns.txt")))
