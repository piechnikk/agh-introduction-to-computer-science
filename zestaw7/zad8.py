# 8. Dana jest niepusta lista, proszę napisać funkcję usuwającą co drugi
# element listy. Do funkcji należy przekazać wskazanie na pierwszy element
# listy.


class Node:
    def __init__(self):
        self.val = None
        self.next: Node = None


def delete(first: Node):
    p = first
    while first != None and p.next != None:
        p.next = p.next.next
        p = p.next


def delete_rec(first: Node):
    if first == None or first.next == None:
        return first
    p = first
    p.next = p.next.next
    delete_rec(p.next)
    return first
