class Node:
    def __init__(self, val):
        self.val = val
        self.next: Node = None


def delOrAdd(head: Node, val):
    guard = Node(None)
    guard.next = head
    current_node = guard
    valExists = False
    while True:
        if current_node.next is None:
            break
        elif current_node.next.val == val:
            current_node.next = current_node.next.next
            valExists = True
            break
        current_node = current_node.next

    if not valExists:
        current_node.next = Node(val)
