class Node:
    """
    Represents a node in a doubly linked list.

    Attributes:
        value (any): The data stored in the node.
        next (Node): Reference to the next node in the list.
        prev (Node): Reference to the previous node in the list.
    """

    def __init__(self, value):
        self.value = value   # Data held by the node
        self.next = None     # Pointer to the next node
        self.prev = None     # Pointer to the previous node

class DoublyLinkedList:
    """
    A doubly linked list implementation.

    Attributes:
        head (Node): The first node in the list.
        tail (Node): The last node in the list.
        length (int): Number of nodes in the list.

    Methods:
        print_list(): Prints all node values from head to tail.
        append(value): Adds a node to the end of the list.
        pop(): Removes and returns the last node.
        prepend(value): Adds a node to the beginning of the list.
        pop_first(): Removes and returns the first node.
        get(index): Returns the node at a given index.
        set_value(index, value): Updates the value of a node.
        insert(index, value): Inserts a node at the specified index.
        remove(index): Removes a node at the specified index.
    """

    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node        # First node in the list
        self.tail = new_node        # Last node in the list
        self.length = 1             # Number of nodes in the list

    def print_list(self):
        # Print all node values from head to tail
        temp = self.head
        while temp:
            print(temp.value)
            temp = temp.next

    def append(self, value):
        # Add a node to the end
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1
        return True

    def pop(self):
        # Remove and return the last node
        if self.length == 0:
            return None
        temp = self.tail
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.tail = temp.prev
            self.tail.next = None
            temp.prev = None
        self.length -= 1
        return temp

    def prepend(self, value):
        # Add a node to the beginning
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        self.length += 1
        return True

    def pop_first(self):
        # Remove and return the first node
        if self.length == 0:
            return None
        temp = self.head
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.head = temp.next
            self.head.prev = None
            temp.next = None
        self.length -= 1
        return temp

    def get(self, index):
        # Return the node at a given index
        if index < 0 or index >= self.length:
            return None

        if index < self.length // 2:
            temp = self.head
            for _ in range(index):
                temp = temp.next
        else:
            temp = self.tail
            for _ in range(self.length - 1, index, -1):
                temp = temp.prev

        return temp

    def set_value(self, index, value):
        # Set the value of the node at the given index
        temp = self.get(index)
        if temp:
            temp.value = value
            return True
        return False

    def insert(self, index, value):
        # Insert a node at a specific index
        if index < 0 or index > self.length:
            return False
        if index == 0:
            return self.prepend(value)
        if index == self.length:
            return self.append(value)

        new_node = Node(value)
        before = self.get(index - 1)
        after = before.next

        new_node.prev = before
        new_node.next = after
        before.next = new_node
        after.prev = new_node

        self.length += 1
        return True

    def remove(self, index):
        # Remove and return the node at the given index
        if index < 0 or index >= self.length:
            return None
        if index == 0:
            return self.pop_first()
        if index == self.length - 1:
            return self.pop()

        temp = self.get(index)
        before = temp.prev
        after = temp.next
        before.next = after
        after.prev = before
        temp.next = None
        temp.prev = None
        self.length -= 1
        return temp