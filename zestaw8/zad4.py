class Node:
    def __init__(self):
        self.val = None
        self.left: Node = None
        self.right: Node = None


def height(head: Node, cnt=1):
    if head == None:
        return 0
    return max(height(head.left), height(head.right)) + 1
