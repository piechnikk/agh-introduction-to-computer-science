class Node:
    def __init__(self, val):
        self.val = val
        self.next: Node = None


def remove_not_unique(head: Node):
    counter = 0
    guard = Node(None)
    guard.next = head
    current_node = guard

    while True:
        if current_node is None or current_node.next is None:
            break
        elif current_node.val == current_node.next.val:
            current_node.next = current_node.next.next
        else:
            current_node = current_node.next
