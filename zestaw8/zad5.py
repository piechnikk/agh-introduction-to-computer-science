class Node:
    def __init__(self):
        self.val = None
        self.left: Node = None
        self.right: Node = None


def leaves(root: Node):
    if root == None:
        return 0
    if root.left is None and root.right is None:
        return 0
    return leaves(root.left) + leaves(root.right)
