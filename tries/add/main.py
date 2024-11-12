class Trie:
    def add(self, word):
        current = self.root
        for char in word:
            if char not in current:
                current[char] = {}
            # Move to the next level in the trie
            current = current[char]
        # Mark the end of the word
        current[self.end_symbol] = True

    # don't touch below this line

    def __init__(self):
        self.root = {}
        self.end_symbol = "*"
