class Node:
    def __init__(self, val):
        self.val: int = val
        self.next: Node = None


def insert(head: Node, number):
    head_copy = head
    loop2 = False
    while True:
        start_node = None
        current_node = head_copy
        counter = 0
        loop = False
        while True:
            if start_node is None and str(current_node.val)[-1] == str(number)[0]:
                start_node = current_node
            elif counter >= 2 and str(number)[-1] == str(current_node.val)[0]:
                start_node.next = Node(number)
                start_node.next.next = current_node
                return counter - 1
            else:
                counter += 1
            if loop and current_node == head_copy:
                break
            loop = True
            current_node = current_node.next
        if loop2 and current_node == head_copy:
            break
        loop2 = True
        head_copy = head_copy.next
    return 0
