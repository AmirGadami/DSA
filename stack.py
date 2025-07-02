class Node:
    """
    Represents a single node in the stack.

    Attributes:
        value (any): The data stored in the node.
        next (Node): A reference to the next node below it in the stack.
    """
    def __init__(self, value):
        self.value = value
        self.next = None


class Stack:
    """
    A stack data structure implemented using a singly linked list.

    Attributes:
        top (Node): The top node of the stack.
        height (int): The number of elements in the stack.

    Methods:
        print_stack(): Prints the elements from top to bottom.
        push(value): Adds a value to the top of the stack.
        pop(): Removes and returns the top node from the stack.
    """
    def __init__(self, value):
        new_node = Node(value)
        self.top = new_node
        self.height = 1

    def print_stack(self):
        # Print all elements from top to bottom
        temp = self.top
        while temp is not None:
            print(temp.value)
            temp = temp.next

    def push(self, value):
        # Add a new node on top of the stack
        new_node = Node(value)
        if self.height == 0:
            self.top = new_node
        else:
            new_node.next = self.top
            self.top = new_node
        self.height += 1
        return True

    def pop(self):
        # Remove and return the top node
        if self.height == 0:
            return None
        temp = self.top
        self.top = self.top.next
        temp.next = None
        self.height -= 1
        return temp