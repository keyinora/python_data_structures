class BSTNode:
    def __init__(self, val=None):
        self.left = None
        self.right = None
        self.val = val

    def insert(self, val):
        # if no value set, set it
        if self.val is None:
            self.val = val
        # no duplicates
        if self.val == val:
            return 

        # Insert to the left if the value is less than the current node's value
        if val < self.val:
            if self.left is None:
                self.left = BSTNode(val)
            else:
                self.left.insert(val)

        # Insert to the right if the value is greater than the current node's value
        elif val > self.val:
            if self.right is None:
                self.right = BSTNode(val)
            else:
                self.right.insert(val)
