class Trie:
    def __init__(self):
        self.root = {}
        self.end_symbol = "*"

    def add(self, word):
        current = self.root
        for letter in word:
            if letter not in current:
                current[letter] = {}
            current = current[letter]
        current[self.end_symbol] = True

    def longest_common_prefix(self):
        current = self.root  # Start at the root of the trie
        prefix = ""  # Initialize an empty prefix string

        while True:
            # Get the children in the current level (keys in the dictionary)
            children = list(current.keys())

            # If we reach the end of a word, break the loop
            if self.end_symbol in children:
                break

            # If there is exactly one child, it can be part of the prefix
            if len(children) == 1:
                # Append the single child to the prefix
                char = children[0]
                prefix += char
                # Move to the next level in the trie
                current = current[char]
            else:
                # If there are multiple children or no children, break the loop
                break

        return prefix
