#DFS CODE

def dfs(graph, start, end):
    visited = set()
    stack = [start]

    while stack:
        node = stack.pop()
        if node not in visited:
            visited.add(node)
            print(node, end=' ')
            if node == end:
              break
            stack.extend(reversed(graph[node]))

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

dfs(graph, start_node, end_node)
