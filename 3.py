import heapq

# heuristic values
h = {"A": 11, "B": 6, "C": 5, "D": 7, "E": 3, "F": 6, "G": 5, "H": 3, "I": 1, "J": 0}

# graph with costs
graph = {
    "A": [("B", 6), ("F", 3)],
    "B": [("C", 3), ("D", 2)],
    "C": [("E", 5)],
    "D": [("E", 8)],
    "E": [("J", 5)],
    "F": [("G", 1), ("H", 7)],
    "G": [("I", 3)],
    "H": [("I", 2)],
    "I": [("J", 3)],
    "J": [],
}


def astar(start, goal):
    open = [(h[start], start)]
    g = {start: 0}
    parent = {start: None}

    while open:
        f, node = heapq.heappop(open)

        if node == goal:
            path = []
            while node:
                path.append(node)
                node = parent[node]
            return path[::-1]

        for n, c in graph[node]:
            new = g[node] + c
            if n not in g or new < g[n]:
                g[n] = new
                heapq.heappush(open, (new + h[n], n))
                parent[n] = node


print("Optimal Path :", astar("A", "J"))
