def dfs(graph, start, goal, path=None):
    if path is None:
        path = []
    path.append(start)
    if start == goal:
        return path
    for neighbor in graph[start]:
        if neighbor not in path:
            new_path = dfs(graph, neighbor, goal, path.copy())
            if new_path:
                return new_path
    return None

def bfs(graph, start, goal):
    queue = [(start, [start])]
    while queue:
        (vertex, path) = queue.pop(0)
        for next in set(graph[vertex]) - set(path):
            if next == goal:
                return path + [next]
            else:
                queue.append((next, path + [next]))
    return None

start_airport = "JFK"
goal_airport = "SEA"

dfs_path = dfs(G, start_airport, goal_airport)
bfs_path = bfs(G, start_airport, goal_airport)

print(f"DFS path from {start_airport} to {goal_airport}: {dfs_path}")
print(f"BFS path from {start_airport} to {goal_airport}: {bfs_path}")
