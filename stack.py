from node import Node

class Stack:
    def __init__(self, top=None):
        self.top = top

    def push(self, item):
        if self.top == None:
            self.top = Node(item, None)
            return

        node = Node(item, self.top)
        self.top = node

    def pop(self):
        node = self.top
        self.top = node.next
        return node.value