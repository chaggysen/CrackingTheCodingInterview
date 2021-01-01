def minHeightBst(array):
	start = 0
	end = len(array)
    return minHeightBstHelper(array, start, end - 1)

def minHeightBstHelper(array, start, end):
	if start > end:
		return
	mid = (start + end) // 2
	value = array[mid]
	newNode = BST(value)
	newNode.left = minHeightBstHelper(array, start, mid - 1)
	newNode.right = minHeightBstHelper(array, mid + 1, end)
	return newNode

class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        if value < self.value:
            if self.left is None:
                self.left = BST(value)
            else:
                self.left.insert(value)
        else:
            if self.right is None:
                self.right = BST(value)
            else:
                self.right.insert(value)
