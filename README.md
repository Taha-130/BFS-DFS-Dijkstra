# Pathfinding Algorithms

This repository contains various pathfinding algorithms implemented in Python. The algorithms included are designed to find the shortest path between nodes in a graph. The project features classic algorithms like Dijkstra, as well as other search algorithms, with different approaches to optimize performance.

## Algorithms Included

1. **Dijkstra Algorithm (`dijkstra.py`)**  
   This algorithm finds the shortest path between nodes in a graph, using a greedy approach.

2. **Dijkstra with Weights (`dijkstra_avec_poids.py`)**  
   An enhanced version of Dijkstra that considers edge weights for finding the shortest path.

3. **Dijkstra with Priority Queue (`dijkstra_avec_tas.py`)**  
   This version of Dijkstra utilizes a priority queue (min-heap) for faster performance, improving efficiency compared to the basic implementation.

4. **Breadth-First Search (`largeur.py`)**  
   A graph traversal algorithm that explores all possible paths level by level. It guarantees the shortest path in unweighted graphs.

5. **Depth-First Search (`profondeur.py`)**  
   A graph traversal algorithm that explores as far as possible along a branch before backtracking. It is not guaranteed to find the shortest path.

6. **Neighborhood Search (`voisinage.py`)**  
   Implements a neighborhood search technique, useful for heuristic or local search algorithms like A*.

## Prerequisites

- Python 3.x

## Installation

Clone the repository to your local machine:

```bash
git clone https://github.com/your-user/pathfinding-algorithms.git
cd pathfinding-algorithms
```

Make sure Python 3 is installed on your machine. You can check by running:

```bash
python3 --version
```

## Running the Algorithms
Each file contains a specific implementation of a pathfinding algorithm. You can run the respective script to test the algorithm.

For example, to run the Dijkstra algorithm, execute:

```bash
python3 dijkstra.py
```

## Example Usage
Below is an example of how to use the algorithms:

# Example: Running Dijkstra algorithm

```bash
import dijkstra

graph = {
    'A': {'B': 1, 'C': 4},
    'B': {'A': 1, 'C': 2, 'D': 5},
    'C': {'A': 4, 'B': 2, 'D': 1},
    'D': {'B': 5, 'C': 1}
}

shortest_path = dijkstra.find_shortest_path(graph, 'A', 'D')
print(shortest_path)
```

## Description of Each Algorithm
Dijkstra: Finds the shortest path in a graph by exploring the nodes and selecting the node with the smallest tentative distance.
Dijkstra with Weights: Extends the basic Dijkstra algorithm to consider weights for each edge in the graph.
Dijkstra with Priority Queue: Optimizes the Dijkstra algorithm by using a priority queue (min-heap) to reduce time complexity.
Breadth-First Search (BFS): Explores nodes level by level and guarantees finding the shortest path in an unweighted graph.
Depth-First Search (DFS): Explores as deeply as possible along one branch before backtracking. It is not guaranteed to find the shortest path.
Neighborhood Search: Searches through neighboring nodes, commonly used in heuristic algorithms such as A*.

## Contributing
Feel free to fork the repository, submit issues, and create pull requests if you'd like to contribute improvements or additional features!

## License
This project is open-source and available under the MIT License. See the LICENSE file for more details.
