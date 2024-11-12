class RBNode:
    def __init__(self, val):
        self.red = False
        self.parent = None
        self.val = val
        self.left = None
        self.right = None


class RBTree:
    def __init__(self):
        self.nil = RBNode(None)
        self.nil.red = False
        self.nil.left = None
        self.nil.right = None
        self.root = self.nil

    def rotate_left(self, pivot_parent):
        if pivot_parent is None or pivot_parent.right == self.nil:
            return  # Nothing to do if pivot_parent or its right child is nil

        pivot = pivot_parent.right  # The node to be rotated up
        pivot_parent.right = pivot.left  # Pivot's left child becomes pivot_parent's new right child

        if pivot.left != self.nil:
            pivot.left.parent = pivot_parent  # Update parent reference if pivot has a left child

        pivot.parent = pivot_parent.parent  # Pivot's parent becomes pivot_parent's parent

        if pivot_parent.parent is None:  # If pivot_parent is root
            self.root = pivot  # Pivot becomes the new root
        elif pivot_parent == pivot_parent.parent.left:
            pivot_parent.parent.left = pivot  # Pivot takes pivot_parent's place as left child
        else:
            pivot_parent.parent.right = pivot  # Pivot takes pivot_parent's place as right child

        pivot.left = pivot_parent  # Set pivot_parent as pivot's new left child
        pivot_parent.parent = pivot  # Update pivot_parent's parent to pivot

    def rotate_right(self, pivot_parent):
        if pivot_parent is None or pivot_parent.left == self.nil:
            return  # Nothing to do if pivot_parent or its left child is nil

        pivot = pivot_parent.left  # The node to be rotated up
        pivot_parent.left = pivot.right  # Pivot's right child becomes pivot_parent's new left child

        if pivot.right != self.nil:
            pivot.right.parent = pivot_parent  # Update parent reference if pivot has a right child

        pivot.parent = pivot_parent.parent  # Pivot's parent becomes pivot_parent's parent

        if pivot_parent.parent is None:  # If pivot_parent is root
            self.root = pivot  # Pivot becomes the new root
        elif pivot_parent == pivot_parent.parent.left:
            pivot_parent.parent.left = pivot  # Pivot takes pivot_parent's place as left child
        else:
            pivot_parent.parent.right = pivot  # Pivot takes pivot_parent's place as right child

        pivot.right = pivot_parent  # Set pivot_parent as pivot's new right child
        pivot_parent.parent = pivot  # Update pivot_parent's parent to pivot

        # don't touch below this line

    def insert(self, val):
        new_node = RBNode(val)
        new_node.parent = None
        new_node.left = self.nil
        new_node.right = self.nil
        new_node.red = True

        parent = None
        current = self.root
        while current != self.nil:
            parent = current
            if new_node.val < current.val:
                current = current.left
            elif new_node.val > current.val:
                current = current.right
            else:
                # duplicate, just ignore
                return

        new_node.parent = parent
        if parent is None:
            self.root = new_node
        elif new_node.val < parent.val:
            parent.left = new_node
        else:
            parent.right = new_node
