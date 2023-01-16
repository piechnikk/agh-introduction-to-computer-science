def zad23(head):
    fast = head
    slow = head
    counter = 0
    while fast != slow:
        slow = slow.next
        fast = fast.next.next
    meeting = fast
    while fast.next != meeting:
        fast = fast.next
        counter += 1
    return counter
