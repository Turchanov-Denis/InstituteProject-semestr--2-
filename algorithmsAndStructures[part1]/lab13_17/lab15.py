class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def display_tree(node, level=0, prefix="Root: ", is_left=None):
    if node is not None:
        print(" " * (level * 4) + prefix, end="")
        print("|-- ", end="")
        print(node.value)

        display_tree(node.left, level + 1, "L--- ", True)
        display_tree(node.right, level + 1, "R--- ", False)

def pre_order_traversal(node, level=0):
    if node:
        print(" " * (level * 4) + f"Прямой обход: {node.value}")
        pre_order_traversal(node.left, level + 1)
        pre_order_traversal(node.right, level + 1)

def in_order_traversal(node, level=0):
    if node:
        in_order_traversal(node.left, level + 1)
        print(" " * (level * 4) + f"Центральный обход: {node.value}")
        in_order_traversal(node.right, level + 1)

def post_order_traversal(node, level=0):
    if node:
        post_order_traversal(node.left, level + 1)
        post_order_traversal(node.right, level + 1)
        print(" " * (level * 4) + f"Концевой обход: {node.value}")

# Пример создания бинарного дерева
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)

# Вывод графического представления дерева
print("Исходное дерево:")
display_tree(root)
print()

# Прямой обход
print("Прямой обход:")
pre_order_traversal(root)
print()

# Центральный обход
print("Центральный обход:")
in_order_traversal(root)
print()

# Концевой обход
print("Концевой обход:")
post_order_traversal(root)
