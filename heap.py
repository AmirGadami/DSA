class MaxHeap:
    """
    A MaxHeap implementation using a list.

    Attributes:
        heap (list): The list representing the binary heap.

    Methods:
        insert(value): Adds a new value while maintaining max-heap property.
        remove(): Removes and returns the maximum value (root).
    """

    def __init__(self):
        self.heap = []  # Initialize the heap as an empty list

    # Get the index of the left child
    def _left_child(self, index):
        return 2 * index + 1

    # Get the index of the right child
    def _right_child(self, index):
        return 2 * index + 2

    # Get the index of the parent
    def _parent(self, index):
        return (index - 1) // 2

    # Swap values at two indices in the heap
    def _swap(self, index1, index2):
        self.heap[index1], self.heap[index2] = self.heap[index2], self.heap[index1]

    def insert(self, value):
        """
        Insert a new value into the heap and bubble it up to maintain max-heap property.
        """
        self.heap.append(value)
        current = len(self.heap) - 1

        # Bubble up until the heap property is restored
        while current > 0 and self.heap[current] > self.heap[self._parent(current)]:
            self._swap(current, self._parent(current))
            current = self._parent(current)

    def _sink_down(self, index):
        """
        Helper method to move a node down the tree to restore the max-heap property.
        """
        max_index = index

        while True:
            left_index = self._left_child(index)
            right_index = self._right_child(index)

            # Check if left child exists and is greater than current max
            if (left_index < len(self.heap)) and (self.heap[max_index] < self.heap[left_index]):
                max_index = left_index

            # Check if right child exists and is greater than current max
            if (right_index < len(self.heap)) and (self.heap[max_index] < self.heap[right_index]):
                max_index = right_index

            # If no swap needed, stop
            if max_index != index:
                self._swap(index, max_index)
                index = max_index
            else:
                return

    def remove(self):
        """
        Remove and return the maximum value (root) from the heap.
        """
        if len(self.heap) == 0:
            return None

        if len(self.heap) == 1:
            return self.heap.pop()

        max_value = self.heap[0]
        self.heap[0] = self.heap.pop()  # Move last to root and sink it down
        self._sink_down(0)

        return max_value