def is_binary_search_tree(tree):
    return _is_bst(tree.root)


def _is_bst(node, min_val=None, max_val=None):
    if not node:
        return True
    if (min_val and node.key < min_val) or (max_val and node.ley > max_val):
        return False
    return _is_bst(node.left, min_val, node.key) and _is_bst(node.right, node.key, max_val)
