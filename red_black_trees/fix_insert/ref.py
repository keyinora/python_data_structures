# ref.py

def ref_impl_ins(reference_tree, user):
    """
    Inserts a user into the reference red-black tree and maintains red-black properties.
    """
    reference_tree.insert(user)
    # After inserting, directly call fix_insert on the newly inserted node.
    last_inserted_node = reference_tree.exists(user)  # Locate the node for the inserted user
    if last_inserted_node:
        reference_tree.fix_insert(last_inserted_node)


def ref_compare(tree, reference_tree):
    """
    Compares the actual tree with the reference tree to ensure they are identical in structure.
    """
    return print_tree(tree) == print_tree(reference_tree)
