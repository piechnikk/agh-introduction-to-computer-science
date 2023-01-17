class Node:
    def __init__(self, val):
        self.val: int = val
        self.next = None


def insert(head: Node, number):
    start_node = head
    while start_node is not None:
        current_node = start_node
        current_start_node = None
        counter = 0
        while current_node is not None:
            if current_start_node is None and str(current_node)[-1] == str(number)[0]:
                current_start_node = current_node
            elif counter >= 2 and str(current_node)[0] == str(number)[-1]:
                current_start_node.next = Node(number)
                current_start_node.next.next = current_node
                return counter
            current_node = current_node.next
        start_node = start_node.next
