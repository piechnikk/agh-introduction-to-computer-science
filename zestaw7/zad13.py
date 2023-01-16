# 13. Proszę napisać funkcję, otrzymującą jako parametr wskaźnik na pierwszy
# element listy o wartościach typu int, usuwającą wszystkie elementy, których
# wartość jest mniejsza od wartości bezpośrednio poprzedzających je
# elementów.


class Node:
    def __init__(self, val):
        self.val = val
        self.next: Node = None


def delete_smaller_numbers(head: Node):
    current_node = head
    while True:
        if current_node.next is None:
            break
        else:
            if current_node.val < current_node.next.val:
                if current_node.next.next is None:
                    current_node.next = None
                else:
                    current_node.next = current_node.next.next
