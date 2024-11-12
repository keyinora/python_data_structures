# ref.py

def ref_implementation(bst_node, user):
    """
    Inserts a user into the BST in the correct order.
    This function serves as a reference implementation for testing.
    """
    # If the node is empty, set it as the root value
    if bst_node.val is None:
        bst_node.val = user
        return

    # Avoid duplicates
    if bst_node.val == user:
        return

    # Insert to the left if the user ID is less than the current node's ID
    if user < bst_node.val:
        if bst_node.left is None:
            bst_node.left = BSTNode(user)
        else:
            ref_implementation(bst_node.left, user)

    # Insert to the right if the user ID is greater than the current node's ID
    elif user > bst_node.val:
        if bst_node.right is None:
            bst_node.right = BSTNode(user)
        else:
            ref_implementation(bst_node.right, user)


def ref_inorder(bst_node, result):
    """
    Performs an in-order traversal of the BST, appending each node's value to the result list.
    This function serves as a reference for the expected order of nodes.
    """
    if bst_node is None:
        return result
    
    ref_inorder(bst_node.left, result)
    result.append(bst_node.val)
    ref_inorder(bst_node.right, result)
    
    return result
