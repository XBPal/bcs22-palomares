"""
Explanation for Each Variable:
paths - list: holds all the possible paths and their respective weights
start - string: the starting point in the map
end - string: the ending point in the map
distances - dictionary: holds the shortest distances from the start point to endpoint
    pointA - current location
    pointB - next location
    weight - distance between current location to next location
distances[start] - sets the value of the distance from the starting location to 0
pQueue - list: stores tuple containing the current distance and current point in a format of (distance, currentPoint)
previousPoint - dictionary: used to track the previous point that leads to the current point in the shortest path.
current_distance - string: stores the value of weight when going from pointA to pointB
current_point - string: stores the value of the current point
"""

# Import heap queue, a priority queue algorithm
import heapq

"""CODES INSIDE THE FUNCTION"""
# Function: Find the shortest distance and path
def short_path(paths, start, end):
    distances = {pointB: float('inf') for pointA, pointB, weight in paths}
    distances[start] = 0

    pQueue = [(0, start)]
    previousPoint = {pointB: None for pointA, pointB, weight in paths}

    while pQueue:
        current_distance, current_point = heapq.heappop(pQueue)

        if current_distance > distances[current_point]:
            continue

        for pointA, pointB, weight in paths:
            if pointA == current_point:
                distance = current_distance + weight

                if distance < distances[pointB]:
                    distances[pointB] = distance
                    heapq.heappush(pQueue, (distance, pointB))
                    previousPoint[pointB] = current_point

    shortest_path = []
    while end:
        shortest_path.insert(0, end)
        end = previousPoint[end]

    return distances, shortest_path


"""CODES OUTSIDE THE FUNCTION"""
# List: Represent each weighted paths of the map
paths = [
    ("Home", "Store A", 7),
    ("Home", "Store B", 14),
    ("Home", "Intersection", 25),
    ("Store A", "Home", 7),
    ("Store A", "Store B", 5),
    ("Store B", "School", 7),
    ("School", "Intersection", 7),
    ("Intersection", "School", 7)
]

# List: Represents each location of the map
locations = ["Home", "Store A", "Store B", "School", "Intersection"]

# First Loop: Asks the user where is the starting point
while True:
    print("LOCATIONS: Home, Store A, Store B, School, Intersection")
    start_point = input("Where is your starting point: ")

    # First If-Else: If the user-input is inside the list "locations", proceed to ask the endpoint.
    if start_point in locations:
        # Second Loop: Asks the user where is the endpoint.
        while True:
            end_point = input("Where do you want to go: ")

            # Second If-Else: If the user-input is inside the list "locations", the loop is broken.
            if end_point in locations:
                break
            # Second If-Else: If the user-input does not exist inside the list "locations", print an error message and repeat the loop.
            else:
                print("Invalid endpoint. Please type another location.")

        # Loop:
        break
    # First If-Else: If the user-input does not exist inside the list "locations", print an error message and repeat the loop.
    else:
        print("Invalid starting point. Please type another location.")

# Function Call: Calls the function "short_path" and gives the values of variables "paths", "start_point", and "end_point"
shortest_distance, shortest_path = short_path(paths, start_point, end_point)

# Print: After running the function "short_path", the shortest path is displayed in the console.
print("======== RESULT ========")

# Outer If-Else: Check if the list "shortest_path" only holds 1 element (meaning, a path does not exist from start_point to endpoint)
if len(shortest_path) == 1:

    # Inner If-Else: Check if the value of start_point and endpoint is the same.
    if start_point == end_point:
        print("Shortest Distance:", 0)
        print("Shortest Path:", start_point)
    else:
        print("Invalid path. Please try again.")

# Outer If-Else: If the list "shortest_path" holds more than 1 element, there exists a path from start_point to endpoint
else:
    print("Shortest Distance:", shortest_distance[end_point])
    print("Shortest Path:", shortest_path)