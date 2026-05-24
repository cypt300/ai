graph = {
    "A": [(["B", "C"], 1), (["D"], 5)],
    "B": [(["E"], 3)],
    "C": [(["E"], 1)],
    "D": [(["G"], 2)],
    "E": [(["G"], 5)],
    "G": [],
}

sol = {}


def ao(n):
    if n in sol:
        return sol[n]

    if not graph[n]:
        sol[n] = (0, None)
        return sol[n]

    mc = float("inf")
    bp = None

    for p, c in graph[n]:
        tc = c
        for x in p:
            tc += ao(x)[0]

        if tc < mc:
            mc, bp = tc, p

    sol[n] = (mc, bp)
    return sol[n]


ao("A")

print("Solution Graph:")
for n, (c, p) in sol.items():
    print("Node:", n, "Cost:", c, "Path:", p)
