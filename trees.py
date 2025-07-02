class Node:
    """
    Represents a node in a binary search tree.

    Attributes:
        value (any): The value stored in the node.
        left (Node): The left child node.
        right (Node): The right child node.
    """
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinarySearchTree:
    """
    A Binary Search Tree (BST) implementation.

    Attributes:
        root (Node): The root node of the tree.

    Methods:
        insert(value): Inserts a value into the BST. Returns True if inserted, False if duplicate.
        contains(value): Returns True if value exists in the BST, else False.
    """
    def __init__(self):
        self.root = None

    def insert(self, value):
        # Insert a value into the tree
        new_node = Node(value)
        if self.root is None:
            self.root = new_node
            return True

        temp = self.root
        while True:
            if new_node.value == temp.value:
                return False  # No duplicates allowed

            if new_node.value < temp.value:
                if temp.left is None:
                    temp.left = new_node
                    return True
                temp = temp.left
            else:  # new_node.value > temp.value
                if temp.right is None:
                    temp.right = new_node
                    return True
                temp = temp.right

    def contains(self, value):
        # Check if the tree contains a value
        if self.root is None:
            return False

        temp = self.root
        while temp is not None:
            if value < temp.value:
                temp = temp.left
            elif value > temp.value:
                temp = temp.right
            else:
                return True  # Found
        return False  # Not found