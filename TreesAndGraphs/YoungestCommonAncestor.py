# This is an input class. Do not edit.
class AncestralTree:
    def __init__(self, name):
        self.name = name
        self.ancestor = None


def getYoungestCommonAncestor(topAncestor, descendantOne, descendantTwo):
    node_one = descendantOne
    node_two = descendantTwo
    count_one = 0
    count_two = 0
    while node_one != topAncestor:
        node_one = node_one.ancestor
        count_one += 1
    while node_two != topAncestor:
        node_two = node_two.ancestor
        count_two += 1
    if count_one > count_two:
        depth_diff = count_one - count_two
        while depth_diff != 0:
            descendantOne = descendantOne.ancestor
            depth_diff -= 1
    elif count_one < count_two:
        depth_diff = count_two - count_one
        while depth_diff != 0:
            descendantTwo = descendantTwo.ancestor
            depth_diff -= 1
    while descendantOne != descendantTwo:
        descendantOne = descendantOne.ancestor
        descendantTwo = descendantTwo.ancestor
    return descendantOne
