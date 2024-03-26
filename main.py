# Define the graph
my_graph = {
    'A': [('B', 5), ('C', 3), ('E', 11)],
    'B': [('A', 5), ('C', 1), ('F', 2)],
    'C': [('A', 3), ('B', 1), ('D', 1), ('E', 5)],
    'D': [('C', 1), ('E', 9), ('F', 3)],
    'E': [('A', 11), ('C', 5), ('D', 9)],
    'F': [('B', 2), ('D', 3)]
}

# Function to find the shortest path
def shortest_path(graph, start, target=''):
    # Initialize unvisited nodes and distances
    unvisited = list(graph)
    distances = {node: 0 if node == start else float('inf') for node in graph}
    # Initialize paths dictionary to store the path from start to each node
    paths = {node: [] for node in graph}
    paths[start].append(start)  # Starting node path
    
    # Iterate until all nodes are visited
    while unvisited:
        # Find the node with the minimum distance
        current = min(unvisited, key=distances.get)
        # Iterate over the neighbors of the current node
        for node, distance in graph[current]:
            # Update distance if a shorter path is found
            if distance + distances[current] < distances[node]:
                distances[node] = distance + distances[current]
                # Update the path to the node
                if paths[node] and paths[node][-1] == node:
                    paths[node] = paths[current][:]
                else:
                    paths[node].extend(paths[current])
                paths[node].append(node)
        unvisited.remove(current)  # Mark current node as visited
    
    # Determine which nodes to print the results for
    targets_to_print = [target] if target else graph
    # Print distance and path for each target node
    for node in targets_to_print:
        if node == start:  # Skip if start node
            continue
        print(f'\n{start}-{node} distance: {distances[node]}\nPath: {" -> ".join(paths[node])}')
    
    # Return distances and paths dictionaries
    return distances, paths
    
# Test the function with start node 'A' and target node 'F'
shortest_path(my_graph, 'A', 'F')
