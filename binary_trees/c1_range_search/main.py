class BSTNode:
    def search_range(self, lower_bound, upper_bound):
        result = []
        
        # Helper function for in-order traversal with range check
        def in_order(node):
            if not node:
                return
            
            # Traverse the left subtree only if there could be values within the range
            if node.val > lower_bound:
                in_order(node.left)
            
            # Add the current node if it falls within the range
            if lower_bound <= node.val <= upper_bound:
                result.append(node.val)
            
            # Traverse the right subtree only if there could be values within the range
            if node.val < upper_bound:
                in_order(node.right)

        # Start the in-order traversal from the root
        in_order(self)
        return result

    # Rest of the BSTNode class remains unchanged
    def exists(self, val):
        if val == self.val:
            return True

        if val < self.val:
            if self.left is None:
                return False
            return self.left.exists(val)

        if self.right is None:
            return False
        return self.right.exists(val)

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
