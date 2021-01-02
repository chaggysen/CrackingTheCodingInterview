# Do not edit the class below except
# for the depthFirstSearch method.
# Feel free to add new properties
# and methods to the class.
class Node:
    def __init__(self, name):
        self.children = []
        self.name = name

    def addChild(self, name):
        self.children.append(Node(name))
        return self

    def depthFirstSearch(self, array):
        current = self
        if current is None:
            return []
        array.append(current.name)
        for child in current.children:
            child.depthFirstSearch(array)
        return array
