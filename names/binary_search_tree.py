class BSTNode:
    def __init__(self, value=None):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        if self.value is None:
            self.value = value
        #compare target value to node value
        #if value >= node.value
        if value >= self.value:
            #go right
            #if node.right is none
            if self.right is None:
                #create new node there
                self.right = BSTNode(value)
            else: #self.right is a BSTNode
                #do the same thing (recurse)
                #insert value into node.right
                #right_child is a BSTNode, so we can call insert on it
                right_child = self.right
                right_child.insert(value)

        #else if value < node.value
        if value < self.value:
            #go left
            #if node.left is none
            if self.left is None:
                #create node
                self.left = BSTNode(value)
            else:
                #do the same thing
                #compare and go left or right
                #insert value into node.left
                left_child = self.left
                left_child.insert(value)

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        # Compare target value to node.value
        # If target == node.value:
        if target == self.value:
        # return True
            return True

        # If target > node.value:
        if target > self.value:
        # Go right
        # If node.right is None:
        # We've traversed the tree and haven't found it
        # return False    
            if self.right is None:
                return False
            else:
            # return node.right.contains(target)
                return self.right.contains(target)

        # Else if target < node.value
        if target < self.value:
        # Go Left
        # If node.left is None:
        # return False
            if self.left is None:
                return False
        # Else:
            else:
        # Do the same thing
        # (compare, go left or right)
        # return node.left.contains(target)
                return self.left.contains(target)