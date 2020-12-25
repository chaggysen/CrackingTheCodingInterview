from LinkedList import LinkedList
# Write code to partition a linked list around a value x such that all nodes less than x
# come before all nodes greater than x. If x is contained within the list, the values of x only need
# to be after elements less than x.

# 2 solutions:
# 1) We can create 2 linkedlists, one for element less than x and one for elements greater or equals than x.
# We iterate throught the linked list inserting elements into our before list and our after list,
# Once we reached the end of the linked list and have completed the splitting, we merge the wo lists.

# 2) In this approach, we start a new list. Elements bigger than the pivot elements are put at the tail and
# elements smaller are put at the head. Each time we insert an element, we update either the tail or the head.


def partition(linkedlist, x):
    current = linkedlist.tail = linkedlist.head

    while current:
        nextNode = current.next
        current.next = None
        if current.value < x:
            current.next = linkedlist.head
            linkedlist.head = current
        else:
            linkedlist.tail.next = current
            linkedlist.tail = current
        current = nextNode

    # Error check in case all nodes are less than x
    if linkedlist.tail.next is not None:
        linkedlist.tail.next = None


ll = LinkedList()
ll.generate(10, 0, 99)
print(ll)
partition(ll, ll.head.value)
print(ll)
