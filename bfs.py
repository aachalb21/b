#BFS CODE

from collections import deque

def bfs(graph, start, end):
    visited = set()
    queue = deque([start])
    while queue:
        node = queue.popleft()
        if node not in visited:
            visited.add(node)
            print(node, end=' ')
            if node == end:
                break
            queue.extend(graph[node])

graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B'],
    'F': ['C']
}

print("Constructed graph:", graph)

start_node = input("Enter the starting node: ").strip().upper()
end_node = input("Enter the ending node: ").strip().upper()

bfs(graph, start_node, end_node)
