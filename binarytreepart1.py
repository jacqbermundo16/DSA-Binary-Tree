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

    # implement in-order traversal method
    def in_order_traversal(self):
        elements = []

        # visit left tree 
        if self.left:
            elements += self.left.in_order_traversal()
        
        # visit base node
        elements.append(self.data)

        # visit right tree
        if self.right:
            elements +=self.right.in_order_traversal()

        return elements

# write a helper method
def build_tree(elements):
    # set the first element as the root node
    root = BinarySearchTreeNode(elements[0])

    # run a full loop on elements
    for i in range(1, len(elements)):
        # build a tree
        root.add_child(elements[i])

    return root

if __name__ == '__main__':
    numbers = [17, 4, 1, 20, 9, 23, 18, 34]
    numbers_tree = build_tree(numbers)