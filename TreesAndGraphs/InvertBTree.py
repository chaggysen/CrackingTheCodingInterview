def invertBinaryTree(tree):
    if tree.left is None and tree.right is None:
        return
    tree.left, tree.right = tree.right, tree.left
    if tree.left:
        invertBinaryTree(tree.left)
    if tree.right:
        invertBinaryTree(tree.right)


# This is the class of the input binary tree.
class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
