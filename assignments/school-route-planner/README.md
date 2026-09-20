# 📘 Assignment: School Route Planner

## 🎯 Objective

Model the school as a weighted graph and build a route planner that finds the shortest walking route between classrooms. You will practice graph representations, priority queues, Dijkstra's algorithm, and explaining algorithm results to users.

## 📝 Tasks

### 🛠️ Represent the School Map

#### Description

Study the starter map and represent each hallway connection as a weighted edge. Complete the helper function so the program can list the classrooms directly connected to a location along with the walking time in minutes.

#### Requirements
Completed program should:

- Represent every classroom and hallway connection in the provided map
- Treat each hallway connection as bidirectional
- Implement `get_neighbors(location)`
- Return neighboring locations with their walking times
- Handle an unknown location with a clear error or empty result


### 🛠️ Implement Dijkstra's Algorithm

#### Description

Implement `shortest_paths(start)` using Dijkstra's algorithm. The function should calculate the smallest known walking time from the starting location to every reachable location.

Use a priority queue so the next location processed is always the one with the smallest currently known distance. The graph contains only non-negative edge weights, which is a requirement for Dijkstra's algorithm.

#### Requirements
Completed program should:

- Initialize the start location with distance `0`
- Represent locations that have not been reached with an appropriate initial distance
- Use a priority queue to process locations in increasing distance order
- Relax edges when a shorter route is discovered
- Return the shortest known distance to every location


### 🛠️ Reconstruct and Display a Route

#### Description

Extend the algorithm to remember each location's predecessor. Implement `find_route(start, destination)` so it returns both the ordered list of locations and the total walking time.

For example, a successful route should be displayed in a form similar to:

```text
Library -> Room 204 -> Science Lab -> Gym
Total walking time: 6 minutes
```

#### Requirements
Completed program should:

- Return locations in travel order from start to destination
- Return the total walking time for the shortest route
- Report when the destination is unknown or unreachable
- Avoid reversing or skipping locations in the final route
- Demonstrate at least three different start and destination pairs


### 🛠️ Compare Route Choices

#### Description

Add a route comparison feature that accepts several possible destinations and recommends the closest one from a chosen starting location. Use the shortest-path results rather than comparing direct hallway connections only.

This is the stretch portion of the assignment. Explain in a short comment or paragraph why a direct connection is not always the fastest route.

#### Requirements
Completed program should:

- Accept a starting location and a collection of possible destinations
- Recommend the destination with the lowest total walking time
- Handle ties consistently and explain the tie-breaking rule
- Handle destinations that cannot be reached
- Explain why weighted graph algorithms are useful for route planning
