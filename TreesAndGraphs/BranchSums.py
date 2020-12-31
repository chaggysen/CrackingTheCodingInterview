class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def branchSums(root):
    currentSum = 0
    output = []
    branchSumsHelper(root, currentSum, output)
    return output


def branchSumsHelper(node, currentSum, array):
    currentSum += node.value
    if node.left is None and node.right is None:
        array.append(currentSum)
    elif node.left is None:
        branchSumsHelper(node.right, currentSum, array)
    elif node.right is None:
        branchSumsHelper(node.left, currentSum, array)
    else:
        branchSumsHelper(node.left, currentSum, array)
        branchSumsHelper(node.right, currentSum, array)
