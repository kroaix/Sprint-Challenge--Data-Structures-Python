class Node:
    def __init__(self, value=None, next_node=None):
        self.value = value
        self.next_node = next_node

    def get_value(self):
        return self.value

    def get_next(self):
        return self.next_node

    def set_next(self, new_next):
        self.next_node = new_next

class LinkedList:
    def __init__(self):
        self.head = None

    def add_to_head(self, value):
        node = Node(value)

        if self.head is not None:
            node.set_next(self.head)

        self.head = node

    def contains(self, value):
        if not self.head:
            return False

        current = self.head

        while current:
            if current.get_value() == value:
                return True

            current = current.get_next()

        return False

    def reverse_list(self, node, prev):
        #O(n)
        #node = current, prev = previous
        #pointer manipulation
        #if current node is 2 with prev being 1 we want instead to re-order it so that 2 is the prev and 1 is current so we need to change the direction the pointers are going
        #we will do this by storing our current, prev and next.. and manipulating those as long as current node is not None

        #reached the end of the list
        if node is None:
            return
        #if next node is none
        if node.next_node is None:
            #new head becomes current node
            self.head = node
            #next node of the new head = value of prev
            node.next_node = prev
        #not at end
        else:
            #saving next in temporary variable
            next_node = node.next_node
            #reversing.. point current node to previous node
            #prev node becomes current
            node.next_node = prev
            self.reverse_list(next_node, node)
