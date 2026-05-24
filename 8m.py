# Minimax

scores = [3, 5, 2, 9]
tree_depth = 2


def minimax(depth, node, isMax):
    if depth == tree_depth:
        return scores[node]

    if isMax:
        return max(
            minimax(depth + 1, node * 2, False), minimax(depth + 1, node * 2 + 1, False)
        )
    else:
        return min(
            minimax(depth + 1, node * 2, True), minimax(depth + 1, node * 2 + 1, True)
        )


print("Leaf Nodes:", scores)
print("Optimal Value:", minimax(0, 0, True))


"""
OUTPUT:    
Leaf Nodes: [3, 5, 2, 9]
Optimal Value: 5
"""
