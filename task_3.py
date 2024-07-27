def dijkstra(graph, start):
    shortest_paths = {start: (None, 0)}
    current_node = start
    visited = set()

    while current_node is not None:
        visited.add(current_node)
        destinations = graph[current_node]
        weight_to_current_node = shortest_paths[current_node][1]

        for next_node, weight in destinations.items():
            weight = weight_to_current_node + weight
            if next_node not in shortest_paths:
                shortest_paths[next_node] = (current_node, weight)
            else:
                current_shortest_weight = shortest_paths[next_node][1]
                if current_shortest_weight > weight:
                    shortest_paths[next_node] = (current_node, weight)

        next_destinations = {node: shortest_paths[node] for node in shortest_paths if node not in visited}
        if not next_destinations:
            return shortest_paths
        current_node = min(next_destinations, key=lambda k: next_destinations[k][1])

    return shortest_paths

# Додавання ваг до ребер графа
weighted_connections = [
    ("JFK", "LAX", 5), ("JFK", "ORD", 2), ("JFK", "ATL", 3),
    ("LAX", "SFO", 2), ("LAX", "SEA", 4),
    ("ORD", "DFW", 1), ("ORD", "DEN", 3),
    ("DFW", "PHX", 2), ("DFW", "ATL", 4),
    ("DEN", "PHX", 3), ("DEN", "SEA", 2),
    ("ATL", "MIA", 2), ("ATL", "PHX", 3),
    ("SFO", "SEA", 1)
]

G_weighted = nx.Graph()
for u, v, w in weighted_connections:
    G_weighted.add_edge(u, v, weight=w)

shortest_paths = dijkstra(G_weighted, start_airport)
print(f"Shortest paths from {start_airport}: {shortest_paths}")
