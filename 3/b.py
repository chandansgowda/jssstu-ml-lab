class TreeNode:
    def __init__(self, value, children=[]):
        self.value = value
        self.children = children

def minimax(node, depth, maximizing_player):
    if depth == 0 or not node.children:
        return node.value, [node.value]

    if maximizing_player:
        max_value = float("-inf")
        max_path = []
        for child_node in node.children:
            child_value, child_path = minimax(child_node, depth - 1, False)
            if child_value > max_value:
                max_value = child_value
                max_path = [node.value] + child_path
        return max_value, max_path
    else:
        min_value = float("inf")
        min_path = []
        for child_node in node.children:
            child_value, child_path = minimax(child_node, depth - 1, True)
            if child_value < min_value:
                min_value = child_value
                min_path = [node.value] + child_path
        return min_value, min_path


game_tree = TreeNode(0, [
    TreeNode(1, [TreeNode(3),TreeNode(12)]),
    TreeNode(4, [TreeNode(8),TreeNode(2)])
])


optimal_value, optimal_path = minimax(game_tree, 2, True)

print("Optimal value:", optimal_value)
print("Optimal path:", optimal_path)
