class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key


class BinaryTree:
    def __init__(self, root):
        self.root = Node(root)
    def preorder_traversal1(self, node, level=0, prefix="Root: "):
        if node is not None:
            print(" " * (level * 4) + prefix + str(node.val))
            if node.left or node.right:
                self.preorder_traversal1(node.left, level + 1, "L--- ")
                self.preorder_traversal1(node.right, level + 1, "R--- ")

    def display_tree(self):
        self.preorder_traversal1(self.root)
    def preorder_traversal(self):
        result = ""
        stack = [self.root]

        while stack:
            current = stack.pop()
            result += str(current.val) + " "

            # Поместите правый узел в стек первым, чтобы обеспечить порядок прямого обхода
            if current.right:
                stack.append(current.right)

            # Поместите левый узел в стек, чтобы он был обработан после правого
            if current.left:
                stack.append(current.left)

        return result.strip()


# Создаем бинарное дерево поиска
bst = BinaryTree(10)
bst.root.left = Node(5)
bst.root.right = Node(15)
bst.root.left.left = Node(3)
bst.root.left.right = Node(7)
bst.root.right.left = Node(12)
bst.root.right.right = Node(18)
bst.display_tree()
# Вызываем прямой обход
result = bst.preorder_traversal()
print("Прямой обход бинарного дерева:", result)
