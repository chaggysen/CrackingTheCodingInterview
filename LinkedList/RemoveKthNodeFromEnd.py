# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def removeKthNodeFromEnd(head, k):
    runner = head
    prev = head
    for i in range(k):
        runner = runner.next
    # Here, we want to remove the head node
    if runner is None:
        head.value = head.next.value
        head.next = head.next.next
        return
    while runner.next is not None:
        runner = runner.next
        prev = prev.next
    prev.next = prev.next.next
