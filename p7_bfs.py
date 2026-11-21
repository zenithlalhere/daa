from collections import deque


def bfs(graph, s):
    """graph: dict {vertex: [neighbours]}. Returns (order, dist, parent)."""
    dist = {v: None for v in graph}     # None = WHITE (undiscovered)
    parent = {v: None for v in graph}
    dist[s] = 0                         # source becomes GRAY
    queue = deque([s])
    order = []
    while queue:
        u = queue.popleft()             # dequeue
        order.append(u)                 # u turns BLACK once processed
        for v in graph[u]:
            if dist[v] is None:         # undiscovered neighbour
                dist[v] = dist[u] + 1
                parent[v] = u
                queue.append(v)         # enqueue
    return order, dist, parent


def shortest_path(parent, s, v):
    """Rebuild s -> v path from the parent map."""
    path = []
    while v is not None:
        path.append(v)
        v = parent[v]
    path.reverse()
    return path if path and path[0] == s else None


if __name__ == "__main__":
    g = {
        'A': ['B', 'C'],
        'B': ['A', 'D', 'E'],
        'C': ['A', 'F'],
        'D': ['B'],
        'E': ['B', 'F'],
        'F': ['C', 'E'],
    }
    order, dist, parent = bfs(g, 'A')
    print("BFS order :", order)
    print("Distances :", dist)
    print("Path A->F :", shortest_path(parent, 'A', 'F'))
