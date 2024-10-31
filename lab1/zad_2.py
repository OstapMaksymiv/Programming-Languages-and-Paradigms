from collections import deque

def bfs(graph, start, end):
    queue = deque([[start]])
    visited = set()
    while queue:
        path = queue.popleft()
        node = path[-1]
        if node == end:
            return path
        if node not in visited:
            for neighbor in graph.get(node,[]):
                new_path = list(path)
                new_path.append((neighbor))
                queue.append((new_path))
            visited.add(node)
    return None



graph = {
    'A': ['B', 'D'],
    'B': ['A', 'C'],
    'C': ['B'],
    'D': ['A']
}

start_node = 'A'
end_node = 'C'
shortest_path = bfs(graph, start_node, end_node)

if shortest_path:
    print(f'Najkrótsza ścieżka z {start_node} do {end_node}: {shortest_path}')
else:
    print(f'Nie znaleziono ścieżki z {start_node} do {end_node}.')

