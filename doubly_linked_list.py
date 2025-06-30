class Node:
    def __init__(self, value):
        self.value = value          # Stores the value of the node
        self.next = None            # Pointer to the next node
        self.prev = None            # Pointer to the previous node

class DoublyLinkedList:
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
        if temp:
            before = temp.prev
            after = temp.next
            before.next = after
            after.prev = before
            temp.next = None
            temp.prev = None
            self.length -= 1
            return temp