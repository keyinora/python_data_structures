class Trie:
    def search_level(self, cur, cur_prefix, words):
        # If we've reached the end of a word, add the prefix to words
        if self.end_symbol in cur:
            words.append(cur_prefix)
        
        # Loop over keys in the current dictionary in sorted order
        for key in sorted(cur.keys()):
            if key != self.end_symbol:
                # Recursive call to traverse deeper into the trie
                self.search_level(cur[key], cur_prefix + key, words)
        
        return words
    
    def words_with_prefix(self, prefix):
        current = self.root  # Start at the root of the trie
        words = []  # List to hold words with the given prefix
        
        # Traverse down to the level of the last character in the prefix
        for char in prefix:
            if char not in current:
                return []  # Prefix not found, return an empty list
            current = current[char]
        
        # Call search_level starting at the level of the last prefix character
        return self.search_level(current, prefix, words)

    # don't touch below this line

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
