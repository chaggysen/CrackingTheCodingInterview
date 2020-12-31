# This is an input class. Do not edit.
class BinaryTree:
    def __init__(self, value, left=None, right=None, parent=None):
        self.value = value
        self.left = left
        self.right = right
        self.parent = parent


def findSuccessor(tree, node):
    nodes = []
    findSuccessorHelper(tree, node, nodes)
    for i in range(len(nodes)):
        if nodes[i] == node:
            if i == len(nodes) - 1:
                return None
            else:
                return nodes[i + 1]
    return None


def findSuccessorHelper(cur_node, node, nodes):
    if cur_node is None:
        return
    findSuccessorHelper(cur_node.left, node, nodes)
    nodes.append(cur_node)
    findSuccessorHelper(cur_node.right, node, nodes)
