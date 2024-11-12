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
        matches = set()
        for i in range(len(document)):
            level = self.root
            for j in range(i, len(document)):
                ch = document[j]
                if ch not in level:
                    break
                level = level[ch]
                if self.end_symbol in level:
                    matches.add(document[i : j + 1])
        return matches

    def advanced_find_matches(self, document, variations):
        matches = set()

        # Loop over each character index in the document
        for i in range(len(document)):
            level = self.root  # Start at the root of the trie

            # Inner loop to check for words starting at each index `i`
            for j in range(i, len(document)):
                ch = document[j]

                # Check if character is in the variations dictionary
                if ch in variations:
                    ch = variations[ch]  # Replace with the corresponding character

                # If the character is not in the current level, break the inner loop
                if ch not in level:
                    break

                # Move to the next level in the trie
                level = level[ch]

                # If we've reached the end of a word, add it to matches
                if self.end_symbol in level:
                    matches.add(document[i:j+1])

        return matches
