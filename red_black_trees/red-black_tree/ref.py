# ref.py
from main import *

# ref.py
def ref_implementation(tree, user):
    """
    Reference implementation of inserting a user into the RBTree.
    This should perform the necessary steps to insert a node into the tree
    while maintaining the red-black tree properties.
    """
    tree.insert(user)

def ref_inorder(node, result):
    """
    Performs an in-order traversal of the tree to collect node values.
    This function helps verify that the RBTree structure matches expectations.
    """
    if node.val is not None:
        ref_inorder(node.left, result)
        result.append(node.val)
        ref_inorder(node.right, result)
    return result
