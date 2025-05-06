
#A* SEARCH

import heapq

def a_star(graph, start, goal, heuristic):
    open_list = []
    heapq.heappush(open_list, (0 + heuristic[start], start))
    
    g_costs = {start: 0}
    parent = {start: None}
    open_set = {start}
    
    while open_list:
        _, current_node = heapq.heappop(open_list)
        open_set.remove(current_node)
        
        if current_node == goal:
            path = []
            while current_node is not None:
                path.append(current_node)
                current_node = parent[current_node]
            return path[::-1], g_costs[goal]
        
        for neighbor, cost in graph[current_node].items():
            tentative_g_cost = g_costs[current_node] + cost
            
            if neighbor not in g_costs or tentative_g_cost < g_costs[neighbor]:
                g_costs[neighbor] = tentative_g_cost
                f_cost = tentative_g_cost + heuristic.get(neighbor, 0)
                if neighbor not in open_set:
                    heapq.heappush(open_list, (f_cost, neighbor))
                    open_set.add(neighbor)
                parent[neighbor] = current_node
                
    return None, float('inf')

graph = {
    'A': {'B': 1, 'C': 4},
    'B': {'A': 1, 'C': 2, 'D': 5},
    'C': {'A': 4, 'B': 2, 'D': 1},
    'D': {'B': 5, 'C': 1}
}

heuristic = {
    'A': 7,
    'B': 6,
    'C': 2,
    'D': 0
}

start = 'A'
goal = 'D'
path, cost = a_star(graph, start, goal, heuristic)

if path:
    print(f"Path found: {path}")
    print(f"Minimum cost: {cost}")
else:
    print("No path found")
