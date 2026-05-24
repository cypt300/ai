from collections import deque  # For queue (FIFO)


# Check if state is safe
def valid(m, c):
    if m < 0 or c < 0 or m > 3 or c > 3:
        return False  # Out of range

    if m > 0 and c > m:
        return False  # Cannibals > Missionaries (left side)

    mr = 3 - m  # Missionaries on right
    cr = 3 - c  # Cannibals on right
    if mr > 0 and cr > mr:
        return False  # Cannibals > Missionaries (right side)

    return True


def bfs():
    start = (3, 3, 1)  # Initial state
    goal = (0, 0, 0)  # Goal state

    q = deque([(start, [start])])  # Queue stores (state, path)
    visited = set([start])  # To avoid repeating states

    while q:
        (m, c, b), path = q.popleft()  # Remove first element

        if (m, c, b) == goal:
            return path  # Return solution path

        # Possible boat moves
        for dm, dc in [(1, 0), (2, 0), (0, 1), (0, 2), (1, 1)]:
            if b == 1:  # Boat on left
                new = (m - dm, c - dc, 0)
            else:  # Boat on right
                new = (m + dm, c + dc, 1)

            if valid(new[0], new[1]) and new not in visited:
                visited.add(new)
                q.append((new, path + [new]))


# Run and print solution
solution = bfs()
for step in solution:
    print(step)
