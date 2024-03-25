class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def isSubtree(root, subRoot):
    if not root:
        return False
    return isSameTree(root, subRoot) or isSubtree(root.left, subRoot) or isSubtree(root.right, subRoot)


def isSameTree(p, q):
    if not p and not q:
        return True
    if not p or not q or p.val != q.val:
        return False
    return isSameTree(p.left, q.left) and isSameTree(p.right, q.right)


if __name__ == "__main__":
    tree_test1 = TreeNode(3, TreeNode(
        4, TreeNode(1), TreeNode(2)), TreeNode(5))
    tree_test2 = TreeNode(3, TreeNode(4, TreeNode(
        1), TreeNode(2, TreeNode(0))), TreeNode(5))
    sub_tree = TreeNode(4, TreeNode(1), TreeNode(2))
    print(isSubtree(tree_test2, sub_tree))
