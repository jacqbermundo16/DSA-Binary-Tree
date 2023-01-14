# define a binary search tree node class
class BinarySearchTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
    # adding nodes
    def add_child(self, data):
        # if there data is not empty
        if data == self.data:
            return

        if data < self.data:
            # add data in the left subtree
            # check if left node has a value
            if self.left:
                self.left.add_child(data)
            # if left node is empty
            else:
                self.left = BinarySearchTreeNode(data) 
        else:
            # add data in right subtree
            if self.right:
                self.right.add_child(data)
            # if left node is empty
            else:
                self.right = BinarySearchTreeNode(data) 