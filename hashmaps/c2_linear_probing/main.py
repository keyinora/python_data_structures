class HashMap:
    def __init__(self, size):
        self.hashmap = [None for _ in range(size)]

    def insert(self, key, value):
        # Compute the initial index for the key
        original_index = self.key_to_index(key)
        index = original_index
        first_iteration = True

        # Loop to find an empty slot or the same key
        while self.hashmap[index] is not None and self.hashmap[index][0] != key:
            if not first_iteration and index == original_index:
                raise Exception("hashmap is full")
            
            index = (index + 1) % len(self.hashmap)  # Wrap around using modulo
            first_iteration = False

        # Insert the key-value pair at the found index
        self.hashmap[index] = (key, value)

    def get(self, key):
        # Compute the initial index for the key
        index = self.key_to_index(key)
        original_index = index

        # Loop to find the key or conclude it doesn't exist
        while self.hashmap[index] is not None:
            if self.hashmap[index][0] == key:
                return self.hashmap[index][1]  # Return the value if the key matches

            index = (index + 1) % len(self.hashmap)  # Wrap around using modulo
            
            if index == original_index:  # We've looped all the way back to start
                break

        # Raise an exception if the key is not found
        raise Exception("sorry, key not found")

    def key_to_index(self, key):
        unicode_sum = sum(ord(c) for c in key)
        return unicode_sum % len(self.hashmap)

    def __repr__(self):
        final = ""
        for i, v in enumerate(self.hashmap):
            if v is not None:
                final += f" - {str(v)}\n"
        return final
