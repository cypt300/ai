graph = [[0, 10, 15, 20], [10, 0, 35, 25], [15, 35, 0, 30], [20, 25, 30, 0]]


def tsp(g, s):
    n = len(g)
    visited = [False] * n
    path = [s]
    visited[s] = True
    cost = 0
    cur = s

    for _ in range(n - 1):
        m = float("inf")
        nxt = -1

        for i in range(n):
            if not visited[i] and g[cur][i] < m:
                m = g[cur][i]
                nxt = i

        path.append(nxt)
        visited[nxt] = True
        cost += m
        cur = nxt

    cost += g[cur][s]
    path.append(s)

    return cost, path


cost, path = tsp(graph, 0)

print("Cost:", cost)
print("Path:", " -> ".join(map(str, path)))
