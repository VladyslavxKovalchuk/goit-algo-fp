import heapq


class Graph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, u, v, weight):
        if u not in self.graph:
            self.graph[u] = []
        self.graph[u].append((v, weight))


def dijkstra(graph, start):
    heap = [(0, start)]
    visited = {}

    while heap:
        (current_distance, current_vertex) = heapq.heappop(heap)

        if current_vertex in visited:
            continue

        visited[current_vertex] = current_distance

        for neighbor, weight in graph.get(current_vertex, []):
            distance = current_distance + weight

            if neighbor not in visited:
                heapq.heappush(heap, (distance, neighbor))

    return visited


if __name__ == "__main__":
    g = Graph()

    g.add_edge("A", "B", 1)
    g.add_edge("A", "C", 4)
    g.add_edge("B", "C", 2)
    g.add_edge("B", "D", 5)
    g.add_edge("C", "D", 1)

    start_vertex = "A"

    shortest_paths = dijkstra(g.graph, start_vertex)

    print(f"Коротший ш {start_vertex}: {shortest_paths}")
