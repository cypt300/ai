N = 8
board = [[0] * N for _ in range(N)]


def safe(r, c):
    for i in range(c):
        if board[r][i]:
            return False

    for i, j in zip(range(r, -1, -1), range(c, -1, -1)):
        if board[i][j]:
            return False

    for i, j in zip(range(r, N), range(c, -1, -1)):
        if board[i][j]:
            return False

    return True


def solve(c):
    if c == N:
        return True

    for r in range(N):
        if safe(r, c):
            board[r][c] = 1

            if solve(c + 1):
                return True

            board[r][c] = 0

    return False


if solve(0):
    for row in board:
        print(" ".join("Q" if x else "." for x in row))
else:
    print("No solution")
