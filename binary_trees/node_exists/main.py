class BSTNode:
    def exists(self, val):
        """
        Check if a node with the given value exists in the tree.
        """
        # Base case: If the current node is None, the value is not found
        if self is None or self.val is None:
            return False
    
        # If the current node's value matches, the value exists in the tree
        if self.val == val:
            return True
    
        # Recurse left if the value is less than the current node's value
        elif val < self.val and self.left is not None:
            return self.left.exists(val)
    
        # Recurse right if the value is greater than the current node's value
        elif val > self.val and self.right is not None:
            return self.right.exists(val)
    
        # If the value is not found in any of the above cases, return False
        return False

        # don't touch below this line

    def __init__(self, val=None):
        self.left = None
        self.right = None
        self.val = val

    def insert(self, val):
        if not self.val:
            self.val = val
            return

        if self.val == val:
            return

        if val < self.val:
            if self.left:
                self.left.insert(val)
                return
            self.left = BSTNode(val)
            return

        if self.right:
            self.right.insert(val)
            return
        self.right = BSTNode(val)
