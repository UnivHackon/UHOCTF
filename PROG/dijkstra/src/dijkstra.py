import heapq

def dijkstra(graph, source, destination):
    distances = {node: float('inf') for node in graph["nodes"]}
    distances[source] = 0

    heap = [(0, source)]
    while heap:
        current_distance, current_node = heapq.heappop(heap)

        if current_distance > distances[current_node]:
            continue

        if current_node == destination:
            break

        for edge in graph["edges"]:
            if edge["source"] == current_node:
                neighbor = edge["target"]
                distance = current_distance + edge["weight"]
                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    heapq.heappush(heap, (distance, neighbor))

    return distances[destination]

# Exemple d'utilisation
graph = {
    "nodes": ["A", "B", "C"],
    "edges": [
        {"source": "A", "target": "B", "weight": 5},
        {"source": "B", "target": "C", "weight": 3},
        {"source": "A", "target": "C", "weight": 10}
    ]
}

source = "A"
destination = "C"
shortest_distance = dijkstra(graph, source, destination)
print(shortest_distance)