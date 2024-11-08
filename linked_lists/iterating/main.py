from node import Node


class LinkedList:
    def __init__(self):
        self.head = None

    def __iter__(self):
      # Initialize the current node as the head
        node = self.head
        # Yield each node until we reach the end of the list
        while node is not None:
            yield node
            node = node.next

    # don't touch below this line

    def __repr__(self):
        nodes = []
        current = self.head
        while current and hasattr(current, "val"):
            nodes.append(current.val)
            current = current.next
        return " -> ".join(nodes)
