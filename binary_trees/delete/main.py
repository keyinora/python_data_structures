class BSTNode:
    def delete(self, val):
        # Check if the current node's value is None, representing an empty tree or leaf
        if self.val is None:
            return None

        # Traverse left if the value to delete is less than the current node's value
        if val < self.val:
            if self.left:
                self.left = self.left.delete(val)
            return self

        # Traverse right if the value to delete is greater than the current node's value
        elif val > self.val:
            if self.right:
                self.right = self.right.delete(val)
            return self

        # If we found the node to delete
        if val == self.val:
            # Case 1: Node has no right child
            if self.right is None:
                return self.left
            # Case 2: Node has no left child
            elif self.left is None:
                return self.right
            # Case 3: Node has both children
            else:
                # Find the minimum node in the right subtree
                min_larger_node = self.right
                while min_larger_node.left is not None:
                    min_larger_node = min_larger_node.left

                # Replace the current node's value with that of the min_larger_node
                self.val = min_larger_node.val

                # Delete min_larger_node from the right subtree
                self.right = self.right.delete(min_larger_node.val)

        return self

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
