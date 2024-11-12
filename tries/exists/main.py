class Trie:
    def exists(self, word):
        current = self.root  # Start at the root of the trie

        # Loop over each character in the word
        for char in word:
            if char not in current:
                return False  # Character not found, word doesn't exist
            current = current[char]

        # Check if end_symbol exists in the final dictionary
        return self.end_symbol in current

    # don't touch below this line

    def add(self, word):
        current = self.root
        for letter in word:
            if letter not in current:
                current[letter] = {}
            current = current[letter]
        current[self.end_symbol] = True

    def __init__(self):
        self.root = {}
        self.end_symbol = "*"
