def dfs(graph):
    """Full DFS over every component. Returns (order, discovery, finish, parent)."""
    color = {v: 'WHITE' for v in graph}
    parent = {v: None for v in graph}
    disc, fin = {}, {}
    order = []
    time = [0]

    def visit(u):
        time[0] += 1
        disc[u] = time[0]               # discovery time
        color[u] = 'GRAY'
        order.append(u)
        for v in graph[u]:
            if color[v] == 'WHITE':
                parent[v] = u
                visit(v)                # recursion = implicit stack
        color[u] = 'BLACK'
        time[0] += 1
        fin[u] = time[0]                # finishing time

    for u in graph:                     # restart for disconnected graphs
        if color[u] == 'WHITE':
            visit(u)
    return order, disc, fin, parent


def dfs_iterative(graph, s):
    """Same traversal with an explicit stack (visits only s's component)."""
    visited, order, stack = set(), [], [s]
    while stack:
        u = stack.pop()
        if u not in visited:
            visited.add(u)
            order.append(u)
            for v in reversed(graph[u]):    # reversed keeps left-to-right order
                if v not in visited:
                    stack.append(v)
    return order


if __name__ == "__main__":
    g = {
        'A': ['B', 'C'],
        'B': ['A', 'D', 'E'],
        'C': ['A', 'F'],
        'D': ['B'],
        'E': ['B', 'F'],
        'F': ['C', 'E'],
    }
    order, disc, fin, parent = dfs(g)
    print("DFS order  :", order)
    print("Discovery  :", disc)
    print("Finishing  :", fin)
    print("Iterative  :", dfs_iterative(g, 'A'))
