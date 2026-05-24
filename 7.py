def neg(x):
    return x[1:] if x.startswith("~") else "~" + x


def res(c1, c2):
    r = []
    for a in c1:
        for b in c2:
            if a == neg(b):
                r.append([x for x in c1 + c2 if x not in [a, b]])
    return r


def solve(kb):
    c = [x.split("||") for x in kb]

    while True:
        n = set()

        for i, a in enumerate(c):
            for b in c[i + 1 :]:
                n.update(tuple(x) for x in res(a, b))

        if not n:
            return "Satisfiable"

        if any(len(x) == 0 for x in n):
            return "Unsatisfiable"

        c.extend([list(x) for x in n])


kb = ["P || Q || ~R", "~P || R", "~Q || R", "~R || ~P || Q"]

print(solve(kb))


# output:
# Satisfiable


kb = ["P", "~P"]

print(solve(kb))

# output:
# Unsatisfiable
