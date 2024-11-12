class BSTNode:
    def inorder(self, visited):
        """
        Perform an inorder traversal of the tree and return the visited nodes.
        """
        # Traverse the left subtree
        if self.left is not None:
            self.left.inorder(visited)
    
        # Visit the current node
        if self.val is not None:
            visited.append(self.val)
    
        # Traverse the right subtree
        if self.right is not None:
            self.right.inorder(visited)
    
        return visited

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
