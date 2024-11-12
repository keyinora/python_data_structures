class BSTNode:
    def height(self):
        """
        Calculate the height of the tree rooted at the current node.
        """
        # If the current node is empty, return 0 (empty tree)
        if self.val is None:
            return 0

        # Recursively calculate the height of the left and right subtrees
        left_height = self.left.height() if self.left else 0
        right_height = self.right.height() if self.right else 0

        # Return the greater of the left or right subtree heights, plus 1 for the current node
        return max(left_height, right_height) + 1

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
