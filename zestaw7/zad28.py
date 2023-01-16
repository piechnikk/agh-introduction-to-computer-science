class Node:
    def __init__(self):
        self.val = None
        self.next: Node = None


def delete(guard1: Node, guard2: Node):
    counter = 0
    back2, front2 = guard2, guard2.next
    while front2:
        back1, front1 = guard1, guard1.next
        while front1.val <= front2.val:
            if front1:
                back1, front1 = front1, front1.next
            else:
                back2, front2 = front2, front2.next
                break
            if front1.val == front2.val:
                counter += 2
                delEl(back1, front1)
                delEl(back2, front2)
        back2, front2 = front2, front2.next
    return counter


def delEl(back: Node, front: Node):
    if front:
        back.next = front.next
    else:
        back.next = None
