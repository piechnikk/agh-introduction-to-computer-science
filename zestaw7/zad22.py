def zad22(head):
    fast = head
    slow = head
    while slow.next != None and fast.next != None and fast.next.next != None:
        if fast == slow:
            return True
        slow = slow.next
        fast = fast.next.next
    return False
