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
    
    # implement post-order traversal method
    def post_order_traversal(self):
        elements = []
        if self.left:
            elements += self.left.post_order_traversal()
        if self.right:
            elements += self.right.post_order_traversal()

        elements.append(self.data)

        return elements

    # implement pre-order traversal method
    def pre_order_traversal(self):
        elements = [self.data]
        if self.left:
            elements += self.left.pre_order_traversal()
        if self.right:
            elements += self.right.pre_order_traversal()

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
        return self.left.find_min()

    # find the maximum element of the binary
    def find_max(self):
        if self.right is None:
            return self.data
        return self.right.find_max()

    # find the sum of the elements
    def calculate_sum(self):
        left_sum = self.left.calculate_sum() if self.left else 0
        right_sum = self.right.calculate_sum() if self.right else 0
        return self.data + left_sum + right_sum

    # write the code for deleting a node
    def delete(self,val):
        if val < self.data:
            if self.left:
                self.left = self.left.delete(val)
        elif val > self.data:
            if self.right:
                self.right = self.right.delete(val)
        else:
            if self.left is None and self.right is None:
                return None

            if self.left is None:
                return self.right

            if self.right is None:
                return self.right

            min_val = self.right.find_min()
            self.data = min_val
            self.right = self.right.delete(min_val)

        return self





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
    letters = ["J", "A", "C", "Q", "U", "E", "L", "I", "N", "E", "B", "E", "R", "M", "U", "N", "D", "O"] 
    letters_tree = build_tree(letters)
    letters_tree.delete("Q")

    print("Min: ", letters_tree.find_min())
    print("Max: ", letters_tree.find_max())
    print("In order traversal: ", letters_tree.in_order_traversal())
    print("Post order traversal: ", letters_tree.post_order_traversal())
    print("Pre order traversal: ", letters_tree.pre_order_traversal())
    print("After deleting Q: ", letters_tree.in_order_traversal())
