class HashMap:
    def __init__(self, size):
        self.hashmap = [None for _ in range(size)]
        self.num_items = 0  # Track the number of filled buckets

    def insert(self, key, value):
        # Call resize to check if we need to expand the hashmap before inserting
        self.resize()

        # Find the index for the key
        index = self.key_to_index(key)

        # Insert the key-value pair or handle collision using linear probing
        while self.hashmap[index] is not None:
            if self.hashmap[index][0] == key:
                # Update the value if the key already exists
                self.hashmap[index] = (key, value)
                return
            index = (index + 1) % len(self.hashmap)  # Linear probing

        # Insert the new key-value pair and increment the filled bucket count
        self.hashmap[index] = (key, value)
        self.num_items += 1

    def resize(self):
        if len(self.hashmap) == 0:
            self.hashmap = [None]  # Set length to 1 if currently 0
            return

        # Calculate current load
        load = self.current_load()
        if load < 0.05:  # Less than 5%, no need to resize
            return

        # Create a new hashmap with 10x the size
        new_size = len(self.hashmap) * 10
        new_hashmap = [None] * new_size
        old_hashmap = self.hashmap

        # Update to new hashmap and reset item count
        self.hashmap = new_hashmap
        self.num_items = 0  # Will be recalculated as items are reinserted

        # Reinsert each item from the old hashmap into the new one
        for item in old_hashmap:
            if item is not None:
                key, value = item
                self.insert(key, value)

    def current_load(self):
        if len(self.hashmap) == 0:
            return 1
        return self.num_items / len(self.hashmap)

    def key_to_index(self, key):
        unicode_sum = sum(ord(c) for c in key)
        return unicode_sum % len(self.hashmap)

    def __repr__(self):
        final = ""
        for i, v in enumerate(self.hashmap):
            if v is not None:
                final += f" - {str(v)}\n"
        return final
