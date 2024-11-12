class BSTNode:
    def get_min(self):
         # Traverse to the leftmost node
        current = self
        while current.left is not None:
            current = current.left
        return current.val

    def get_max(self):
        # Traverse to the rightmost node
        current = self
        while current.right is not None:
            current = current.right
        return current.val

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
