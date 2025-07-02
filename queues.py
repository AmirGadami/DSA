class Node:
    """
    Represents a node in a singly linked list.

    Attributes:
        value (any): The data stored in the node.
        next (Node): The next node in the list (or None).
    """
    def __init__(self, value):
        self.value = value
        self.next = None


class Queue:
    """
    A queue implementation using a singly linked list (FIFO).

    Attributes:
        first (Node): The front node of the queue.
        last (Node): The rear node of the queue.
        length (int): The number of elements in the queue.

    Methods:
        print_queue(): Prints all elements in the queue from front to rear.
        enqueue(value): Adds a new node at the end of the queue.
        dequeue(): Removes and returns the node from the front of the queue.
    """
    def __init__(self, value):
        new_node = Node(value)
        self.first = new_node  # Front of the queue
        self.last = new_node   # Rear of the queue
        self.length = 1

    def print_queue(self):
        # Print all elements from front to rear
        temp = self.first
        while temp is not None:
            print(temp.value)
            temp = temp.next

    def enqueue(self, value):
        # Add a new node to the end of the queue
        new_node = Node(value)
        if self.first is None:
            self.first = new_node
            self.last = new_node
        else:
            self.last.next = new_node
            self.last = new_node
        self.length += 1
        return True

    def dequeue(self):
        # Remove and return the front node of the queue
        if self.length == 0:
            return None
        temp = self.first
        if self.length == 1:
            self.first = None
            self.last = None
        else:
            self.first = temp.next
            temp.next = None
        self.length -= 1
        return temp