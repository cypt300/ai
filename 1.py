# Water Jug DFS for X=3, Y=5, Z=4

X = 3
Y = 5
Z = 4

visited = set()


def dfs(state, path):
    if state in visited:
        return False

    visited.add(state)
    path.append(state)

    x, y = state

    # Goal check
    if x == Z or y == Z:
        print("Solution Path:")
        for step in path:
            print(step)
        return True

    # Possible moves
    possible_moves = [
        (X, y),  # Fill X
        (x, Y),  # Fill Y
        (0, y),  # Empty X
        (x, 0),  # Empty Y
        # Pour X -> Y
        (x - min(x, Y - y), y + min(x, Y - y)),
        # Pour Y -> X
        (x + min(y, X - x), y - min(y, X - x)),
    ]

    for move in possible_moves:
        if dfs(move, path.copy()):
            return True

    return False


dfs((0, 0), [])
