class Node:
    """
    A node in the binary search tree.
    
    Attributes:
        value (int): The value stored in the node.
        left (Node): The left child node.
        right (Node): The right child node.
    """
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinarySearchTree:
    """
    A binary search tree (BST) implementation with recursive insert and delete operations.
    
    Attributes:
        root (Node): The root node of the tree.
    """
    def __init__(self):
        self.root = None

    def __r_insert(self, current_node, value):
        """
        Recursively insert a value into the tree starting from current_node.
        """
        if current_node is None:
            return Node(value)
        if value < current_node.value:
            current_node.left = self.__r_insert(current_node.left, value)
        elif value > current_node.value:
            current_node.right = self.__r_insert(current_node.right, value)
        return current_node

    def r_insert(self, value):
        """
        Public method to insert a value into the BST.
        """
        if self.root is None:
            self.root = Node(value)
        else:
            self.__r_insert(self.root, value)

    def min_value(self, current_node):
        """
        Returns the minimum value in the subtree rooted at current_node.
        """
        while current_node.left is not None:
            current_node = current_node.left
        return current_node.value

    def __delete_node(self, current_node, value):
        """
        Recursively delete a node with the given value from the subtree rooted at current_node.
        """
        if current_node is None:
            return None

        if value < current_node.value:
            current_node.left = self.__delete_node(current_node.left, value)
        elif value > current_node.value:
            current_node.right = self.__delete_node(current_node.right, value)
        else:
            # Case 1: No children
            if current_node.left is None and current_node.right is None:
                return None
            # Case 2: One child (right only)
            elif current_node.left is None:
                return current_node.right
            # Case 2: One child (left only)
            elif current_node.right is None:
                return current_node.left
            # Case 3: Two children
            else:
                sub_tree_min = self.min_value(current_node.right)
                current_node.value = sub_tree_min
                current_node.right = self.__delete_node(current_node.right, sub_tree_min)

        return current_node

    def delete_node(self, value):
        """
        Public method to delete a node with the specified value.
        """
        self.root = self.__delete_node(self.root, value)