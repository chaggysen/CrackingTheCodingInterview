from LinkedList import LinkedList
# Write code to remove duplicates from an unsorted linked list

def remove_dups(node):
    memo = {}
    if node is None:
        return
    cur_node = node.head
    memo[cur_node.value] = True
    while cur_node.next:
        if cur_node.next.value in memo:
            cur_node.next = cur_node.next.next
        else:
            memo[cur_node.next.value] = True
            cur_node = cur_node.next

    return node
