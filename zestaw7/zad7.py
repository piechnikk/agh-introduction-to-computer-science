class Node:
    def __init__(self, val):
        self.val:any = val
        self.next:Node = None

def delLastEl(head:Node):
    curr = head
    while curr.next is not None:
        if curr.next.next is None:
            curr.next = None
        curr = curr.next