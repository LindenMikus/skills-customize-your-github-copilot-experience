import heapq

# Each edge stores a neighboring location and the walking time in minutes.
SCHOOL_MAP = {
    "Main Entrance": [("Office", 2), ("Library", 4)],
    "Office": [("Main Entrance", 2), ("Room 101", 3)],
    "Library": [("Main Entrance", 4), ("Room 204", 1), ("Cafeteria", 5)],
    "Room 101": [("Office", 3), ("Science Lab", 4)],
    "Room 204": [("Library", 1), ("Science Lab", 2)],
    "Science Lab": [("Room 101", 4), ("Room 204", 2), ("Gym", 3)],
    "Cafeteria": [("Library", 5), ("Gym", 2)],
    "Gym": [("Cafeteria", 2), ("Science Lab", 3)],
}


def get_neighbors(location):
    """Return the locations directly connected to location."""
    # TODO: Return the neighboring locations and walking times.
    pass


def shortest_paths(start):
    """Return the shortest distance from start to every school location."""
    # TODO: Initialize distances and use a priority queue for Dijkstra's algorithm.
    pass


def find_route(start, destination):
    """Return the shortest route and its total walking time."""
    # TODO: Track predecessors while calculating distances, then rebuild the route.
    pass


def recommend_destination(start, destinations):
    """Return the closest reachable destination and its travel time."""
    # TODO: Compare shortest-path results for the possible destinations.
    pass


if __name__ == "__main__":
    # TODO: Add calls that demonstrate at least three routes.
    route, minutes = find_route("Main Entrance", "Gym")
    print(" -> ".join(route))
    print(f"Total walking time: {minutes} minutes")
