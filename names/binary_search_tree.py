class BSTNode:
    def __init__(self, value=None):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree

    # compare value of node to parent node and decides whether to insert to left or right side of the binary tree
    def insert(self, value):
        if self.value is None:
          self.value = value
        # compare new value with parent node
        # if the new value is less than the parent value
        elif value < self.value:
            # if empty construct a node based on the value we are given
            if self.left is None:
                self.left = BSTNode(value)
            # otherwise, insert left
            else:
                self.left.insert(value)
        # same written above goes for right
        else:
            if self.right is None:
                self.right = BSTNode(value)
            else:
                self.right.insert(value)

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        if self.value == target:
            return True
            #if target is more than or equal to value - go right
        elif target > self.value:
            if self.right is not None:
              #keep looking right
                return self.right.contains(target)
            else:
              #completed our search with no matches
                return False
        else:
            if self.left is not None:
              #keep looking left
                return self.left.contains(target)
            else:
              #completed our search with no matches
                return False
