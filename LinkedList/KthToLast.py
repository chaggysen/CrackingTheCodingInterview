from LinkedList import LinkedList
# Implement an algorithm to find the kth to last element of a singly linked list.
# We can use two pointers (runner and current). We place them k nodes apart in the linked list by putting current
# at the beginning and runner at the k nodes into the list. Then, we more them at the same  pace.
# runner will hit the end of the linked list after Lenght - k steps and at that point, current will be the length - k node.


def kth_to_last(linkedlist, k):
    runner = current = linkedlist.head
    for i in range(k):
        if runner is None:
            return None
        runner = runner.next

    while runner:
        current = current.next
        runner = runner.next

    return current


linkedlist = LinkedList()
linkedlist.generate(10, 0, 99)
print(linkedlist)
print(kth_to_last(linkedlist, 3))
