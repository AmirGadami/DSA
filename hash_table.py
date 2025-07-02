class HashTable:
    """
    A basic hash table implementation using separate chaining for collision resolution.

    Attributes:
        data_map (list): An internal list of buckets, each bucket is a list of key-value pairs.

    Methods:
        __hash(key): Private method to generate hash index for a given key.
        set_item(key, value): Stores a key-value pair in the hash table.
        get_item(key): Retrieves the value associated with the given key.
        keys(): Returns a list of all keys in the hash table.
        print_table(): Prints the hash table's contents.
    """

    def __init__(self, size=7):
        self.data_map = [None] * size  # Initialize buckets

    def __hash(self, key):
        # Generate a hash index from a string key
        my_hash = 0
        for letter in key:
            my_hash = (my_hash + ord(letter) * 23) % len(self.data_map)
        return my_hash

    def print_table(self):
        # Display all key-value pairs in the table
        for i, val in enumerate(self.data_map): 
            print(i, ": ", val)

    def set_item(self, key, value):
        # Store a key-value pair in the table
        index = self.__hash(key)
        if self.data_map[index] is None:
            self.data_map[index] = []
        self.data_map[index].append([key, value])

    def get_item(self, key):
        # Retrieve the value for a given key
        index = self.__hash(key)
        if self.data_map[index] is not None:
            for pair in self.data_map[index]:
                if pair[0] == key:
                    return pair[1]
        return None

    def keys(self):
        # Return a list of all keys in the table
        all_keys = []
        for bucket in self.data_map:
            if bucket is not None:
                for pair in bucket:
                    all_keys.append(pair[0])
        return all_keys