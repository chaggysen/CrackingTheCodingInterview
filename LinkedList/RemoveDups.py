from LinkedList import LinkedList
# Write code to remove duplicates from an unsorted linked list


def remove_dups(linkedlist):
    memo = {}
    if linkedlist.head is None:
        return
    cur_node = linkedlist.head
    memo[cur_node.value] = True
    while cur_node.next:
        if cur_node.next.value in memo:
            cur_node.next = cur_node.next.next
        else:
            memo[cur_node.next.value] = True
            cur_node = cur_node.next

    return linkedlist


ll = LinkedList()
ll.generate(100, 0, 9)
print(ll)
remove_dups(ll)
print(ll)
