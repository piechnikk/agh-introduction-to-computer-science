class Node:
    def __init__(self, val):
        self.val: int = val
        self.next: Node = None


def add1(head: Node):
    # lista idzie od końca liczby pierwszy znak to cyfra jedności etc.
    # guard = Node(None)
    # guard.next = head
    current_node = head
    current_transfer = 1
    while True:
        current_sum = current_node.val + current_transfer
        current_transfer = current_sum // 10
        current_node.val = current_sum % 10
        if current_node.next is None:
            break

        current_node = current_node.next

    if current_transfer != 0:
        current_node.next = Node(current_transfer)
