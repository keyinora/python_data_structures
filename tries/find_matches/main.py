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

    def find_matches(self, document):
        matches = set()  # Set to store matched words

        # Loop over each character index in the document
        for i in range(len(document)):
            level = self.root  # Start at the root of the trie

            # Inner loop to check for words starting at each index `i`
            for j in range(i, len(document)):
                char = document[j]

                # If the character is not in the current level, break the inner loop
                if char not in level:
                    break

                # Move to the next level in the trie
                level = level[char]

                # If we've reached the end of a word, add it to matches
                if self.end_symbol in level:
                    matches.add(document[i:j+1])

        return matches
