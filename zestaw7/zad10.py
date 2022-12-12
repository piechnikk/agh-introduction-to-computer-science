# 10. Liczby naturalne reprezentowane jak poprzednim zadaniu. Proszę napisać
# funkcję dodającą dwie takie liczby. W wyniku dodawania dwóch liczb powinna
# powstać nowa lista.
class Node:
    def __init__(self):
        self.val: int = None
        self.next: Node = None


def add(first1: Node, first2: Node, carry=0, tab: Node = None, start: Node = None):
    if first1 is not None and first2 is not None:
        sum = first1.val + first2.val + carry

    elif first1 is not None and first2 is None:
        sum = first1.val + carry

    elif first1 is None and first2 is not None:
        sum = first2 + carry

    else:
        return start

    next_val = sum % 10
    next_carry = sum // 10
    next_node = Node(next_val, None)
    if tab in None:
        tab = Node(next_val, None)
        start = tab
    else:
        tab.next = next_node
    add(first1.next, first2.next, next_carry, tab.next, start)
