from node import Node


class LinkedList:
    def add_to_tail(self, node):
        # Create a new node with the given value
        new_node = node
        # If the list is empty, set the new node as the head
        if not self.head:
            self.head = new_node
        else:
            # Traverse to the end of the list and add the new node
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
            

    # don't touch below this line

    def __init__(self):
        self.head = None

    def __iter__(self):
        node = self.head
        while node is not None:
            yield node
            node = node.next

    def __repr__(self):
        nodes = []
        for node in self:
            nodes.append(node.val)
        return " -> ".join(nodes)
