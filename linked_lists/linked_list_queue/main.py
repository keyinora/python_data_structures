from node import Node


class LinkedList:
    def add_to_head(self, node):
        node.set_next(self.head)
        # If the list is empty, set both head and tail to the new node
        if not self.head:
            self.head = node
            self.tail = node
        else:
            # Point the new node's next to the current head and update the head
            node.next = self.head
            self.head = node
            

    def add_to_tail(self, node):
        # If the list is empty, set both head and tail to the new node
        if not self.head:
            self.head = node
            self.tail = node
        else:
            # Link the current tail to the new node and update the tail
            self.tail.next = node
            self.tail = node


    def __init__(self):
        self.head = None
        self.tail = None
    # don't touch below this line

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
