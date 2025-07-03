class Node:
    """
    Represents a node in the binary search tree.

    Attributes:
        value (int): The value stored in the node.
        left (Node): Pointer to the left child.
        right (Node): Pointer to the right child.
    """
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinarySearchTree:
    """
    A Binary Search Tree (BST) with insertion, search, and traversal methods.
    
    Attributes:
        root (Node): The root of the tree.
    """
    def __init__(self):
        self.root = None

    def insert(self, value):
        """
        Inserts a new node into the BST.
        Returns True if inserted, False if value already exists.
        """
        new_node = Node(value)
        if self.root is None:
            self.root = new_node
            return True

        temp = self.root
        while True:
            if new_node.value == temp.value:
                return False  # Duplicate value not allowed
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
        """
        Checks whether the value exists in the BST.
        Returns True if found, False otherwise.
        """
        if self.root is None:
            return False

        temp = self.root
        while temp:
            if value < temp.value:
                temp = temp.left
            elif value > temp.value:
                temp = temp.right
            else:
                return True
        return False

    def BFS(self):
        """
        Performs Breadth-First Search (level-order traversal).
        Returns a list of values in BFS order.
        """
        current_node = self.root
        queue = []
        results = []

        if current_node is None:
            return results

        queue.append(current_node)

        while len(queue) > 0:
            current_node = queue.pop(0)
            results.append(current_node.value)
            if current_node.left is not None:
                queue.append(current_node.left)
            if current_node.right is not None:
                queue.append(current_node.right)

        return results

    def dfs_pre_order(self):
        """
        Performs Depth-First Search in Pre-Order (Node → Left → Right).
        Returns a list of visited node values.
        """
        results = []

        def traverse(current_node):
            results.append(current_node.value)
            if current_node.left is not None:
                traverse(current_node.left)
            if current_node.right is not None:
                traverse(current_node.right)

        if self.root is not None:
            traverse(self.root)
        return results

    def dfs_post_order(self):
        """
        Performs Depth-First Search in Post-Order (Left → Right → Node).
        Returns a list of visited node values.
        """
        results = []

        def traverse(current_node):
            if current_node.left is not None:
                traverse(current_node.left)
            if current_node.right is not None:
                traverse(current_node.right)
            results.append(current_node.value)

        if self.root is not None:
            traverse(self.root)
        return results

    def dfs_in_order(self):
        """
        Performs Depth-First Search in In-Order (Left → Node → Right).
        Returns a list of visited node values in ascending order.
        """
        results = []

        def traverse(current_node):
            if current_node.left is not None:
                traverse(current_node.left)
            results.append(current_node.value)
            if current_node.right is not None:
                traverse(current_node.right)

        if self.root is not None:
            traverse(self.root)
        return results