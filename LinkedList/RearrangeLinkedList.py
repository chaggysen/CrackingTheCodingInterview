# This is the class of the input linked list.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def rearrangeLinkedList(head, k):
    smallerHead = None
    smallerTail = None
    equalsHead = None
    equalsTail = None
    largerHead = None
    largerTail = None

    current = head
    while current is not None:
        if current.value == k:
            equalsHead, equalsTail = appendToLinkedList(
                equalsHead, equalsTail, current)
        elif current.value < k:
            smallerHead, smallerTail = appendToLinkedList(
                smallerHead, smallerTail, current)
        else:
            largerHead, largerTail = appendToLinkedList(
                largerHead, largerTail, current)
        prevNode = current
        current = current.next
        prevNode.next = None

    firstHead, firstTail = connectLinkedLists(
        smallerHead, smallerTail, equalsHead, equalsTail)
    finalHead, _ = connectLinkedLists(
        firstHead, firstTail, largerHead, largerTail)
    return finalHead


def appendToLinkedList(head, tail, current):
    newHead = head
    newTail = current
    if newHead is None:
        newHead = current
    if tail is not None:
        tail.next = current
    return (newHead, newTail)


def connectLinkedLists(headOne, tailOne, headTwo, tailTwo):
    newHead = headTwo if headOne is None else headOne
    newTail = tailOne if tailTwo is None else tailTwo

    if tailOne is not None:
        tailOne.next = headTwo
    return (newHead, newTail)
