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

    # implement a search method
    def search(self, val):
        if self.data == val:
            return True

        if val < self.data:
            # val might be in left subtree
            if self.left:
                return self.left.search(val)
            else:
                return False

        if val > self.data:
            # val might be in right subtree
            if self.right:
                return self.right.search(val)
            else:
                return False

    # find the minimum element of the binary tree
    def find_min(self):
        if self.left is None:
            return self.data
        return self.left.right.find_min()


# write a helper method
def build_tree(elements):
    # set the first element as the root node
    root = BinarySearchTreeNode(elements[0])

    # run a full loop on elements
    for i in range(1, len(elements)):
        # build a tree
        root.add_child(elements[i])

    return root

# if __name__ == '__main__':
    numbers = [17, 4, 1, 20, 9, 23, 18, 34, 18, 4] # added 18 and 4 to check if it will duplicate in the tree
    numbers_tree = build_tree(numbers)
    # printing the tree in an in-order traversal method
    # print(numbers_tree.in_order_traversal())
    # check if the search is working
    print(numbers_tree.search(200))

# building tree that contains string
#if __name__ == '__main__':
    countries = ["India", "Pakistan", "Germany", "USA", "China", "India", "UK", "USA"] 
    country_tree = build_tree(countries)

    print("UK is in the list? ", country_tree.search("UK"))
    print("Sweden is in the list? ", country_tree.search("Sweden"))

    print(country_tree.in_order_traversal())

if __name__ == '__main__':
    numbers = [17, 4, 1, 20, 9, 23, 18, 34] 
    numbers_tree = build_tree(numbers)



