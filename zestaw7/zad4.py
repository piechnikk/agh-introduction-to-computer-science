class Node:
    def __init__(self):
        self.val = None
        self.next: Node = None


def reverseNode(p: Node):
    if p == None:
        return None
    if p.next == None:
        return p
    if p.next.nexy == None:
        l = p.next
        l.next = p
        p.next = None
        return 1
    l = p.next
    m = l.next
    p.next = None
    while m != None:
        l.next = p
        p = l
        l = m
        m = m.next
    l.next = p
    return l


def reqReverseNode(first: Node, last: Node = None):
    if first == None:
        return None, None
    if first.next == None:
        return first, first
    x, y = reqReverseNode(first.next)
    y.next = first
    first.next = None
    return x, first
