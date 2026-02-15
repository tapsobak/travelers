from travelers_main import *

# Load towns once
towns_loaded = load_towns("towns.txt")

# Display towns
print("List of Towns and X & Y Coords Below!!!\n")
print(towns_loaded)
print(f"\nTotal numbers of towns: {len(towns_loaded)}")

# Calculate and display distance between first two towns
dist = distance(towns_loaded[0], towns_loaded[1])
print(
    f"\nEuclidean Distance between {towns_loaded[0][0]} and {towns_loaded[1][0]} is: {dist}"
)

# Calculate itinerary once
print("\nItinerary based on the distance of the closest next town!!!")
itinerary = itinenary_greedy(towns_loaded)
print(itinerary)

# Calculate and display total distance
total_dist = total_distance(itinerary)
print(f"\nTotal Distance Traveled: {total_dist} units.")
