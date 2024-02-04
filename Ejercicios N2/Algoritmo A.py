import heapq

def a_star(graph, start, goal):
    queue = [(0, start, [])]
    visited = set()

    while queue:
        cost, current, path = heapq.heappop(queue)

        if current in visited:
            continue

        visited.add(current)
        path = path + [current]

        if current == goal:
            return path

        for neighbor, weight in graph[current].items():
            heapq.heappush(queue, (cost + weight, neighbor, path))

# Ejemplo de uso:
grafo = {
    'A': {'B': 1, 'C': 4},
    'B': {'A': 1, 'C': 2, 'D': 5},
    'C': {'A': 4, 'B': 2, 'D': 1},
    'D': {'B': 5, 'C': 1}
}
resultado = a_star(grafo, 'A', 'D')
print(resultado)
