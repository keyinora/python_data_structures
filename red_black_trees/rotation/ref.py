# ref.py
from main import *

# ref.py

def ref_impl_left(reference_tree, pivot_parent):
    """
    Reference left rotation operation for the reference tree.
    This will rotate the right child of pivot_parent up.
    """
    if pivot_parent is None or pivot_parent.right == reference_tree.nil:
        return  # Nothing to do if pivot_parent or its right child is nil

    pivot = pivot_parent.right
    pivot_parent.right = pivot.left

    if pivot.left != reference_tree.nil:
        pivot.left.parent = pivot_parent

    pivot.parent = pivot_parent.parent

    if pivot_parent.parent is None:
        reference_tree.root = pivot
    elif pivot_parent == pivot_parent.parent.left:
        pivot_parent.parent.left = pivot
    else:
        pivot_parent.parent.right = pivot

    pivot.left = pivot_parent
    pivot_parent.parent = pivot

def ref_impl_right(reference_tree, pivot_parent):
    """
    Reference right rotation operation for the reference tree.
    This will rotate the left child of pivot_parent up.
    """
    if pivot_parent is None or pivot_parent.left == reference_tree.nil:
        return  # Nothing to do if pivot_parent or its left child is nil

    pivot = pivot_parent.left
    pivot_parent.left = pivot.right

    if pivot.right != reference_tree.nil:
        pivot.right.parent = pivot_parent

    pivot.parent = pivot_parent.parent

    if pivot_parent.parent is None:
        reference_tree.root = pivot
    elif pivot_parent == pivot_parent.parent.left:
        pivot_parent.parent.left = pivot
    else:
        pivot_parent.parent.right = pivot

    pivot.right = pivot_parent
    pivot_parent.parent = pivot

def ref_compare(node1, node2):
    """
    Compares two nodes recursively to check if two trees are identical in structure and values.
    """
    if node1 is None and node2 is None:
        return True
    if node1 is None or node2 is None:
        return False
    if node1.val != node2.val or node1.red != node2.red:
        return False
    return ref_compare(node1.left, node2.left) and ref_compare(node1.right, node2.right)
